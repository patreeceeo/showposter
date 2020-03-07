from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import ui, api
from django.contrib.auth import views as auth_views

rest_router = DefaultRouter(trailing_slash=False)
rest_router.register('uploaded_image', api.UploadedImageView)
rest_router.register('unused_uploaded_image', api.UnusedUploadedImageView)

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('', ui.ListView.as_view(), name='list-view'),
    path('s/<slug>', ui.DetailView.as_view(), name='detail-view'),
    path('create-post', ui.CreatePostView.as_view(), name='create-post'),

    path('gallery', ui.GalleryView.as_view(), name='gallery-view'),

    path('api/', include(rest_router.urls)),
    path('api/bulk_uploaded_image', api.bulk_delete_uploaded_image),
]

