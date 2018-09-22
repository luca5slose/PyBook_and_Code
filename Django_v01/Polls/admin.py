from django.contrib import admin
from .models import Question, Choice
# Register your models here.


# 先移除choice的register调用，然后在QuestionAdmin添加inlines字段
# 这个类加inlines字段的作用是在管理页面外键Choice所属的页面给主键Question添加一个新的的时候
# 默认提供其他三个Choice的空间便于填写，相当于一个问题默认三个选项
# 页面还有额外添加选项的按钮，也有delete列可以删除除了默认三个之外新加的选项。
# 有个问题是很多个选项会竖排占用屏幕大量的空间，而修改admin.StackedInline为admin.TabularInline
# 这个方法会使得显示内联相关对象的表格，就是紧凑横排
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # 在管理页面把pub_date放在question_text前面
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 对于拥有很多字段的表单，把表单分割成字段集
    # fieldsets中每个元组第一个元素是字段集的标题
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_display变量是要显示的字段名称的元组，是你想要在Question管理页面看到什么字段
    # 在显示页面was_published_recently的下划线会被替换成空格
    # 还可以根据pub_date进行排序，was_published_recently就不行，但需要在models修改一些属性
    inlines = [ChoiceInline]

    # 添加一个“Filter”侧边栏，可以使人们通过pub_date字段对变更列表进行过滤，会自动匹配字段对应的过滤器
    list_filter = ['pub_date']

    # 在顶部添加一个搜索框，可以用任意数量的字段进行搜索，但是在后台是用LIKE进行查询
    # 所以限制一下搜索的字段数会更容易查询
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)



