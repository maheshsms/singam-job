from django.conf.urls import url
from relative_app import views

app_name='relative_app'

urlpatterns=[
    url(r'^relative/$',views.Relative,name='Relative'),
    url(r'^other/$',views.other,name='other'),
]
