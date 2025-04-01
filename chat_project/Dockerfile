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

# 启动时收集静态文件并运行 Daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "chat_project.asgi:application"]
