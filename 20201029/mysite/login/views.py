from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from login.models import Users


def login(request):
    if request.session.get('id', None):
        print("1")
        return  redirect('/login/index/')
    if request.method == "GET":
        print("2")
        return render(request, 'login.html')
    else:
        print("3")
        username = request.POST.get("username")
        password = request.POST.get("password")
        info = ""
        # if username=="admin" and password=="123":
        # print(Users.objects.get(username=username, password=password))
        res = Users.objects.filter(username=username, password=password)
        # print(res[0].id)
        # print(res[0].username)
        if res :
            print("4")
            request.session['id'] = res[0].id
            request.session['username'] = res[0].username
            return redirect('/login/index/')
        else:
            print("5")
            info = "登录失败！"
        print("6")
        return render(request, 'temp.html', {"info": info})


def init(request):
    username = "admin"
    password = "1234"
    users = Users()
    users.username = username
    users.password = password
    try:
        users.save()
    except IntegrityError:
        return HttpResponse("用户名重复！")
    return HttpResponse("ok")

# session
def index(request):
    if request.session.get('id', None):
        return render(request, 'index.html')
    else:
        return HttpResponse("请重新登录！")


def exit(request):
    if request.session.get('id', None):
        del request.session['id']
    if request.session.get('username', None):
        del request.session['username']
    return redirect('/login/login/')


def welcome(request):
    return render(request, 'welcome.html')