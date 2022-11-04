from django.contrib import admin
from .models import Artist,Songs, Lyrc
# Register your models here.

admin.site.register(Artist)
admin.site.register(Songs)
admin.site.register(Lyrc)