from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.views import generic
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
# Create your views here.

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template("polls/index.html")
    context = {'latest_question_list' : latest_question_list}
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
'''


# 改成通用视图，解决冗余问题
# 通用视图分为ListView，DetailView和TemplateView
# TemplateView一般只用在需要返回模板的时候
# ListView相当于默认model.objects.all()，取出某个类的所有数据丢给模板，一般需要自己重写获取数据方法
# DetailView一般用来获取详细信息，比如ListView获取一个列表，然后DetailView得到列表里的某一项的详细信息
class IndexView(generic.ListView):
    # 这两个也是固定操作
    # 指定模板和指定上下文变量
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # 重写了通用视图中获取数据的方法，默认获取方法是制定model变量后自动获取比如去掉下面的方法再加上model=Quetion
    # 重写的是MultipleObjectMixin里的方法
    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        # -pub_date和pub_date区别是前者是desc从大到小后者是asc从小到大

        # 改进：和timezone.now()进行比较来检查日期，pub_date小于等于当前时间
        # 顺序是这样的，先filter找到pub_date小于当前时间的然后全拿出来，在根据pub_date从大到小拍个序并拿出前五条
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


'''
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
'''


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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