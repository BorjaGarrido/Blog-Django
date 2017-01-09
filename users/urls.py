from django.conf.urls import include, url

from users import views

urlpatterns = [
                       # Users
                       url(r'^list$', views.userList, name='list'),
                       url(r'^new$', views.usersNew, name='new'),
                       url(r'^delete/(?P<user_id>\d+)$', views.userDelete, name='delete'),
                       url(r'^login$', views.userLogin, name='login'),
                       url(r'^logout$', views.userLogout, name='logout'),
]
