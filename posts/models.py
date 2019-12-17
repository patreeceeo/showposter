from django.db import models
from django.core.validators import validate_slug

# Create your models here.
class Post(models.Model):
    slug  = models.CharField(max_length=20, unique=True, validators=[validate_slug])
    start_date = models.DateField()
    location_text = models.CharField(max_length=140)
    ticket_price = models.IntegerField()
    copy_text = models.TextField()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail-view', kwargs={'slug': self.slug})
