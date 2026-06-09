# Sistema de Optimización de Rutas de Reparto

## Descripción del Proyecto

Este proyecto consiste en una aplicación web desarrollada para la gestión y optimización de rutas de reparto utilizando tecnologías NoSQL.

La solución permite administrar información relacionada con vehículos, conductores, clientes y rutas de distribución mediante una interfaz web desarrollada en Flask y una base de datos MongoDB Atlas.

El objetivo principal es reducir los tiempos de entrega, mejorar la organización logística y facilitar la consulta de información en tiempo real.

---

## Tecnologías Utilizadas

### Backend

* Python 3.13
* Flask
* PyMongo

### Base de Datos

* MongoDB Atlas

### Frontend

* HTML5
* Bootstrap 5

### Control de Versiones

* Git
* GitHub

---

## Arquitectura de la Solución

La arquitectura implementada sigue un modelo de tres capas:

### Presentación

Interfaz web desarrollada con HTML y Bootstrap.

### Lógica de Negocio

Aplicación Flask encargada de procesar solicitudes y comunicarse con MongoDB.

### Persistencia de Datos

MongoDB Atlas almacena la información de:

* Clientes
* Conductores
* Vehículos
* Rutas
* Historial de rutas

---

## Funcionalidades Implementadas

### Dashboard Principal

Permite visualizar indicadores en tiempo real:

* Total de rutas
* Total de clientes
* Total de conductores
* Total de vehículos

### Gestión de Vehículos

* Consulta de vehículos registrados
* Registro de nuevos vehículos

### Gestión de Clientes

* Consulta de clientes

### Gestión de Conductores

* Consulta de conductores

### Gestión de Rutas

* Consulta de rutas disponibles

---

## Estructura del Proyecto

```text
ProyectoLogistica/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── vehiculos.html
│   ├── agregar_vehiculo.html
│   ├── clientes.html
│   ├── conductores.html
│   └── rutas.html
│
└── screenshots/
```

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/hjdiaz05/optimizacion-rutas-mongodb.git
```

### Entrar al proyecto

```bash
cd optimizacion-rutas-mongodb
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar:

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

---

## Modelo de Datos

### Colección Clientes

```json
{
  "cliente_id": "C001",
  "nombre": "Supermercado Nacional",
  "ciudad": "Santo Domingo",
  "estado": "Activo"
}
```

### Colección Conductores

```json
{
  "conductor_id": "D001",
  "nombre": "Juan Perez",
  "licencia": "LIC12345",
  "estado": "Disponible"
}
```

### Colección Vehículos

```json
{
  "vehiculo_id": "V001",
  "placa": "L123456",
  "marca": "Hyundai",
  "modelo": "HD65",
  "tipo": "Camion",
  "capacidad_kg": 5000,
  "estado": "Disponible"
}
```

### Colección Rutas

```json
{
  "ruta_id": "R001",
  "fecha": "2026-06-08",
  "estado": "Activa",
  "prioridad": "Alta"
}
```

---

## Capturas de Pantalla

Agregar capturas de:

1. Dashboard principal.
2. Listado de vehículos.
3. Formulario agregar vehículo.
4. Listado de clientes.
5. Listado de conductores.
6. MongoDB Atlas.

---

## Autor

Hector Diaz

Proyecto Final - Bases de Datos NoSQL

Universidad Abierta para Adultos (UAPA)
