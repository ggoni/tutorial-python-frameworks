from django.contrib import admin
from .models import Post


# Create a new class por posts in Admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')


# Register your models here.
admin.site.register(Post, PostAdmin)
