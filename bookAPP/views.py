from django.shortcuts import render, HttpResponse, redirect
from bookAPP import models
from django.urls import reverse
from functools import wraps




# Create your views here.
# 测试页面调用的方法
def test(request):
    return render(request, 'test.html')


# 定义一个方法用于测试URL通过视图反向链接的用法
def trytest(request):
    if request.method == 'POST':
        url_back = reverse('go', kwargs={'number': request.POST['get_num']})  # 向别名为go的链接以字典的方式传入参数 reverse是反向的意思
        print(url_back)
        return redirect(url_back)
    return render(request, 'trytest.html')


# 用于演示URL反向链接在视图中传参数的用法
def testargs(request, number):
    print(number)
    return HttpResponse('url反向链接视图传参数成功')


# def check_login(func):
#     def inner(func):
#         pass



#检查用户登录装饰器 cookies版
#装饰器可以认为是，修饰函数或者类的方法，如果条件成立就运行函数
# def check_login(func):
#     @wraps(func) # 其实也是一个装饰器，因为写装饰器的时候方法名，注释，和属性其实都被改变了，为了不改变，需要在前面加上一个Wraps的装饰器，这样就可以不改变原函数
#     def inner(*args, **kwargs):
#         print('005，进入装饰器innner')
#         rs = args[0].get_signed_cookie('islogin', default='0', salt='66666666')
#         if rs == '1':
#             print('006,判断Cookies正确')
#             return func(*args, **kwargs)
#         else:
#             print('007,判断Cookies不正确')
#             return redirect('/signin/?next={}'.format(args[0].path_info))
#     return inner
#Session 检查用户登录版装饰器
def check_login(func):
    @wraps(func) # 其实也是一个装饰器，因为写装饰器的时候方法名，注释，和属性其实都被改变了，为了不改变，需要在前面加上一个Wraps的装饰器，这样就可以不改变原函数
    def inner(*args, **kwargs):
        print('005，进入装饰器innner')
        rs = args[0].session.get('islogin')
        if rs == '1':
            print('006,判断Cookies正确,用户名为：{}'.format(args[0].session.get('name'))) #取Session中存入的name值
            return func(*args, **kwargs)
        else:
            print('007,判断Cookies不正确')
            return redirect('/signin/?next={}'.format(args[0].path_info))
    return inner

# signin用户登录 Cookies 版本
# def signin(request):                                             #http://127.0.0.1:8002/signin/?next=/authorslist/
#     print('get_full_path:',request.get_full_path())              #/signin/?next=/authorslist/
#     print('get_full_path_info:',request.get_full_path_info())    #/signin/?next=/authorslist/
#     print('path_info:',request.path_info)                        #/authorslist/
#     print('009,进入signin方法')
#     next_url = request.GET.get('next')
#     print('008，获取到的URL值为：', next_url)
#     if request.method == 'GET':
#         if next_url != '':
#             next_url = '/publisherlist/'
#         if request.get_signed_cookie('islogin', default='0', salt='66666666') == '1':
#             print('003，登录的Cookies存在')
#             return redirect(next_url)
#         else:
#             print('010，Cookies不存在')
#             return render(request, 'signin.html')
#     if request.method == 'POST':
#         print(request.POST.get('uname'), request.POST.get('upassword'))
#         if request.POST.get('uname') == 'kevin' and request.POST.get('upassword') == '888':
#             print('001,用户名密码正确')
#             red = redirect(next_url)
#             red.set_signed_cookie('islogin', '1', salt='66666666', max_age=10)
#             return red
#             print('002，返回到上次访问的页面')
#         else:
#             return render(request, 'signin.html')

