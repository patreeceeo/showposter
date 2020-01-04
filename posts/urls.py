from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='list-view'),
    path('s/<slug>/', views.DetailView.as_view(), name='detail-view'),
    path('post/', views.CreatePostView.as_view(), name='add-view')
]
