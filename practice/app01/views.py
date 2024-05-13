from django.shortcuts import render, HttpResponse, redirect
import requests
from bs4 import BeautifulSoup


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

    if request.method == 'GET':
        print(request.GET)
        print(request.method)
        print(request.GET.get('username'))
        print(request.GET.get('password'))
        return render(request,  'login.html')
    else:
        print(request.POST)
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        if request.POST.get('username') == 'admin' and request.POST.get('password') == '123':
            return HttpResponse('登录成功')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

def register(request):
    return render(request, 'register.html')


def news(req):
    # 向特定网页发送请求
    response = requests.get('http://www.baidu.com')

    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取所有的段落
    paragraphs = soup.find_all('p')

    # 将每个段落的文本存储到一个列表中
    paragraph_texts = [p.get_text() for p in paragraphs]

    # 获取所有的文字信息
    text = soup.get_text()

    # 将段落列表传递给模板
    return render(req, 'news.html', {'text': text, 'paragraphs': paragraph_texts, 'title': '百度新闻'})


def something(request):
    # request是一个HttpRequest对象，封装了用户请求的所有内容

    # 1. 获取请求方式
    print(request.method)

    # 2. 在URL上传递的参数
    print(request.GET)

    # 3. 在请求体中提交的参数
    print(request.POST)

    # 4. 返回一个响应对象
    # return HttpResponse('Something')

    # 5. 返回一个HTMl页面+渲染（替换）-》 字符串，返回给浏览器
    # return render(request, 'something.html',{"title": 'Coming Soon'})

    # 6. 重定向,该地的原理是返回一个响应对象，让浏览器重新请求另一个URL
    # 而不是返回一个HTML页面，也不是返回一个字符串
    return redirect("https://www.baidu.com")
