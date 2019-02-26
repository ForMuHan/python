from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^addhandle/$', views.addhandle),
    url(r'^modify/$', views.modify),
    url(r'^delete/$', views.delete),
    url(r'^deletehandle/$', views.deletehandle),
    url(r'^check$', views.check)
]
