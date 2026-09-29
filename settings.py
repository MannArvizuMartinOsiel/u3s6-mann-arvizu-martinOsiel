# pymysql: el conector que instalaste en el paso 02
import pymysql
# Hace que Django use pymysql como si fuera el driver oficial de MySQL para Python
pymysql.install_as_MySQLdb()

# config: función de python-decouple que lee valores del archivo .env
from decouple import config

# (más abajo en el archivo, reemplazá el DATABASES que trae Django por defecto)
DATABASES = {
    'default': {
        # ENGINE: qué motor de base de datos usar — mysql en vez del sqlite3 por defecto
        'ENGINE': 'django.db.backends.mysql',
        # NAME: nombre de la base de datos, leído de la variable DB_NAME del .env
        'NAME': config('DB_NAME'),
        # USER: usuario de conexión, leído de DB_USER
        'USER': config('DB_USER'),
        # PASSWORD: contraseña de conexión, leída de DB_PASSWORD
        'PASSWORD': config('DB_PASSWORD'),
        # HOST: servidor donde vive la base de datos, leído de DB_HOST
        'HOST': config('DB_HOST'),
        # PORT: puerto de conexión; default='3306' se usa solo si DB_PORT no está en el .env
        'PORT': config('DB_PORT', default='3306'),
        # OPTIONS: Aiven exige que la conexión venga cifrada (SSL)
        'OPTIONS': {'ssl': {'ssl-mode': 'REQUIRED'}},
    # cierre del diccionario de configuración de la conexión
    }
# cierre del diccionario DATABASES
}
INSTALLED_APPS = [
    # apps que Django trae instaladas por defecto (admin, auth, sessions, etc.)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'core': tu app nueva, agregada al final de la lista
    'core',
]