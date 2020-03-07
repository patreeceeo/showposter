from django.db import models
from django.core.validators import validate_slug
from posts.utils import get_slug
from django.utils import timezone
from django.contrib.auth.models import User

def get_default_slug():
    slug = get_slug()
    while Post.objects.filter(slug=slug).count() == 1:
        slug = get_slug()
    return slug

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    date_created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.image.url

class Post(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    slug = models.CharField(max_length=24, unique=True, validators=[validate_slug], default=get_default_slug)
    date_of_show = models.DateField()
    alternate_text = models.TextField()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail-view', kwargs={'slug': self.slug})

