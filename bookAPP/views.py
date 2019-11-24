from django.shortcuts import render,HttpResponse,redirect
from bookAPP import models
# Create your views here.

def publisherlist(request):
    res = models.publishinfo.objects.all()
    return render(request,'publisherlist.html',{'publisherlist':res})

def addpublisher(request):
    if request.method == 'POST':
        models.publishinfo.objects.create(pname=request.POST['publishname'])
        return redirect('/publisherlist/')
    return render(request,'addpublisher.html')

def deletepublish(request):
    if request.GET:
        models.publishinfo.objects.filter(pid=request.GET['pid']).delete()
        return redirect('/publisherlist/')
    return HttpResponse('Nothing for delete!')

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

def bookslist(request):
    booslist = models.bookinfo.objects.all()
    return render(request,'bookslist.html',{'booklist':booslist})

def addbook(request):
    if request.method == 'POST':
        print(request.POST['publisherselect'])
        models.bookinfo.objects.create(bname=request.POST['bookname'],book_pubish_id=request.POST['publisherselect'])
        return redirect('/bookslist/')
    publisherlist = models.publishinfo.objects.all()
    return render(request,'addbook.html',{'publisherlist':publisherlist})

def deletebook(request):
    if request.GET:
        models.bookinfo.objects.filter(bid=request.GET['bid']).delete()
        return redirect('/bookslist/')
    return HttpResponse('Nothing for delete!')

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

def authorslist(request):
    authorlist = models.authorinfo.objects.all()
    return render(request,'authorslist.html',{'authorlist':authorlist})

def addauthor(request):
    if request.method == 'POST':
        allbooks = request.POST.getlist('booksselect')
        print(allbooks)
        authorobject = models.authorinfo.objects.create(aname=request.POST['authorname'])
        authorobject.author_book_publish.set(allbooks)
        return  redirect('/authorslist/')
    allbooks = models.bookinfo.objects.all()
    return render(request,'addauthor.html',{'bookslist':allbooks})

def deleteauthor(request):
    if request.GET:
        models.authorinfo.objects.get(aid=request.GET['aid']).delete()
        return redirect('/authorslist/')
    return HttpResponse('Noting for Delete!')