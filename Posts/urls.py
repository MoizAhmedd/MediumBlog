from django.urls import path
from . import views

urlpatterns = [
    path('',views.ArticleListView.as_view(),name ='home'),
    path('article/<int:pk>',views.ArticleDetailView.as_view(),name ='article_page'),
    path('article/new', views.NewPostView.as_view(), name = 'new_article'),
    path('article/<int:pk>/edit',views.EditPostView.as_view(),name = 'edit_article'),
    path('article/<int:pk>/delete',views.DeletePostView.as_view(),name = 'delete_article'),

]
