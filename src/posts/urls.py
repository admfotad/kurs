from django.conf.urls import url
from django.contrib import admin
#from posts import views as post_view
from .views import (post_create,
                    post_detail,
                    post_list,
                    post_update,
                    post_delete,
                    )

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),

]