from django.contrib import admin


from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'active')
    list_filter = ('active', 'title')
    search_fields = ['title']

