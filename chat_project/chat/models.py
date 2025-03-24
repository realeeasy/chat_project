from django.db import models
from django.contrib.auth.models import User

# 房间模型
class Room(models.Model):
    name = models.CharField(max_length=30, unique=True)  # 房间名
    description = models.TextField(blank=True, null=True)  # 房间描述
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    members = models.ManyToManyField(User, related_name='rooms', blank=True)  # 房间成员


    def __str__(self):
        return self.name


# Create your models here.
