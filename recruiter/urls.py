from django.conf.urls import include, url
from recruiter import views

urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^$',views.user_login,name='login'),
    url(r'^recruiter/logout/$',views.user_logout,name='logout'),
    url(r'^candidate_detail/(?P<user_id>[0-9])$',views.user_detail,name='candidate_detail'),
]

