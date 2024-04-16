from django.shortcuts import render, HttpResponse
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
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def news(req):
    # 向特定网页发送请求
    response = requests.get('http://www.baidu.com')

    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取所有的段落
    paragraphs = soup.find_all('p')

    # 打印每个段落
    for p in paragraphs:
        print(p.get_text().encode('utf-8'))

    return render(req, 'news.html')
