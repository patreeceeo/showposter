from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class ListView(generic.ListView):
    model = Post
    template_name = 'list.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'

class UploadView(generic.TemplateView):
    template_name  = 'upload.html'

class CreatePostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('list-view')

from rest_framework import serializers
from .models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = UploadedImage
    fields = ('id', 'image')

from rest_framework import viewsets
from .models import UploadedImage

class UploadedImageRESTView(viewsets.ModelViewSet):
  serializer_class = UploadedImageSerializer
  queryset = UploadedImage.objects.all()

