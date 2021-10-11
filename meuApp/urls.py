from django.conf.urls import url
from . import views

#url da requisição
urlpatterns = [
    url(r'^cdb/$', views.CDB.as_view(), name='CDB-pós-fixado'),

]