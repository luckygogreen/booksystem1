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
from django.conf.urls import url

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
    test

urlpatterns = [
    path('admin/', admin.site.urls),
    url('publisherlist',publisherlist),
    #url('addpublisher',addpublisher),
    url('addpublisher',views.Add_publisher.as_view()),
    url('deletepublish',deletepublish),
    url('editpublisher',editpublisher),
    url('bookslist',bookslist),
    url('addbook',addbook),
    url('deletebook',deletebook),
    url('editbook',editbook),
    url('authorslist',authorslist),
    url('addauthor',addauthor),
    url('deleteauthor',deleteauthor),
    url('editauthor',editauthor),
    url('test',test)
]