# signin用户登录 Session 版本
from django.views.decorators.csrf import csrf_exempt, csrf_protect
@csrf_exempt  #  如果想让那个表单不被伪安全验证，则可以用 csrf_exempt 装饰器，但必须导入上述包
def signin(request):
    request.session.get('islogin')
    next_url = request.GET.get('next')
    if next_url == None:
        next_url = '/publisherlist/'
    print('008，获取到的URL值为：', next_url)
    if request.method == 'GET':
        if request.session.get('islogin') == '1': # 获取Session 值
            print('003，登录的Cookies存在')
            return redirect(next_url)
        else:
            print('010，Cookies不存在')
            return render(request, 'signin.html')
    if request.method == 'POST':
        print(request.POST.get('uname'), request.POST.get('upassword'))
        if request.POST.get('uname') == 'kevin' and request.POST.get('upassword') == '888':
            print('001,用户名密码正确')
            request.session['islogin'] = '1'  #设置Session值
            request.session['name'] = request.POST.get('uname') #创建一个键值对关系的数据，存入给Session
            request.session.set_expiry(10)  #设置Session 失效时间
            # # 设置会话Session和Cookie的超时时间
            # request.session.set_expiry(value)
            # *如果value是个整数，session会在些秒数后失效。
            # *如果value是个datatime或timedelta，session就会在这个时间后失效。
            # *如果value是0, 用户关闭浏览器session就会失效。
            # *如果value是None, session会依赖全局session失效策略。
            return redirect(next_url)
        else:
            return render(request, 'signin.html')

# Cookies 版本 logout
# def logout(request):
#     rs = redirect('/signin/')
#     rs.delete_cookie('islogin')
#     print('011,Cookies 值已被清楚')
#     return rs
# Session 版本 logout
def logout(request):
    print('011-1,Session 清楚中')
    # request.session.delete()  #   只删除Session 数据，不删除Cookies
    request.session.flush()  #清楚Session值    删除Session数据和Cookies值
    print('011,Session值已被清楚')
    return redirect('/signin/')

# 单表操作读取数据
@check_login
def publisherlist(request):
    from utils.pagination import Pagination  # 导入自定义的工具包
    PaginationObj = Pagination(models.publishinfo.objects.all().count(), request.GET.get('page', 1), 10, 15)  # 实例化工具包的对象
    alldata = models.publishinfo.objects.all()[PaginationObj.startnum:PaginationObj.endnum]
    return render(request, 'publisherlist.html',
                  {
                      'publisherlist': alldata,
                      'pagerange': PaginationObj.pagerange,
                      'lastpage': PaginationObj.lastpage,
                      'currentpage': PaginationObj.pagecurrent,
                      'previouspage': PaginationObj.previous,
                      'previousswitch': PaginationObj.previous_switch,
                      'nextpage': PaginationObj.next,
                      'nextpageswitch': PaginationObj.next_switch
                  })


# 单表操作添加数据 # 用方法直接执行浏览器的返回操作，叫做FBV = function build view


def addpublisher(request):
    if request.method == 'POST':
        models.publishinfo.objects.create(pname=request.POST['publishname'])
        return redirect('/publisherlist/')
    return render(request, 'addpublisher.html')


# 单表操作添加数据 # 用类直接执行浏览器的返回操作，叫做CBV = Class build view
# 用类执行浏览器的返回操作必须要导入，view包,
from django.views import View
#在CBV中用装饰器的方法
from django.utils.decorators import method_decorator  # Django中把类中的函数，直接变成方法装饰器
# @method_decorator(check_login,name='get')  # 如果把装饰器写到类上面，必须要给Name属性
class Add_publisher(View):
    @method_decorator(check_login)  # 调用类转换后的装饰器方法 @method_decorator是固定写法，括号内容为装饰器名
    def get(self, request):
        return render(request, 'addpublisher.html')

    def post(self, request):
        models.publishinfo.objects.create(pname=request.POST['publishname'])
        return redirect('/publisherlist/')


# 单表操作删除数据,用路由器原理接收要删除的参数ID，参看url配置和前端代码，此处不可以用 if request.method来判断。
def deletepublish(request, del_id):
    print(del_id)
    models.publishinfo.objects.filter(pid=del_id).delete()
    return redirect('/publisherlist/')


# 单表操作修改数据
def editpublisher(request):
    if request.method == 'POST':
        publishobject = models.publishinfo.objects.get(pid=request.POST['editpublishid'])
        publishobject.pname = request.POST['editpublishname']
        publishobject.save()
        return redirect('/publisherlist/')
    if request.GET:
        res = models.publishinfo.objects.get(pid=request.GET['pid'])
        return render(request, 'editpublisher.html', {'editpublisher': res})
    return HttpResponse('Nothiing for edit!')


# 一对多外键关系表查询数据
def bookslist(request):
    booslist = models.bookinfo.objects.all()
    return render(request, 'bookslist.html', {'booklist': booslist})


