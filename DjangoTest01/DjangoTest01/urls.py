"""
URL configuration for DjangoTest01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # 添加路由，当用户发送请求时，执行myapp.views.hello函数
    path('', views.hello),
 
    # 获取全部用户信息
    path('user/list/', views.user_list),
    # 获取指定id的用户信息，<int:user_id>是RESTful API风格请求，将请求url的最后一段值作为请求参数
    path('user/<int:user_id>/', views.user_list),
    path('user/add/', views.user_add),
    path('user/update/<int:user_id>/', views.user_update),
    path('user/del/<int:user_id>/', views.user_del),
]
