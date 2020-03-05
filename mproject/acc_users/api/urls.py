from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'account_api'
#from index.api.views import SchoolCreateView, AddressCreateView, StudentCreateView, SubjectCreateView ,SchoolListView, AddressListView, StudentListView, SubjectListView


urlpatterns = [
path('usercreate/', views.UserCreate.as_view(), name='usercreate'),
path('rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
path('myuserlogin/', views.MyUserLogin.as_view(), name='myuserlogin'),
# path('detail/', views.DetailView.as_view(), name='detailview'),
]