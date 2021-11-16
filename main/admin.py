from django.contrib import admin
from .models import ToDo, ToMeet

# Register your models here.
admin.site.register(ToDo)
admin.site.register(ToMeet)

