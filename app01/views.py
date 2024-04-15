from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hello!')

def login(request):
    """
    登录视图函数
    :param request: 请求对象
    :return:   返回登录页面
    """
    # 由于在settings.py中配置了TEMPLATES，所以可以直接使用render方法渲染模板文件
    # 1.先搜索根目录下的templates文件夹
    # 2.再按注册表顺序搜索每个app下的templates文件夹
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')