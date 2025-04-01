from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# 房间模型
class Room(models.Model):
    name = models.CharField(max_length=30, unique=True)  # 房间名
    slug = models.SlugField(unique=True, null=True, blank=True)  # 新增 slug 字段
    description = models.TextField(blank=True, null=True)  # 房间描述
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    members = models.ManyToManyField(User, related_name='rooms', blank=True)  # 房间成员

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # 生成 slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
