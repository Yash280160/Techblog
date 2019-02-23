from django.urls import path
from . import views

urlpatterns = [

path('register/', views.register, name = 'register'),
path('login/', views.login, name = 'login'),
path('logout/', views.logout, name = 'logout'),
path('post/', views.questions_list, name = 'ques'),
path('post_new/', views.post, name = 'post'),

]