# chat/admin.py
from django.contrib import admin
from .models import Room

admin.site.register(Room)  # 注册 Room 模型

# Register your models here.
