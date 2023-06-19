from django.urls import path
from articles_app import views

urlpatterns = [
    path('public-articles/', views.public_articles, name='public_articles'),
    path('authenticate/', views.user_authentication, name='user_authentication'),
    path('register/', views.user_registration, name='user_registration'),
    path('closed-articles/', views.closed_articles, name='closed_articles'),
    path('create-article/', views.create_article, name='create_article'),
    path('article/<int:article_id>/', views.update_or_delete_article, name='update_or_delete_article'),
]
