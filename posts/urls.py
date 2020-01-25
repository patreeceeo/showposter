from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import ui, api

rest_router = DefaultRouter(trailing_slash=False)
rest_router.register('upload', api.UploadedImageRESTView)

urlpatterns = [
    path('', ui.ListView.as_view(), name='list-view'),
    path('s/<slug>', ui.DetailView.as_view(), name='detail-view'),
    path('upload', ui.UploadView.as_view(), name='upload-view'),
    path('post', ui.CreatePostView.as_view(), name='add-view'),

    path('gallery', ui.GalleryView.as_view(), name='gallery-view'),

    path('api/', include(rest_router.urls))
]

