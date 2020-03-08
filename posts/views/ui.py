from django.views import generic
from django.urls import reverse_lazy
from posts.models import Post
from posts.forms import PostForm
from posts.models import UploadedImage
from django.contrib.auth.mixins import LoginRequiredMixin

class ListView(generic.ListView):
    model = Post
    template_name = 'list.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'

class GalleryView(generic.TemplateView):
    template_name  = 'gallery.html'

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('list-view')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        post.save()
        return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('list-view')
