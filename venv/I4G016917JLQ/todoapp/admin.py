from django.contrib import admin
from .models import * #* imports all the created Models in models.py
# Register your models here.
admin.site.register(Task)