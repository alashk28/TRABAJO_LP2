# ParcialLP2: Librería de Análisis Estadístico

Este repositorio contiene una librería desarrollada en Python para realizar cálculos de estadística descriptiva, utilizando los principios de la Programación Orientada a Objetos (POO).

## Integrantes del Grupo

| Nombre | Codigo |
|--------|--------|
| Carmen Tullume Arlette | 20231483
| Flores Villa Brayan | 20231492
| Palma Cruz Yasmin | 20231504

**Institución:** Universidad Nacional Agraria la Molina  
**Curso:** Lenguaje de Programación 2  
**Profesor:** Ana Vargas  
**Fecha de entrega:** 28 de octubre de 2025   

## Descripción

**MedidPy** es una librería completa que permite realizar análisis estadístico descriptivo tanto de datos **cuantitativos** (numéricos) como **cualitativos** (categóricos), además de análisis de relaciones entre variables (**bivariado**).

La librería está completamente implementada usando los principios de **Programación Orientada a Objetos**, incluyendo:
- **Abstracción** mediante clases abstractas
- **Encapsulamiento** de datos y métodos privados
- **Herencia** con jerarquía de clases
- **Polimorfismo** con implementaciones específicas

## Estructura del proyecto
El proyecto está organizado como un paquete modular, donde cada módulo cumple una función específica dentro del análisis estadístico.

 Carpeta / Archivo | Descripción |
|--------------------|-------------|
| **estadisticas_paquete/** | Carpeta principal del paquete estadístico |
| ├── `__init__.py` | Indica que la carpeta es un paquete de Python |
| ├── `base_data.py` | Clase base encargada de leer, clasificar y manejar los datos |
| ├── `stats_base.py` | Clase padre con métodos estadísticos generales |
| ├── `cuantitativos.py` | Contiene la clase para análisis de variables numéricas |
| └── `cualitativos.py` | Contiene la clase para análisis de variables categóricas |
| **pruebas/** | Carpeta destinada a las pruebas del paquete |
| ├── `datos_prueba.csv` | Archivo CSV con datos de ejemplo |
| └── `test_general.py` | Script que ejecuta todas las pruebas del paquete |
| **salidas/** | Carpeta donde se guardan los resultados del análisis |
| └── `resultados.txt` | Archivo de texto con los resultados generados |

## Características Principales

### Análisis de Datos Cuantitativos
- Medidas de tendencia central (media, mediana, moda)
- Medidas de dispersión (varianza, desviación estándar, coeficiente de variación, rango, IQR)
- Medidas de posición (percentiles, cuartiles)
- Medidas de forma (asimetría)
  
### Análisis de Datos Cualitativos
- Moda y distribución de frecuencias
- Tablas de frecuencia (absoluta, relativa, porcentual, acumulada)

## Instalación

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas 

### Pasos de instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/alashk28/TRABAJO_LP2.git
cd TRABAJO_LP2/pruebas
```

2. **Verificar la instalación:**
```bash
python test_general.py
```
