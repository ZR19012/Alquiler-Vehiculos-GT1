# 🚗 Sistema de Alquiler de Vehículos

> Proyecto Final — Lógica de Programación  
> Ingeniería en Desarrollo de Software

![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![PSeInt](https://img.shields.io/badge/PSeInt-Pseudoc%C3%B3digo-green)

---

## 📌 Descripción

Sistema de gestión de alquiler de vehículos desarrollado como proyecto final de la materia **Lógica de Programación**. La aplicación permite a los clientes realizar reservas de vehículos para rangos de fechas específicos, validando disponibilidad en tiempo real y gestionando el ciclo de vida de cada vehículo.

La fase inicial del proyecto presenta la lógica del sistema en **pseudocódigo (PSeInt)**, con una implementación posterior en **Python CLI**.

---

## 👥 Integrantes

|           Nombre               |               GitHub                     |      Rol      |
|--------------------------------|------------------------------------------|---------------|
| Josue Emanuel Zúniga Ramírez   |[@ZR19012](https://github.com/ZR19012)    | Desarrollador |
| Ronald Oswaldo Pérez Santos    |[@PS18039](https://github.com/usuario_compañero) | Desarrollador |

---

## 🎯 Funcionalidades del Sistema

### Módulos Principales

| Módulo                            | Descripción | Estado |
|--------                           |-------------|--------|
| 🔍 **Consulta de Disponibilidad** | Verifica si un vehículo está disponible en un rango de fechas dado | ✅ En pseudocódigo |
| 📅 **Gestión de Reservas**         | Permite crear, consultar y cancelar reservas de clientes | ✅ En pseudocódigo |
| 🚦 **Estados de Vehículos** | Administra los estados: Disponible, Alquilado, En Mantenimiento | 🔄 Planificado |
| 👤 **Gestión de Clientes** | Registro y consulta de información de clientes | 🔄 Planificado |

### Lógica de Negocio

- Un **cliente** puede realizar una reserva para un vehículo en un rango de fechas.
- Se valida que el vehículo seleccionado **esté disponible** en las fechas solicitadas.
- Cada vehículo tiene un **estado** que puede ser:
  - 🟢 `Disponible` — Listo para ser reservado
  - 🔴 `Alquilado` — Actualmente en uso por un cliente
  - 🟡 `En Mantenimiento` — No disponible temporalmente


## 🗂️ Estructura del Proyecto

```
Alquiler-Vehiculos-GT1/

pseudocodigo/
  SistemaAlquilerVehiculos.psc
  mostrar_vehiculos.psc
  estado_vehiculo.psc
  reserva.psc

README.md
.gitignore
```

## Avance Actual Entrega 1

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

## Próxima entrega 

Para la siguiente fase del proyecto se tiene planificado:

- Implementar el sistema en Python
- Desarrollar un menú funcional en consola
- Aplicar operaciones CRUD, crear, leer, actualizar, eliminar
- Validar disponibilidad de vehículos por fechas
- Mejorar la lógica de negocio del sistema

Esto permitirá pasar del diseño lógico a una aplicación funcional.
