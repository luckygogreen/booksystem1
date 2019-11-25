from django.shortcuts import render,HttpResponse,redirect
from bookAPP import models
# Create your views here.
#测试用方法
def test(request):
    return render(request,'test.html')
#单表操作读取数据
def publisherlist(request):
    res = models.publishinfo.objects.all()
    return render(request,'publisherlist.html',{'publisherlist':res})
#单表操作添加数据 # 用方法直接执行浏览器的返回操作，叫做FBV = function build view
def addpublisher(request):
    if request.method == 'POST':
        models.publishinfo.objects.create(pname=request.POST['publishname'])
        return redirect('/publisherlist/')
    return render(request,'addpublisher.html')
#单表操作添加数据 # 用类直接执行浏览器的返回操作，叫做CBV = Class build view
#用类执行浏览器的返回操作必须要导入，view包,
from django.views import View
class Add_publisher(View):
    def get(self,request):
        return render(request,'addpublisher.html')
    def post(self,request):
        models.publishinfo.objects.create(pname=request.POST['publishname'])
        return redirect('/publisherlist/')
#单表操作删除数据
def deletepublish(request):
    if request.GET:
        models.publishinfo.objects.filter(pid=request.GET['pid']).delete()
        return redirect('/publisherlist/')
    return HttpResponse('Nothing for delete!')
#单表操作修改数据
def editpublisher(request):
    if request.method == 'POST':
        publishobject = models.publishinfo.objects.get(pid=request.POST['editpublishid'])
        publishobject.pname = request.POST['editpublishname']
        publishobject.save()
        return redirect('/publisherlist/')
    if request.GET:
        res = models.publishinfo.objects.get(pid=request.GET['pid'])
        return render(request,'editpublisher.html',{'editpublisher':res})
    return HttpResponse('Nothiing for edit!')
#一对多外键关系表查询数据
def bookslist(request):
    booslist = models.bookinfo.objects.all()
    return render(request,'bookslist.html',{'booklist':booslist})
#一对多外键关系表添加数据
def addbook(request):
    if request.method == 'POST':
        print(request.POST['publisherselect'])
        models.bookinfo.objects.create(bname=request.POST['bookname'],book_pubish_id=request.POST['publisherselect'])
        return redirect('/bookslist/')
    publisherlist = models.publishinfo.objects.all()
    return render(request,'addbook.html',{'publisherlist':publisherlist})
#一对多外键关系表删除数据
def deletebook(request):
    if request.GET:
        models.bookinfo.objects.filter(bid=request.GET['bid']).delete()
        return redirect('/bookslist/')
    return HttpResponse('Nothing for delete!')
#一对多外键关系表修改数据
def editbook(request):
    if request.method == 'POST':
        bookobject = models.bookinfo.objects.get(bid=request.POST['bookid'])
        bookobject.bname = request.POST['bookname']
        bookobject.book_pubish_id = request.POST['publisherselect']
        bookobject.save()
        return redirect('/bookslist/')
    if request.GET:
        bookselect = models.bookinfo.objects.get(bid=request.GET['bid'])
        publishlist = models.publishinfo.objects.all()
        return render(request,'editbook.html',{'bookselect':bookselect,'publishlist':publishlist})
    return HttpResponse('Nothing for edit!')
#多对多外键关系表查询数据
def authorslist(request):
    authorlist = models.authorinfo.objects.all()
    return render(request,'authorslist.html',{'authorlist':authorlist})
#多对多外键关系表查添加数据
def addauthor(request):
    if request.method == 'POST':
        allbooks = request.POST.getlist('booksselect')
        print(allbooks)
        authorobject = models.authorinfo.objects.create(aname=request.POST['authorname'])
        authorobject.author_book_publish.set(allbooks)
        return  redirect('/authorslist/')
    allbooks = models.bookinfo.objects.all()
    return render(request,'addauthor.html',{'bookslist':allbooks})
#多对多外键关系表删除数据
def deleteauthor(request):
    if request.GET:
        models.authorinfo.objects.get(aid=request.GET['aid']).delete()
        return redirect('/authorslist/')
    return HttpResponse('Noting for Delete!')
#多对多外键关系表修改数据
def editauthor(request):
    if request.method == 'POST':
        authorobject = models.authorinfo.objects.get(aid=request.POST['authornid'])
        authorobject.author_book_publish.set(request.POST.getlist('booksselect'))
        authorobject.save()
        return redirect('/authorslist/')
    authorselect = models.authorinfo.objects.get(aid=request.GET['aid'])
    bookslist = models.bookinfo.objects.all()
    return render(request,'editauthor.html',{'authorselect':authorselect,'bookslist':bookslist})