from django.contrib import admin

# Register your models here.
from dashboard.models import Page, Party, Post, Like, Comment, Reply

admin.site.register(Page)
admin.site.register(Party)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Reply)