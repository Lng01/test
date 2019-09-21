# -*- coding: utf-8 -*-
from django.shortcuts import render

from testapp import models

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    notes = models.Note.objects.all()
    # 创建一个空的字典
    context = {'notes_list': notes}
    # 把数据装载进字典，字典的key-value建议相同
    # 使用render函数进行渲染，接收三个参数：请求、模板名称、上下文
    return render(request, 'testapp/templates/home.html', context)
