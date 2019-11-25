#from django.conf import urls #这样导入包是错误的，因为urls的实际操作方法没有被调用，
from django.conf.urls import url
from houseAPP import views
from houseAPP.views import house
urlpatterns = [
    url('house',house,name='gohouse')
]