from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Comments)
admin.site.register(Replay)