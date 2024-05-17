from django.shortcuts import render, redirect
from app01 import models
import json


# Create your views here.
def depart_list(request):
    # 在数据库中获得所有的部门信息
    # [数据，数据，数据]
    query_set = models.Department.objects.all()
    return render(request, 'index.html', {'query_set': query_set})


def depart_add(request):
    """添加页面"""

    # GET请求
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    print("POST请求")
    # POST请求
    depart_name = request.POST.get('Depart')
    print(depart_name)

    # 添加到数据库
    models.Department.objects.create(title=depart_name)

    # 返回到部门列表页面
    return redirect('/depart/list/')


def depart_delete(request):
    """删除部门页面"""

    # 这里删除完之后id并没有被重置
    # 如果需要重置执行以下代码
    # with connection.cursor() as cursor:
    #     cursor.execute("ALTER TABLE app01_department AUTO_INCREMENT = 1;")

    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()  # 删除数据库中的数据

    return redirect('/depart/list/')


def depart_edit(request, nid):
    """编辑部门页面"""

    # 如果是GET请求，返回编辑页面
    if request.method == 'GET':
        obj = models.Department.objects.filter(id=nid).first()
        print(obj.id, obj.title)
        return render(request, 'depart_edit.html', {'depart_name': obj.title})

    # 如果是POST请求，修改数据库中的数据
    deaprt_name = request.POST.get('Depart')
    models.Department.objects.filter(id=nid).update(title=deaprt_name)

    return redirect('/depart/list/')


def user_list(request):
    """员工列表"""

    # 获取所有员工信息
    query_set = models.UserInfo.objects.all()

    # 获取所有部门信息
    depart = models.Department.objects.all()

    return render(request, 'user_list.html', {'query_set': query_set, 'depart_list': depart})
