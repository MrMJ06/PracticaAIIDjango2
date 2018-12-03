from django.contrib import admin
from main.models import *
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Rating)
admin.site.register(User)