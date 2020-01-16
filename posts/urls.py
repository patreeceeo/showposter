from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

ajax_router = DefaultRouter()
ajax_router.register('', views.RelatedImageAJAXView)

urlpatterns = [
    path('', views.ListView.as_view(), name='list-view'),
    path('s/<slug>/', views.DetailView.as_view(), name='detail-view'),
    path('upload/', views.UploadView.as_view(), name='upload-view'),
    path('post/', views.CreatePostView.as_view(), name='add-view'),

    path('api/upload', include(ajax_router.urls))
]

