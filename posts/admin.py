from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('slug',)
    fieldsets = (
            (None, {
                'fields': ('slug',),
                'description': 'Short but unique name that can be used to link to this post. No special characters. Try not to change this, otherwise people who have links using the old slug will get a sad 404 page.',
            }),
            ('deets', {
                'fields': (
                    'end_date',
                    'alternate_text',
                    'full_size'
                )
            })
    )

admin.site.register(Post, PostAdmin)
