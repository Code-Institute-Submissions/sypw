from django.contrib import admin
from .models import Discussion, forum


admin.site.register(forum)
admin.site.register(Discussion)
