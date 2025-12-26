## 🚀 Despliegue en Producción (Live Demo)

El proyecto se encuentra desplegado en la nube utilizando **Render** como plataforma PaaS.

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **API Root** | [https://proyecto-visitas-nghf.onrender.com/api/visitas/](https://proyecto-visitas-nghf.onrender.com/api/visitas/) | Endpoint principal (JSON) |
| **Panel Admin** | [https://proyecto-visitas-nghf.onrender.com/admin/](https://proyecto-visitas-nghf.onrender.com/admin/) | Administración del sistema |
| **Cliente Web** | [https://cliente-visitas.onrender.com](https://cliente-visitas.onrender.com) | Dashboard (Frontend) |

---

## 📋 Integraciones y Características (Evaluación)

Este proyecto cumple con los requerimientos de la evaluación final mediante las siguientes implementaciones técnicas:

### 1. Arquitectura API REST (Integración A)
En lugar de una aplicación monolítica tradicional, el sistema expone sus datos vía **JSON**.
- **Serializadores:** Transformación de modelos complejos de Django a formatos nativos de Python/JSON.
- **ViewSets:** Lógica de negocio encapsulada para operaciones CRUD estandarizadas.

### 2. Calidad y Seguridad
- **CORS Configurado:** Implementación de `django-cors-headers` permitiendo el consumo seguro desde el cliente frontend (`cliente-visitas.onrender.com`).
- **Variables de Entorno:** Credenciales de base de datos y claves secretas gestionadas internamente por la plataforma Render, sin exposición en el código fuente.
- **Base de Datos Robusta:** Migración de SQLite (desarrollo) a **PostgreSQL** (producción) para integridad y escalabilidad de datos.

---

## 🛠 Stack Tecnológico

* **Lenguaje:** Python 3.12
* **Framework:** Django 5.x
* **API Toolkit:** Django REST Framework (DRF)
* **Base de Datos:** PostgreSQL (vía Render)
* **Servidor Web:** Gunicorn (WSGI)
* **Infraestructura:** Render (PaaS)

---

## ⚙️ Instalación y Ejecución Local

Si deseas levantar este backend en tu entorno local de desarrollo, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPO_GITHUB>
cd gestion_empresa

#2. Crear entorno virtual
Bash

# En Windows
python -m venv venv

venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate

#3. Instalar dependencias
Bash

pip install -r requirements.txt


#4. Configuración de Base de Datos
Por defecto, el proyecto local usará db.sqlite3. Aplica las migraciones:

Bash

python manage.py migrate

#5. Crear Superusuario (Admin)

Para acceder al panel /admin:

#Bash

python manage.py createsuperuser
#Ejecutar el servidor

#Bash

# python manage.py runserver
# La API estará disponible en # 

http://127.0.0.1:8000/api/visitas/.