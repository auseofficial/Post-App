from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_body')
    list_per_page = 2  

    def post_title(self, obj):
        return obj.title
    post_title.short_description = 'Title'
    post_title.admin_order_field = None  

    def post_body(self, obj):
        return obj.body
    post_body.short_description = 'Body'
    post_body.admin_order_field = None
    
admin.site.register(Post, PostAdmin)