# 一对多外键关系表添加数据
def addbook(request):
    if request.method == 'POST':
        print(request.POST['publisherselect'])
        models.bookinfo.objects.create(bname=request.POST['bookname'], book_pubish_id=request.POST['publisherselect'])
        return redirect('/bookslist/')
    publisherlist = models.publishinfo.objects.all()
    return render(request, 'addbook.html', {'publisherlist': publisherlist})


# 一对多外键关系表删除数据
def deletebook(request, del_id):
    models.bookinfo.objects.filter(bid=del_id).delete()
    return redirect('/bookslist/')


# 一对多外键关系表修改数据
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
        return render(request, 'editbook.html', {'bookselect': bookselect, 'publishlist': publishlist})
    return HttpResponse('Nothing for edit!')


# 多对多外键关系表查询数据
@check_login
def authorslist(request):
    authorlist = models.authorinfo.objects.all()
    return render(request, 'authorslist.html', {'authorlist': authorlist})


# 多对多外键关系表查添加数据
def addauthor(request):
    if request.method == 'POST':
        allbooks = request.POST.getlist('booksselect')
        print(allbooks)
        authorobject = models.authorinfo.objects.create(aname=request.POST['authorname'])
        authorobject.author_book_publish.set(allbooks)
        return redirect('/authorslist/')
    allbooks = models.bookinfo.objects.all()
    return render(request, 'addauthor.html', {'bookslist': allbooks})


# 多对多外键关系表删除数据
def deleteauthor(request):
    if request.GET:
        models.authorinfo.objects.get(aid=request.GET['aid']).delete()
        return redirect('/authorslist/')
    return HttpResponse('Noting for Delete!')


# 多对多外键关系表修改数据
def editauthor(request):
    if request.method == 'POST':
        authorobject = models.authorinfo.objects.get(aid=request.POST['authornid'])
        authorobject.author_book_publish.set(request.POST.getlist('booksselect'))
        authorobject.save()
        return redirect('/authorslist/')
    authorselect = models.authorinfo.objects.get(aid=request.GET['aid'])
    bookslist = models.bookinfo.objects.all()
    return render(request, 'editauthor.html', {'authorselect': authorselect, 'bookslist': bookslist})


# Form表单上传文件方法
def uploadfile(request):
    success = ''
    if request.method == 'POST':
        filename = request.FILES['uploadfile'].name  # 另外一种写法 request.FILES.get('uploadfile').name
        print(filename)
        with open(filename, 'wb') as file:
            for i in request.FILES['uploadfile'].chunks():
                print(i)
                file.write(i)
        success = 'upload successful'
    return render(request, 'uploadfile.html', {'showmessage': success})


# 测试路由器Url属性方法
def testurl(request):
    return HttpResponse('testurl')


def ceshiurl(request):
    return HttpResponse('ceshiurl')


def moreurl(request, arg1, arg2):  # 接受从URL路由器传过来的2组参数，只有前面的参数有（）代表以及分组的形式，参数才能被方法获取到
    print(arg1, '---', arg2)
    return HttpResponse('moreurl')


def getnumurl(request, arg1):
    print(arg1)
    return HttpResponse('getnumurl')


# 利用路由器地址解析，发射功能删除指定数据表的内容
def delete(request, table_name, delete_id):  # 接受浏览器url传过来的符合正则表达式参数 url(r'^delete/([a-zA-Z]+)/(\d+)/$',views.delete)
    print('程序运行到了delete')
    print(table_name, '-----', delete_id)
    # 利用字符串反射类，函数，变量的方法，一共两部，第一步判断if hasattr(models,table_name): ，第二步获取deletetable = getattr(models,table_name)
    if hasattr(models, table_name):  # 判断表名是否在models类中，
        print('表存在于Models中')
        print(getattr(models, table_name))  # getattr(models,table_name 返回的值为<class 'bookAPP.models.publishinfo'>
        deletetable = getattr(models, table_name)  # 讲得到的路径返回给一个变量deletetable
        # deletetable.objects.filter(pid=delete_id).delete()
        try:
            deletetable.objects.get(pid=delete_id).delete()  # 删除自定表里ID为delete_id的数据，这里Try 用来判断传入的id是否存在，这里是打点不出来的。
            return HttpResponse('数据删除成功')
        except Exception as e:
            print(e)
            return HttpResponse('没有该ID的值')
    else:
        return HttpResponse('没有要删除的表')
    return HttpResponse('table_name is {},delete_id is {}'.format(table_name, delete_id))

