"""booksystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from houseAPP import urls as house_urls
from carAPP import urls as car_urls
from app02 import views as appveiws
from bookAPP import views
from bookAPP.views import \
    publisherlist,\
    addpublisher,\
    deletepublish,\
    editpublisher,\
    bookslist,\
    addbook,\
    deletebook,\
    editbook,\
    authorslist,\
    addauthor,\
    deleteauthor,\
    editauthor,\
    test,\
    uploadfile,\
    testurl,\
    ceshiurl,\
    moreurl,\
    getnumurl,\
    trytest,\
    testargs


urlpatterns = [
    path('admin/', admin.site.urls),
    #url('publisherlist',publisherlist),
    # path('publisherlist/',publisherlist), #在Django2.0以后Url被替换为path，但是url依然可以用
    url(r'^publisherlist/$',publisherlist),
    #url('addpublisher',addpublisher),
    url('addpublisher',views.Add_publisher.as_view()), #另外一种调用View函数的方法，等同于上面的方法
    url(r'^deletepublish/([0-9]+)/$',deletepublish),
    url('editpublisher',editpublisher),
    #url('bookslist',bookslist),


    url(r'^bookslist',views.bookslist), #r表示正则表达式，^表示以booklist开头，
    url('addbook',addbook),
    url(r'^deletebook/([0-9]+)/$',deletebook),
    url('editbook',editbook),


    url('authorslist',authorslist),
    url('addauthor',addauthor),
    url('deleteauthor',deleteauthor),
    url('editauthor',editauthor),

    #路由器反向链接实例
    url('trytest', trytest,name='tryreverse'),  # 定义一个链接，用于测试URL利用视图反向链接的操作
    url('test',test,name='gotest'),  #给路径命名一个别名，在浏览器调用别名即可获得当前的路径 HTML 调用方法href={% url 别名 %}
    url(r'^gogogo/(?P<number>[0-9]{2,4})/$',testargs,name='go'), #用于演示URL反向链接，在视图中传参数的用法 传参数必须要用到reverse反向

    #路由器上传文件
    url(r'^uploadfile/$',uploadfile), # $判断正则表达式是否完全匹配，如果不加$的话，http://127.0.0.1:8001/bookslist/a/d/a/ 也可以正常访问bookslist页面

    #路由器正则表达式分组传参
    url('cocoturl',testurl),
    url(r'^ceshiurl/[0-9]{2,4}/$',ceshiurl),# 地址栏传入正则表达式的内容，开头为ceshiurl/ 拼接一个0-9的2-4位数的地址，$并且检查匹配
    url(r'^moreurl/([0-9]{2,4})/([a-zA-Z]{3})/$',moreurl), #()可以用来分组，所以现在拆分为2组，每组代表一个参数，前面是0-9的2-4位数，后面是3位由字母组成的字符串，后台的方法可以接受穿过来的两组参数
    url(r'^getnumurl/([0-9]+)/$',getnumurl), # +代表，由0-9组成的数字，不限位数，如果不写+号，只能是0-9之间的一位数，并且只有加括号，作为分组，参数才能被view函数接收

    #路由器反向链接
    url('house/',include((house_urls,'house'),namespace='house')),
    url('car/',include((car_urls,'car'),namespace='car')),
    url(r'^$',publisherlist), #什么都不写，当浏览器访问http://127.0.0.1:8002/  项目初始路径的时候直接返回指定函数

    #路由器参数反射函数，类和变量
    url(r'^delete/([a-zA-Z]+)/(\d+)/$',views.delete),
    url(r'^faq/$',appveiws.faq),

    url(r'^signin/$',views.signin,name='sign'),
    url(r'^logout/$',views.logout,name='logout'),



]
