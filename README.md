# API de Gestión de Recursos Humanos (HRMS)

Proyecto Django REST Framework para gestión de empleados, departamentos, asistencia y nómina.

## Descripción

Esta API expone endpoints CRUD para las siguientes entidades:

- `Empleado`
- `Departamento`
- `Asistencia`
- `Nómina`

Incluye documentación OpenAPI con Swagger y Redoc.

## Requisitos

- Python 3.11
- pip
- SQLite (ya configurado por defecto)

## Dependencias principales

- Django==6.0
- djangorestframework==3.17.1
- drf-spectacular==0.29.0
- django-environ==0.12.0
- djangorestframework_simplejwt==5.5.1
- drf-yasg==1.21.15

## Instalación

1. Crear y activar el entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

3. Crear archivo `.env` en la raíz del proyecto con al menos:

```env
SECRET_KEY=tu_secreto_aqui
DEBUG=False
```

4. Aplicar migraciones:

```powershell
python manage.py migrate
```

5. Ejecutar el servidor:

```powershell
python manage.py runserver
```

## Endpoints principales

Base API: `/api/v1/`

- `GET /api/v1/empleados/` - Listar empleados
- `POST /api/v1/empleados/` - Crear empleado
- `GET /api/v1/empleados/{id}/` - Detalle empleado
- `PUT /api/v1/empleados/{id}/` - Actualizar empleado
- `PATCH /api/v1/empleados/{id}/` - Actualizar parcialmente empleado
- `DELETE /api/v1/empleados/{id}/` - Eliminar empleado

- `GET /api/v1/departamentos/` - Listar departamentos
- `POST /api/v1/departamentos/` - Crear departamento
- `GET /api/v1/departamentos/{id}/` - Detalle departamento
- `PUT /api/v1/departamentos/{id}/` - Actualizar departamento
- `PATCH /api/v1/departamentos/{id}/` - Actualizar parcialmente departamento
- `DELETE /api/v1/departamentos/{id}/` - Eliminar departamento

- `GET /api/v1/asistencia/` - Listar registros de asistencia
- `POST /api/v1/asistencia/` - Crear registro de asistencia
- `GET /api/v1/asistencia/{id}/` - Detalle asistencia
- `PUT /api/v1/asistencia/{id}/` - Actualizar asistencia
- `PATCH /api/v1/asistencia/{id}/` - Actualizar parcialmente asistencia
- `DELETE /api/v1/asistencia/{id}/` - Eliminar asistencia

- `GET /api/v1/nomina/` - Listar nóminas
- `POST /api/v1/nomina/` - Crear nómina
- `GET /api/v1/nomina/{id}/` - Detalle nómina
- `PUT /api/v1/nomina/{id}/` - Actualizar nómina
- `PATCH /api/v1/nomina/{id}/` - Actualizar parcialmente nómina
- `DELETE /api/v1/nomina/{id}/` - Eliminar nómina

## Documentación de OpenAPI

- Swagger UI: `http://127.0.0.1:8000/docs/`
- Redoc: `http://127.0.0.1:8000/redoc/`
- Esquema JSON: `http://127.0.0.1:8000/schema/`

## Modelos y campos

### Empleado

- `nombre` (CharField)
- `apellidos` (CharField)
- `edad` (IntegerField)
- `puesto` (CharField)
- `salario` (CharField)
- `fecha_contratacion` (DateField)

### Departamento

- `nombre` (CharField, único)
- `descripcion` (TextField)
- `gerente` (ForeignKey a Empleado, opcional)

### Asistencia

- `empleado` (ForeignKey a Empleado)
- `fecha` (DateField)
- `hora_entrada` (TimeField)
- `hora_salida` (TimeField, opcional)

### Nómina

- `empleado` (ForeignKey a Empleado)
- `periodo_inicio` (DateField)
- `periodo_fin` (DateField)
- `salario_base` (DecimalField)
- `deducciones` (DecimalField)
- `bonificaciones` (DecimalField)
- `fecha_pago` (DateField)
- `salario_neto` (campo calculado)

## Pruebas unitarias

El proyecto incluye pruebas unitarias para los modelos y los endpoints CRUD básicos. Para ejecutar todas las pruebas:

```powershell
.\.venv\Scripts\python.exe manage.py test
```

Las pruebas cubren:

- creación y listado de empleados
- creación y listado de departamentos
- creación y listado de registros de asistencia
- creación y listado de nóminas
- cálculo de `salario_neto` en el modelo `Nomina`

## Consideraciones

- Actualmente no hay autenticación o permisos especiales configurados en la API.
- La base de datos utilizada por defecto es `SQLite` en `db.sqlite3`.
- El proyecto usa `drf-spectacular` para generar el esquema OpenAPI.
- Se añadió `apps/__init__.py` para que el paquete `apps` sea reconocido correctamente por Django y los tests.

## Comandos útiles

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
- `python manage.py test`

## Estructura del proyecto

- `HRMS/` - configuración principal de Django
- `apps/employees/` - empleados
- `apps/departments/` - departamentos
- `apps/attendance/` - asistencia
- `apps/payroll/` - nómina

---

Esta documentación cubre la configuración mínima y los endpoints expuestos por la API actual. Ajusta el archivo `.env` y la configuración de `settings.py` según tu entorno de despliegue.