from django.contrib import admin
from .models import Discussion, Forum


admin.site.register(Forum)
admin.site.register(Discussion)
