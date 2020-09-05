from django.contrib import admin

# Register your models here.
from facebook.models import Atricle
from facebook.models import Page
from facebook.models import Comment
admin.site.register(Atricle)
admin.site.register(Page)
admin.site.register(Comment)