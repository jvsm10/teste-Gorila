from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cdb/$', views.CDBList.as_view(), name='cdb-list'),

]