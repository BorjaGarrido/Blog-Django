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

6) Creación de administrador:
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

7) Las URLs de cada aplicacion se añaden en el archivo urls.py de "Proyecto/Proyecto", mientras que dentro de cada aplicacion
se tendrá que crear un archivo urls.py que contendra las direcciones de la propia aplicacion. 

8) PASOS A SEGUIR PARA LA CREACION DE ELEMENTOS DE UNA APLICACION:
    1º. Se crean el modelo correspondiente (App/models.py, makemigrations, migrate)
    2º. Se diseñan las vistas que trabajaran con el modelo creado (App/views.py)
    3º. Se crearan las urls que enlazaran los elementos del modelo y la web (App/urls.py)
    4º. Añadir las direcciones oportunas en el html en concreto
    
9) Las plantillas html van en App/Template/App. Es necesario crear esa dirección, y en esta se guardarán los .html

10) Crear el forms.py en App/ y anñadir las formas necesarias:

    class DestinoForm(forms.ModelForm):
	class Meta:
		model = Destino
        	fields = '__all__'

->Las relaciones que se pueden dar en Django son:
        .Muchos a uno: Para definir este tipo de relación usamos ForeignKey(). Sirve para asociar un modelo a muchos modelos diferentes (1:n). Ejemplo: una marca de carros posee varios carros.
        .Muchos a muchos: Para definir este tipo de relación usamos ManyToManyField(). Sirve para asociar varios modelos a muchos modelos diferentes (n:n). Ejemplo: diferentes pizzas poseen diferentes toppings.


->Asignar autor a una variable
if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()                        
user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
