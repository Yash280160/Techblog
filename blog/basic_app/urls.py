from django.urls import path
from . import views

urlpatterns = [

path('register/', views.register, name = 'register'),
path('login/', views.login, name = 'login'),
path('logout/', views.logout, name = 'logout'),
path('post/', views.questions_list, name = 'ques'),
path('post_new/', views.post, name = 'post'),
path('post_detail/<int:pk>/', views.post_detail, name=  'post_detail'),
path('post/<int:pk>/comment', views.add_comment_to_post , name = "add_comment_to_post"),
path('comment/<int:pk>/approve', views.comment_approve, name = 'comment_approve'),
path('comment/<int:pk>/remove', views.comment_remove, name = 'comment_remove'),
path('AKA/', views.askQuestion, name = 'askQuestion'),
path('Read|Answer/', views.showQuestions, name='Answer'),
path('Answer/<int:pk>/', views.detailed, name='detail'),
path('addAnswer/<int:pk>/',views.answer_form, name='answer'),



]