from django.conf.urls import url
from carAPP import views
urlpatterns = [
    url('car',views.car,name='gocar')
]