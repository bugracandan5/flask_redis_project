# Kullanılacak temel imaj
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Uygulama kodlarını kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["python", "app.py"]
