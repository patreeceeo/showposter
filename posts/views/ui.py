from django.views import generic
from django.urls import reverse_lazy
from posts.models import Post
from posts.forms import PostForm

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

