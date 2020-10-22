from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cal(request):
    return render(request,'cal.html')

def js(request):
    number1=eval(request.POST.get('number1'))
    number2=eval(request.POST.get('number2'))
    sum=number1+number2
    print(sum)
    return HttpResponse(sum)


def index(request):
    return render(request,'index.html')