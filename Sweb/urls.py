from django.urls import path
from . import views

urlpatterns = [
#住民のWebアプリに使用するURL
    path('home', views.home, name='home'),#一番最初にアクセスする画面
    path('add/', views.add, name='add'),
    path('pdf/', views.pdf, name='pdf'),
    #path('/start/', views.start_quiz, name='start_quiz'),
    path('test/', views.test_start, name='test_start'),
    path('next/<int:question_index>/', views.next_question, name='next_question'),
    path('create_test_instance/<int:question_index>/', views.create_test_instance, name='create_test_instance'),
    path('incorrect/', views.incorrect, name='incorrect'),
    path('complete/', views.quiz_complete, name='quiz_complete'),
    path('video', views.video, name='video'),
]
