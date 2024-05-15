from django.shortcuts import render,redirect
from app01 import models


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

    # POST请求
    depart_name = request.POST.get('depart')

    # 添加到数据库
    models.Department.objects.create(title=depart_name)

    # 返回到部门列表页面
    return redirect('/depart/list/')