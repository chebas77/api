# API REST - CRUD

Este proyecto implementa una API REST para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un conjunto de datos. Está diseñado con una arquitectura basada en Django y Django REST Framework.

## Arquitectura del Proyecto

- **Framework principal**: Django
- **API REST**: Django REST Framework (DRF)
- **Frontend**: Plantillas HTML con estilos CSS personalizados
- **Base de datos**: SQLite (por defecto, pero puede ser configurada para usar otras bases de datos)
- **Gestión de dependencias**: Virtual environment (venv)

## Librerías Utilizadas

- **Django**: Framework principal para el desarrollo web.
- **Django REST Framework**: Para la creación de la API REST.
- **SQLite**: Base de datos por defecto.
- **Otros**: Librerías estándar de Python para manejo de formularios, vistas y plantillas.

## Uso de la API REST

La API REST permite interactuar con los datos mediante las siguientes rutas:

- **GET /api/products/**: Obtiene la lista de productos.
- **POST /api/products/**: Crea un nuevo producto.
- **GET /api/products/{id}/**: Obtiene los detalles de un producto específico.
- **PUT /api/products/{id}/**: Actualiza un producto existente.
- **DELETE /api/products/{id}/**: Elimina un producto.

## Código Fuente

El código fuente del proyecto se encuentra en la carpeta `src/myapp`. Las plantillas HTML están en `src/myapp/templates/myapp`.

## Pasos para Levantar el Proyecto en Otra Computadora

Sigue los pasos a continuación para configurar y ejecutar el proyecto en otra computadora:

### 1. Clonar el repositorio
```bash
git clone https://github.com/chebas77/api.git
cd api
```

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

source venv/Scripts/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos
```bash
python manage.py migrate
```

### 5. Crear un superusuario (opcional, para acceder al panel de administración)
```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

### 7. Acceder al proyecto
- **Frontend**: Abre `http://127.0.0.1:8000/` en tu navegador.
- **API REST**: Accede a `http://127.0.0.1:8000/api/products/`.

## Notas Adicionales

- Si necesitas instalar nuevas librerías, recuerda actualizarlas en el archivo `requirements.txt` usando:
  ```bash
  pip freeze > requirements.txt
  ```
- Puedes cambiar la configuración de la base de datos en el archivo `settings.py` si deseas usar una base de datos diferente.

## Estructura del Proyecto

```plaintext
api/                        # Raíz del proyecto
├── src/                    # Directorio del código fuente
│   ├── myapp/              # Aplicación principal
│   │   ├── models.py       # Modelos de datos
│   │   ├── views.py        # Vistas basadas en funciones
│   │   ├── urls.py         # Patrones de URL
│   │   ├── admin.py        # Configuraciones del administrador
│   │   └── serializers.py  # Serializadores para la API REST
│   ├── templates/          # Plantillas HTML
│   │   └── myapp/          # Plantillas específicas de la aplicación
│   └── manage.py           # Script de gestión de Django
├── venv/                   # Entorno virtual
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

¡Disfruta trabajando con este proyecto!
