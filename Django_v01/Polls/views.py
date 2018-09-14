from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template("polls/index.html")
    context = {'latest_question_list' : latest_question_list}
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # 没找到这个问题给个404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # 快捷方式写法：需要从shortcut导入get_object_or_404
    question = get_object_or_404(Question, pk=question_id)

    # return HttpResponse("You are looking at the question {0}".format(question_id))
    return render(request, "polls/detail.html", {'question' : question})


def results(request, question_id):
    response = "You are looking at the results of question {0}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 重新显示该问题的表单
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 始终在成功处理 POST 数据后返回一个 HttpResponseRedirect ，
        # （合并上句） 这样可以防止用户点击“后退”按钮时数据被发送两次。
        # （合并至上一句）
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))