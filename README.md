# Sistema de Alquiler de Vehículos

> Proyecto Final — Lógica de Programación  
> Ingeniería en Desarrollo de Software

![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![PSeInt](https://img.shields.io/badge/PSeInt-Pseudoc%C3%B3digo-green)

---

## Descripción

Sistema de gestión de alquiler de vehículos desarrollado como proyecto final de la materia **Lógica de Programación**. La aplicación permite a los clientes realizar reservas de vehículos para rangos de fechas específicos, validando disponibilidad en tiempo real y gestionando el ciclo de vida de cada vehículo

La fase inicial del proyecto presenta la lógica del sistema en **pseudocódigo PSeInt**, con una implementación posterior en **Python**
---

## Integrantes

|           Nombre               |               GitHub                     |      Rol      |
|--------------------------------|------------------------------------------|---------------|
| Josue Emanuel Zúniga Ramírez   |[@ZR19012](https://github.com/ZR19012)    | Desarrollador |
| Ronald Oswaldo Pérez Santos | [@PS18039](https://github.com/PS18039) | Desarrollador |
---

## Funcionalidades del Sistema

### Módulos Principales

| Módulo                            | Descripción | Estado |
|--------                           |-------------|--------|
| 🔍 **Consulta de Disponibilidad** | Verifica si un vehículo está disponible en un rango de fechas dado | ✅ En Python  |
| 📅 **Gestión de Reservas**         | Permite crear, consultar y cancelar reservas de clientes | ✅ En Python  |
| 🚦 **Estados de Vehículos** | Administra los estados: Disponible, Alquilado, En Mantenimiento | ✅ En Python |
| 👤 **Gestión de Clientes** | Registro y consulta de información de clientes | 🔄 Planificado |

### Lógica de Negocio

- Un **cliente** puede realizar una reserva para un vehículo en un rango de fechas.
- Se valida que el vehículo seleccionado **esté disponible** en las fechas solicitadas.
- Cada vehículo tiene un **estado** que puede ser:
  - 🟢 `Disponible` — Listo para ser reservado
  - 🔴 `Alquilado` — Actualmente en uso por un cliente
  - 🟡 `En Mantenimiento` — No disponible temporalmente


## 🗂️ Estructura del Proyecto

```text
Sistema_Alquiler_Vehiculos/
│
├── main.py
├── README.md
├── .gitignore
└── pseudocodigo/
    └── SistemaAlquilerVehiculos.psc
```

## Avance Entrega 1

Actualmente el sistema se encuentra en fase de diseño lógico utilizando pseudocódigo en PSeInt.
El sistema permite simular el flujo básico de alquiler de vehículos, validando disponibilidad y estado.

Se han implementado los siguientes módulos:
- Visualización de vehículos
- Reserva de vehículos
- Cambio de estado de vehículos

Se ha trabajado con estructuras como:
- Arreglos
- Ciclos
- Condicionales
- Menú interactivo

## Próxima entrega 2

Para la siguiente fase del proyecto se tiene planificado:

- Implementar el sistema en Python
- Desarrollar un menú funcional en consola
- Aplicar operaciones CRUD, crear, leer, actualizar, eliminar
- Validar disponibilidad de vehículos por fechas
- Mejorar la lógica de negocio del sistema

Esto permitirá pasar del diseño lógico a una aplicación funcional

## Avance Actual Entrega 2

En esta segunda entrega se realizó la migración inicial del pseudocódigo desarrollado en PSeInt hacia una aplicación funcional en Python por consola

El sistema actualmente permite

- Consultar vehículos disponibles por rango de fechas
- Registrar nuevas reservas
- Ver todas las reservas registradas
- Cancelar reservas existentes
- Visualizar el listado de vehículos y sus estados

Para esta etapa se utilizaron estructuras básicas de Python como listas, diccionarios, funciones, condicionales, ciclos y manejo básico de errores

## Cómo ejecutar el programa

1. Tener instalado Python 3
2. Descargar o clonar el repositorio
3. Abrir la carpeta del proyecto en el IDE
4. Ejecutar el archivo

```bash
python main.py
```

## Pruebas realizadas

- Consulta de disponibilidad de vehículos por fechas
- Registro de una nueva reserva
- Visualización de reservas existentes
- Cancelación de una reserva
- Validación de fechas incorrectas
- Validación de vehículos inexistentes

## Estado actual del proyecto

El proyecto se encuentra en una fase funcional inicial. Actualmente ya cuenta con una aplicación por consola en Python que permite demostrar el flujo principal del sistema de alquiler de vehículos. 

## Próxima entrega 3

Para la siguiente fase del proyecto se tiene planificado:

- Mejorar la estructura del proyecto separando módulos en Python
- Implementar gestión de clientes
- Agregar actualización de reservas y vehículos
- Mejorar validaciones y manejo de errores
- Implementar pruebas unitarias básicas
- Optimizar la lógica de disponibilidad de vehículos
- Mejorar la interfaz por consola

Esto permitirá convertir el proyecto en una aplicación más completa, organizada y estable para la entrega final

# ENTREGA FINAL
## Nuevas funcionalidades implementadas

En la versión actual del sistema se agregaron nuevas mejoras funcionales para fortalecer la lógica de negocio y mejorar la experiencia de uso del sistema.

### Mejoras implementadas

* Gestión dinámica de estados de vehículos
* Módulo de reportes
* Cálculo automático de costos de reserva
* Gestión de precios por día para cada vehículo
* Validaciones avanzadas de fechas y datos de entrada
* Persistencia de datos utilizando SQLite
* Organización modular del proyecto en Python

### Nuevos módulos incorporados

| Módulo                   | Descripción                                                 |
| ------------------------ | ----------------------------------------------------------- |
| 💰 Gestión de Precios    | Cada vehículo posee un precio de alquiler por día           |
| 📊 Reportes              | Permite visualizar reportes de reservas, ingresos y estados |
| 🛠️ Mantenimiento        | Permite cambiar estados de vehículos manualmente            |
| 🗄️ Base de Datos SQLite | Persistencia de información del sistema                     |

## Estructura actual del proyecto

```text
Alquiler-Vehiculos-GT1/
│
├── main.py
├── database.py
├── vehiculos.py
├── reservas.py
├── reportes.py
├── README.md
├── .gitignore
├── data/
│   └── alquiler.db
│
└── pseudocodigo/
    └── SistemaAlquilerVehiculos.psc
```

## Tecnologías utilizadas

* Python 3
* SQLite
* PSeInt
* Git y GitHub

## Funcionalidades actuales del sistema

* Visualización de vehículos
* Gestión de estados
* Registro de reservas
* Cancelación de reservas
* Consulta de disponibilidad
* Gestión de mantenimiento
* Cálculo automático de costos
* Reportes generales
* Reporte de ingresos
* Persistencia de datos

## Reportes disponibles

El sistema actualmente permite generar:

* Reporte de vehículos por estado
* Reporte general de reservas
* Reporte total de ingresos

## Base de datos

El sistema utiliza SQLite para almacenar la información de:

* Vehículos
* Reservas
* Estados
* Totales de alquiler

La base de datos se genera automáticamente al ejecutar el sistema.

## Estado actual del proyecto

Actualmente el sistema se encuentra en una fase funcional avanzada, permitiendo gestionar reservas, disponibilidad, estados de vehículos, costos y reportes mediante una aplicación desarrollada en Python por consola.

## Pruebas Unitarias

Se implementaron pruebas unitarias básicas utilizando el módulo unittest de Python.

Las pruebas verifican:

- Consulta de disponibilidad de vehículos
- Respuesta correcta del sistema
- Validación del tipo de datos retornado

Archivo de prueba:
- prueba_vehiculos.py
