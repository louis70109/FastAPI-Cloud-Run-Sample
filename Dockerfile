FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# 將專案複製到容器中
COPY . /app

# 安裝必要的套件
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# 開放指定的埠號，讓容器外的系統能夠訪問應用程式
EXPOSE 8080

# 啟動 FastAPI 應用程式
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
