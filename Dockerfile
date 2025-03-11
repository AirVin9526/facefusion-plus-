FROM nvidia/cuda:12.2-base
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 7860
CMD ["python", "webui/app.py", "--share"]  # Sourcegraph可追踪启动命令
