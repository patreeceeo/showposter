from django.contrib import admin

# Register your models here.
from .models import Post, UploadedImage

class PostAdmin(admin.ModelAdmin):
    list_display=('slug',)
    fieldsets = (
            (None, {
                'fields': ('slug',),
                'description': 'Short but unique name that can be used to link to this post. No special characters. Try not to change this, otherwise people who have links using the old slug will get a sad 404 page.',
            }),
            ('deets', {
                'fields': (
                    'date_of_show',
                    'alternate_text',
                )
            })
    )

class UploadedImageAdmin(admin.ModelAdmin):
    list_display=('image', 'date_created')

admin.site.register(Post, PostAdmin)
admin.site.register(UploadedImage, UploadedImageAdmin)
