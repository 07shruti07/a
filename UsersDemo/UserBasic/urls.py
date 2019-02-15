from django.urls import path
from UserBasic import views

#  Template urls

app_name = 'basicapp'

urlpatterns=[
	path('register/',views.register,name='register'),
	path('userlogin/',views.userlogin,name='userlogin')
]