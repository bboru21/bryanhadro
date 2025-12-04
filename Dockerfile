FROM python:3.12-slim

WORKDIR /app

# Install OS-level dependences needed by Pillow 
RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libtiff5-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl-dev tk-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# collect static files
RUN python manage.py collectstatic --noinput --settings website.settings.local

ENV PYTHONUNBUFFERED=1

# Gunicorn will be used for both local and production
CMD ["gunicorn", "website.wsgi:application", "--bind", "0.0.0.0:9000"]