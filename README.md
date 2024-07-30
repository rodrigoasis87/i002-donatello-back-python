<div align='center'>
  <img height="200" width="200" src="https://github.com/igrowker/i002-donatello-front/blob/55511e83ecb4200b56d4154a9f93caa84b1b324a/src/assets/logo.png"> 
</div>

# Donatello: Soluciones SaaS para Pequeños Comercios de Comida
Es una app web que revoluciona la gestión para pequeños comercios de comida, haciendo accesible y eficiente lo que antes parecía inalcanzable. Pensada para la gestión integral de pequeños comercios gastronomicos. 

 ## 🚀 Objetivo
 Facilitar la gestión de pequeños comercios de comida mediante una plataforma SaaS accesible y asequible, impulsando el crecimiento y la eficiencia operativa.

 ## 💡 Problema
 Falta de gestión adecuada y recursos limitados para inversión en tecnología, resultando en ineficiencias y pérdidas económicas.

 ## 📊 Datos Clave:

- 59% de restaurantes fracasan en los primeros 3 años debido a mala gestión.
- 63% carecen de sistemas de gestión de inventario. 
- 72% no gestionan adecuadamente a sus usuarios/clientes.

 ## 🔧 Solución
 Donatello ofrece herramientas para automatizar tareas, informes detallados, y conexión con clientes, adaptándose a presupuestos ajustados.

 ## 🌐 Impacto
 Herramientas para optimizar operaciones, mejorar rentabilidad y competir digitalmente, apoyando el dinamismo económico local.

 ## 🍕 Por qué Donatello? 
Inspirado en el personaje de las Tortugas Ninja, simboliza innovación tecnológica aplicada al sector gastronómico.


## Arquitectura y diseño
### Frontend
- **Despliegue**:  https://dona-tello.netlify.app/
- **Repositorio**: https://github.com/igrowker/i002-donatello-front
- **Tecnologías**: Angular, Github Actions `PENDIENTEEEEE MODIFICAR`

### Backend Python (Finanzas)
- **Despliegue**:  https://dona-tello.netlify.app/ `PENDIENTEEEEE MODIFICAR`
- **Repositorio**: https://github.com/igrowker/i002-donatello-back-python
- **Tecnologías**: Python, Django, PostgreSQL, Github Actions, Render

### Backend Java (API principal)
- **Despliegue**:  https://i002-donatello-back-java-latest-z9hn.onrender.com/
- **Repositorio**: https://github.com/igrowker/i002-donatello-back-java
- **Tecnologías**: Java 17, Springboot 3, PostrgreSQL, Json Web Token, Swagger, Docker, Github Actions etcs. 
- **Endpoints**: `Swagger:` https://i002-donatello-back-java-latest-z9hn.onrender.com/api/docs barra algo mas... `Revisar!!`   

## Funcionalidades
- **Usuarios, Autenticación y autorización**: Usando spring security, JWT (Json Web Token). Gestión del perfil público.
- **Inventario**: Gestión de productos y stock.
- **Clientes**: Gestión de datos de clientes.
- **Proveedores**: Gestión de contactos de proveedores.
- **Promociones**: Creación y gestión de promociones.
- **Notificaciones**: Gestión de notificaciones y alertas. `Revisar!!` 
- **Menú**: Gestión de menús y sus elementos.
- **Finanzas**: A traves del backend Python, Gestión de transacciones financieras. Registro de ingresos y gastos. Generación de reportes financieros.

## Equipo
### Frontend
- `Abraham` https://www.linkedin.com/in/abraham-rubin-arg/
- `Brikman` https://www.linkedin.com/in/brikman-paul-morales-52a9a7245/
- `Damian` https://www.linkedin.com/in/damian-e-lambrecht/
- `Erik` https://www.linkedin.com/in/erik-argel/
- `Richard` https://www.linkedin.com/in/richard-alexander-diaz-cata%C3%B1o-a566421bb/

### Backend Python 
- `Delfina` https://www.linkedin.com/in/delfina-quinteros-b61370209/
- `Rodrigo` https://www.linkedin.com/in/rodrigo-asis/

### Backend Java
- `David` https://www.linkedin.com/in/david-costa-yafar/
- `Emanuel` https://www.linkedin.com/in/emamagallanes/
- `Jesus` https://www.linkedin.com/in/jvaletadoria1095/
- `Ursula` https://www.linkedin.com/in/ursula-martinez

### QA 
- `Marcelo` https://www.linkedin.com/in/marcelo-de-angelis-/
- `Nancy` https://www.linkedin.com/in/Nancy-Cabral-Ruiz-Diaz/

### DevOps
- `Adrián` https://www.linkedin.com/in/adriánramos/

## Para desplegar en local:
### Requisitos Previos

- [Python](https://www.python.org/downloads/) 3.10 o superior
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (opcional, pero recomendado)
- [pip](https://pip.pypa.io/en/stable/installation/) para la gestión de paquetes de Python

## Instalación

### 1. Clonate el repositorio

    git clone https://github.com/tu-usuario/tu-repositorio.git  

    cd tu-repositorio

### 2. Configurate el entorno virtual

    python3 -m venv venv`  
    source venv/bin/activate  # En Linux/macOS  
    # venv\Scripts\activate  # En Windows  

### 3. Instalar las dependencias

    pip install -r requirements.txt

### 4. Configurar la base de datos de Postgre

    CREATE DATABASE donatello_db;  
    CREATE USER donatello_user WITH PASSWORD 'password';  
    ALTER ROLE donatello_user SET client_encoding TO 'utf8';  
    ALTER ROLE donatello_user SET default_transaction_isolation TO 'read committed';  
    ALTER ROLE donatello_user SET timezone TO 'UTC';  
    GRANT ALL PRIVILEGES ON DATABASE donatello_db TO donatello_user;

### (no te olvides de configurar el archivo settings.py)

    DATABASES = {  
       'default': {  
            'ENGINE': 'django.db.backends.postgresql',  
            'NAME': 'donatello_db',  
            'USER': 'donatello_user',  
            'PASSWORD': 'password',  
            'HOST': 'localhost',  
            'PORT': '5432',  
        }  
    }  

### 5. Realiza las migraciones de la base de datos

    python manage.py makemigrations  
    python manage.py migrate  

### 6. Crea un superusuario

    python manage.py createsuperuser  

### 7. ¡Y a correr!

    python manage.py runserver



## Agradecimientos

**Queremos expresar nuestra más profunda gratitud al increíble equipo de igrowker. Todo el material, documentacion y el acompañamiento desde el dia 0, han sido fundamentales para lograr este proyecto. Gracias por creer en nosotros y por estar ahí, día tras día, con ganas y dedicación. ¡Gracias, totales!**

### 🚀 https://igrowker.com/
### 🚀 https://www.linkedin.com/company/igrowker/

![image](https://xlab.igrowker.com/ig_w%202.png)







