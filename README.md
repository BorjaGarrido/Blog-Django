# Blosiuto
Blousiuto de perpiñón

1) Para crear el proyecto:  
    django-admin startproject "Proyecto"
 
2) Justo al iniciar el proyecto:
    python manage.py migrate
 
2.1) Para realizar la migraciones al hacer cambios en los modelos:
    ->Dentro de la carpeta del proyecto "Proyecto":
        python manage.py makemigrations
        python manage.py migrate
 
3) Para crear la aplicacion:
    ->Dentro de la carpeta del proyecto "Proyecto":
        python manage.py startapp "App"
    
4) Añadir "App" dentro del archivo Proyecto/settings.py en INSTALLED_APPS:
     INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'App',
    )

5) Los modelos nuevos se añaden el "App/models.py"

5) Creación de administrador:
    ->Dentro de la carpeta "App/admin.py":

        from django.contrib import admin
        from .models import NuevoModelo

        admin.site.register(NuevoModelo)
    
    ->Se añade el modelo definido anteriormente para hacerlo visible en la página del adminstrador
    
    ->Dentro de la carpeta del proyecto "Proyecto":
        python manage.py createsuperuser
        Username: admin
        Email address: admin@admin.com
        Password:
        Password (again):
        
    ->Debe mostrar:
        Superuser created successfully.
        


    
