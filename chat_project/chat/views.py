from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Room
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'chat/index.html')
def room_list(request):
    """房间选择页面"""
    rooms = Room.objects.all()  # 查询所有房间
    return render(request, 'chat/room_list.html', {'rooms': rooms})
@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "注册成功！请登录。")
            return redirect("/login/")  # 注册成功后跳转到登录页面
        else:
            messages.error(request, "注册失败，请检查表单内容。")
    else:
        form = UserCreationForm()

    return render(request, "chat/register.html", {"form": form})
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"欢迎回来, {username}！")
            return redirect("index")
        else:
            messages.error(request, "用户名或密码错误！")
    
    return render(request, "chat/login.html")  