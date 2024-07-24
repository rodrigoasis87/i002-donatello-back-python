# Etapa 1: Construcción de la aplicación
FROM python:3.10-slim AS builder
WORKDIR /app

# Envs
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update

# Copia y establece las dependencias del proyecto
RUN pip install --upgrade pip
COPY /requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Configuración de la aplicación
FROM builder AS setup
WORKDIR /app
COPY . .

# Etapa 3: Servidor de producción
FROM python:3.10-slim AS production
WORKDIR /app

# Copia los archivos del build anterior
COPY --from=setup /app /app

# Configura variables de entorno
# ENV DJANGO_SETTINGS_MODULE=nombre_de_tu_app.settings.prod
ENV PYTHONPATH /usr/local/bin/django-admin

# Configura la ejecución de la aplicación
CMD ["python3", "manage.py", "runserver"]
