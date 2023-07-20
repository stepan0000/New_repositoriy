from django.urls import path
from .views import index,top_sellers,advertisment_post,register,login,profile
urlpatterns = [
    path('',index,name= '/'),
    path('top-sellers',top_sellers,name= 'top'),
    path('advertisment-post',advertisment_post,name = 'advpost'),
    path('register',register,name = 'reg1'),
    path('login',login,name = 'login'),
    path('profile',profile,name='profile')
]