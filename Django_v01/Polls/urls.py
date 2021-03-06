from django.conf.urls import url
from . import views

# 添加命名空间，使得django能分得清一个项目下不同应用的url。
# 做法是添加一个app_name属性然后在使用url的时候在前面加上应用名称如polls:detail
app_name = 'polls'

urlpatterns = [
    # ex:/polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex:/polls/5
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex:/polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex:/polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
