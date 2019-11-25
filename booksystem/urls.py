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
    path('publisherlist/',publisherlist), #在Django2.0以后Url被替换为path，但是url依然可以用
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
    url('trytest', trytest),  # 定义一个链接，用于测试URL利用视图反向链接的操作
    url('test',test,name='gotest'),  #给路径命名一个别名，在浏览器调用别名即可获得当前的路径 HTML 调用方法href={% url 别名 %}
    url(r'^gogogo/(?P<number>[0-9]{2,4})/$',testargs,name='go'), #用于演示URL反向链接，在视图中传参数的用法
    url(r'^uploadfile/$',uploadfile), # $判断正则表达式是否完全匹配，如果不加$的话，http://127.0.0.1:8001/bookslist/a/d/a/ 也可以正常访问bookslist页面
    url('cocoturl',testurl),
    url(r'^ceshiurl/[0-9]{2,4}/$',ceshiurl),# 地址栏传入正则表达式的内容，开头为ceshiurl/ 拼接一个0-9的2-4位数的地址，$并且检查匹配
    url(r'^moreurl/([0-9]{2,4})/([a-zA-Z]{3})/$',moreurl), #()可以用来分组，所以现在拆分为2组，每组代表一个参数，前面是0-9的2-4位数，后面是3位由字母组成的字符串，后台的方法可以接受穿过来的两组参数
    url(r'^getnumurl/([0-9]+)/$',getnumurl), # +代表，由0-9组成的数字，不限位数，如果不写+号，只能是0-9之间的一位数，并且只有加括号，作为分组，参数才能被view函数接收

    url('house/',include(house_urls)),
    url('car/',include(car_urls))
]

########################################################################
#Python 中多添加一个APP项目的方法，
########################################################################
#方法一，在Pycharm软件中的Terminal中，输入 python3 manage.py startapp carAPP  #carAPP为APP项目名，
#方法二，或者在Pycharm软件中的Tools中选择Run manage.py task 然后在命令中输入 startapp houseAPP，#houseAPP为APP项目名

########################################################################
#Django项目中，include 包含其他APP项目中的url方法
########################################################################
#第一步，在主项目中的setting.py 中找到 INSTALLED_APPS 然后添加如下代码，'carAPP.apps.CarappConfig', # 可以点出来，注意，首字母一定要大写 carAPP为新建的项目
#第二步，在carAPP项目目录中新建一个PY文件，命名为urls.py
#第三步，在主项目中urls 页面中，导入，include包 和APP的urls包
#from django.conf.urls import url,include，
#from carAPP import urls as car_urls # 导入carAPP下的urls.py文件，并且给他重新命名为car_urls (避免和主目录的命名冲突)
#第四步，在主目录的urlpatterns列表中，添加要指向的子项目carAPP的url
#url('car', include(car_urls)) #用于表示所有访问目录结构为/car/的请求全部调用car_urls目录导航
# 第五步，然后在carAPP中的url中输入如下代码：
# from django.conf.urls import url #导入 url 方法，切记，from django.conf import urls 是错误的，会返回未定义错误
# from carAPP import views #导入views的视图方法
# urlpatterns = [
#     url('carindex',views.carindex)   #执行浏览器返回的请求
# ]
# 第六步，编辑carAPP目录下的views方法，用于处理浏览器的请求
# from django.shortcuts import render,HttpResponse,redirect
# def carindex(request):
#     return HttpResponse('This is carapp page')

########################################################################
#Django项目中，Url反向解析
########################################################################
# 第一种方式
# 在要解析的URLs.py文件夹下面给 路径命名别名
# urlpatterns = [
#     url('car',views.car,name='gocar') # gocar为命名的别名，可任意命名
# ]
# 然后在HTML前段调用命名的别名
# <a href="{% url 'gocar' %}"> go to car page</a>    #{% url 'gocar' %} 是调用别名的固定写法
# 第二种方式
#说先需要确定URL中有被别名的路径
# url('test', test, name='gotest'),
# 然后在另外一个视图中操作调用test页面这里，以trytest为例 url('trytest',trytest), #定义一个链接，用于测试URL利用视图反向链接的操作
# 在Views的视图中找到trytest方法，里面编辑要跳转的test页面，编辑前需要导入reserve包
# from django.urls import reverse
# def trytest(request):
#     return redirect(reverse('gotest'))
########################################################################
#Django项目中，Url反向解析,传参数
########################################################################
# 第一步，确定好URL参数代码的拼写
# url(r'^gogogo/(?P<number>[0-9]{2,4})/$', testargs, name='go'),  # 用于演示URL反向链接，在视图中传参数的用法 ,传参数的固定写法必须有 ?P,有几个参数写几个?P
# 第二步，编辑一个调用上面URL的view函数
# #定义一个方法用于测试URL通过视图反向链接的用法
# def trytest(request):
#         # return redirect(reverse('gotest'))
#     url_back = reverse('go',kwargs={'number':88})
#     print(url_back)
#     return redirect(url_back)
# 为了方便测试，可以为有参数的URL顶一个view方法，因为有参数所以必须要接受传来的参数
# def testargs(request,number):
#     print(number)
#     return HttpResponse('url反向链接视图传参数成功')
# 第三步，在HTML中的调用方法
# <a href="{% url 'go' 88 %}">测试go88HTML 调用</a>