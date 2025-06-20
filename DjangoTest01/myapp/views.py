from django.shortcuts import render

# Create your views here.
import json
from datetime import datetime
 
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
 
from myapp.models import User
 
 
def hello(request):
    print(request.method)  # 获取请求方式
    print(request.path)  # 获取请求路径
    return HttpResponse("Hello World")  # 返回一个字符串到前端
 
 # 获取用户列表
def user_list(request, user_id=None):
    if request.method != "GET":
        return JsonResponse({'message': '请求方式错误，应使用GET请求 ！！！'})
    print("GET请求参数：", request.GET)  # 获取get请求路径中的参数
 
    if user_id:  # 如果提供了用户ID，则返回单个用户的信息
        try:
            # 查询指定id，且isdel字段等于0的用户信息
            user = User.objects.filter(isdel=0).get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'message': '未找到该用户信息 ！！！'})
 
        user = model_to_dict(user)  # 转换为字典类型
        return JsonResponse(user)
 
    # 查询用户列表，返回的是QuerySet类型
    users = User.objects.filter(isdel=0).all()
    # 遍历数据
    for user in users.values():
        print(user)
        break
 
    # 将数据转换为list类型
    user_list = list(users.values())
    # 向前端返回JSON字符串，safe=False允许传入非字典类型数据
    return JsonResponse(user_list, safe=False)
 
 
@csrf_exempt  # 跳过csrf验证
def user_add(request):
    if request.method != "POST":
        return JsonResponse({'message': '请求方式错误，应使用POST请求 ！！！'})
 
    request_data = json.loads(request.body)  # 获取请体中的参数
    print(request_data)
 
    now_time = datetime.now()
    user = User(name=request_data.get('name'),
                account=request_data.get('account'),
                password=request_data.get('password'),
                age=request_data.get('age'),
                gender=request_data.get('gender'),
                money=0.00,
                create_time=now_time,
                update_time=now_time,
                isdel=0,
                )
    print(user.name, user.create_time)
    user.save()
    return JsonResponse({'message': '添加成功'})
 
 
@csrf_exempt  # 跳过csrf验证
def user_update(request, user_id):
    if request.method != "PUT":
        return JsonResponse({'message': '请求方式错误，应使用PUT请求 ！！！'})
    try:
        user = User.objects.filter(isdel=0).get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'message': '未找到该用户信息 ！！！'})
 
    request_data = json.loads(request.body)  # 获取请体中的参数
    print(request_data)
 
    user.name = request_data.get('name')
    user.password = request_data.get('password')
    user.age = request_data.get('age')
    user.gender = request_data.get('gender')
    user.update_time = datetime.now()
    print(user.name, user.update_time)
    user.save()
 
    return JsonResponse({'message': '修改成功'})
 
 
@csrf_exempt  # 跳过csrf验证
def user_del(request, user_id):
    if request.method != "DELETE":
        return JsonResponse({'message': '请求方式错误，应使用DELETE请求 ！！！'})
    try:
        user = User.objects.filter(isdel=0).get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'message': '未找到该用户信息 ！！！'})
 
    user.isdel = 1
    user.save()
    # change_row = User.objects.filter(id=user_id).delete()  # 真删除
    return JsonResponse({'message': '删除成功'})
