# Gestión de Información sobre Países

### Trabajo Práctico Integrador – Programación I  
**Autores:** Leonardo Morlacca y Nahuel Montero  
**Año:** 2025  

---

## Descripción del Proyecto

Este sistema permite **gestionar información sobre países** utilizando el lenguaje **Python**.  
El objetivo principal es aplicar los conocimientos de estructuras de datos (listas y diccionarios), modularización con funciones, validaciones, manejo de archivos CSV y presentación de estadísticas.

Cada país posee los siguientes datos:
- **Nombre**
- **Población**
- **Superficie (km²)**
- **Continente**

El programa ofrece un **menú interactivo en consola** para realizar operaciones de carga, búsqueda, filtrado, ordenamiento y análisis estadístico de los datos.

---

## Funcionalidades Principales

**Agregar Países**  
Permite registrar uno o varios países con todos sus datos, validando que no existan duplicados.

**Actualizar País**  
Permite modificar la población y superficie de un país existente.

**Buscar País**  
Busca países por nombre (coincidencia parcial o exacta).

**Filtrar Países**  
- Por continente  
- Por rango de población  
- Por rango de superficie  

**Ordenar Países**  
Muestra los países ordenados por nombre, población o superficie (de menor a mayor).

**Mostrar Estadísticas**  
- País con mayor y menor población  
- Promedio de población  
- Promedio de superficie  
- Cantidad de países por continente  

---

## Estructura del Archivo CSV

Ejemplo del archivo `dataset.csv` utilizado por el sistema:

```csv
NOMBRE,POBLACION,SUPERFICIE,CONTINENTE
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
