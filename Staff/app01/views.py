from django.shortcuts import render, redirect
from app01 import models
from django.utils import timezone
from django import forms


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
    depart_name = request.POST.get('Depart')
    models.Department.objects.filter(id=nid).update(title=depart_name)

    return redirect('/depart/list/')


def user_list(request):
    """员工列表"""

    # 获取所有员工信息
    query_set = models.UserInfo.objects.all()

    # 获取所有部门信息
    depart = models.Department.objects.all()

    return render(request, 'user_list.html', {'query_set': query_set, 'depart_list': depart})


def user_add(request):
    """添加员工"""

    # GET请求
    if request.method == 'GET':
        context = {
            'depart_list': models.Department.objects.all(),
            'gender_choice': models.UserInfo.gender_choices
        }
        return render(request, 'user_add.html', context)

    # POST请求
    user_name = request.POST.get('name')
    age = request.POST.get('age')
    pwd = request.POST.get('pwd')
    salary = request.POST.get('ac')

    ctime = request.POST.get('ctime')
    print(ctime)
    ctime = timezone.datetime.strptime(ctime, "%Y-%m-%d")

    gender_id = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加用户进入数据库
    models.UserInfo.objects.create(
        name=user_name,
        age=age,
        password=pwd,
        salary=salary,
        create_time=ctime,
        depart_id=depart_id,
        gender=gender_id
    )

    return redirect('/user/list/')


class UserModelForm(forms.ModelForm):
    create_time = forms.DateTimeField(
        label='创建时间',
        widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = models.UserInfo
        fields = ['name', 'age', 'password', 'salary', 'create_time', 'depart', 'gender']

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'create_time':
                field.widget.attrs = {'class': 'form-control'}
            if name == 'name':
                # 设置输入的最长长度
                field.widget.attrs = {'class': 'form-control', 'maxlength': '3'}


def user_model_form_add(request):
    """使用ModelForm添加数据"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})

    form = UserModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_model_form_add.html', {'form': form})
