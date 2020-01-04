from django.db import models
from django.core.validators import validate_slug
from posts.utils import get_slug

def get_default_slug():
    slug = get_slug()
    while Post.objects.filter(slug=slug).count() == 1:
        slug = get_slug()
    return slug


# Create your models here.
class Post(models.Model):
    slug = models.CharField(max_length=24, unique=True, validators=[validate_slug], default=get_default_slug)
    end_date = models.DateField()
    alternate_text = models.TextField()
    full_size = models.ImageField(upload_to='images/',  default='images/grimpizza.jpg')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail-view', kwargs={'slug': self.slug})


