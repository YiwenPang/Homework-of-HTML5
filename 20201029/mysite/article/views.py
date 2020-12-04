from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from article.models import Types, Articles


def articlelist(request):
    articles = Articles.objects.all()
    return render(request, 'article-list.html', {'articles': articles})


def articleadd(request):
    if request.method == 'GET':
        types = Types.objects.all()
        print(types)
        return render(request, 'article-add.html', {'types': types})
    else:
        title = request.POST.get("title")
        type = request.POST.get("type")
        content = request.POST.get("content")
        author = request.session.get("id")
        article = Articles(title=title, content=content, type_id=type, author_id=author)
        article.save()
        return HttpResponse("文章添加成功！")


def typeinit(request):
    type = Types(title='国内新闻')
    type.save()
    type = Types(title='国际新闻')
    type.save()
    type = Types(title='财经新闻')
    type.save()
    return render(request, 'temp.html', {"info": "文章类型初始化完成！"})


def articledel(request):
    id = request.POST.get('id')
    Articles.objects.filter(id=id)[0].delete()
    return HttpResponse("1")


def articleedit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        article = Articles.objects.filter(id=id)[0]
        types = Types.objects.all()
        return render(request, 'article-edit.html', {'article': article, 'types': types})
    else:
        title = request.POST.get("title")
        type = request.POST.get("type")
        content = request.POST.get("content")
        id = request.POST.get("id")
        author = request.session.get("id")
        article = Articles.objects.filter(id=id)[0]
        article.title = title
        article.type_id = type
        article.author_id = author
        article.content = content
        article.save()
        return HttpResponse("修改成功！")
