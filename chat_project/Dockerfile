# 使用官方推荐的轻量级镜像
FROM python:3.12-slim-bookworm

# 设置工作目录
WORKDIR /app

# 安装依赖，充分利用缓存
COPY requirements.txt /app/
# 使用清华镜像源
RUN pip install -r requirements.txt

# 复制项目代码
COPY . /app/

# 暴露端口（文档化作用）
EXPOSE 8000

# 启动时：
# 1. 运行数据库迁移
# 2. 收集静态文件
# 3. 创建超级用户（如果不存在）
# 4. 启动 Daphne
CMD ["sh", "-c", "python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    echo \"from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword') \
    if not User.objects.filter(username='admin').exists() else print('Superuser already exists')\" | python manage.py shell && \
    daphne -b 0.0.0.0 -p 8000 chat_project.asgi:application"]
