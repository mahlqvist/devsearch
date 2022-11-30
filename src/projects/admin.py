from django.contrib import admin

# Register your models here.
from .models import Tag, Project, Review

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Review)