from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('slug', 'start_date', 'location_text')
    fieldsets = (
            (None, {
                'fields': ('slug',),
                'description': 'Short but unique name that can be used to link to this post. No special characters. Try not to change this, otherwise people who have links using the old slug will get a sad 404 page.',
            }),
            ('deets', {
                'fields': (
                    'start_date',
                    'location_text',
                    'ticket_price',
                    'copy_text'
                )
            })
    )

admin.site.register(Post, PostAdmin)
