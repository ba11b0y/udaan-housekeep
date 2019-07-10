from django.contrib import admin
from .models import Task, Asset, Worker

# Register your models here.
admin.site.register(Task)
admin.site.register(Asset)
admin.site.register(Worker)
