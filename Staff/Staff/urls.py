"""Staff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app01.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 部门管理
    path('depart/list/', app01.views.depart_list),
    path('depart/add/', app01.views.depart_add),
    path('depart/delete/', app01.views.depart_delete),
    # 中间加入一个参数，则在视图函数中也要加入一个参数
    # 比如http://localhost:8000/depart/1/edit/
    path('depart/<int:nid>/edit/', app01.views.depart_edit),

    # 员工管理
    path('user/list/', app01.views.user_list),
    path('user/add/', app01.views.user_add),
]
