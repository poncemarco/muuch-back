FROM python:3.10-slim


# Instala dependencias del sistema necesarias para GDAL
RUN apt-get update && \
    apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt requirements.txt

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente del proyecto
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación en modo desarrollo
CMD ["sh", "-c", "python manage.py migrate && gunicorn myapp.wsgi:application --bind 0.0.0.0:8000"]

