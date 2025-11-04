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
MedidPy es una biblioteca integral diseñada para llevar a cabo el análisis estadístico descriptivo de datos de naturaleza tanto numérica (cuantitativa) como categórica (cualitativo).

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
### Gestion de datos (DataManager)
- Lectura de archivos CSV con manejo de encoding
- Clasificacion automatica de columnas en cuantitativas y cualitativas
- Integracion con las clases de analisis

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

## 🚀 Ejemplo de Uso

### 1️⃣ Cargar los datos

```python
from estadisticas_paquete.base_data import DataManager
import os

ruta_csv = os.path.join("pruebas", "datos_prueba.csv")
dm = DataManager(ruta_csv)
dm.leer_csv()
dm.clasificar_columnas()

#### Salida esperada
Commit 2: Datos cargados exitosamente. 5 filas.
Commit 3: Clasificación completada. Cuantitativas: ['Edad', 'Nota'], Cualitativas: ['Nombre', 'Sexo']

### Ejemplo 1: Calcualar moda y tipo de moda (Análisis cualitativo)

from estadisticas_paquete.cualitativos import Cualitativos
from estadisticas_paquete.base_data import DataManager
import os

# Cargar los datos
ruta_csv = os.path.join("pruebas", "datos_prueba.csv")
dm = DataManager(ruta_csv)
dm.leer_csv()

# Obtener la columna 'Sexo' como lista
lista_sexo = dm.df['Sexo'].tolist()

# Crear el objeto Cualitativos
cuali = Cualitativos(datos=lista_sexo, nombre="Sexo")

# Calcular moda
moda = cuali.moda()
tipo_moda = cuali.mode_type()

print("Moda:", moda)
print("Tipo de moda:", tipo_moda)

#### Salida esperada
Moda: ['F']
Tipo de moda: Unimodal

### Ejemplo 2: Generar tablas de frecuencia (Análisis Cualitativo)
resumen = cuali.summary(include_table=True, sort_table_by_count=True)

print(f"Variable: {resumen['variable']}")
print(f"Total de datos: {resumen['n']}")
print(f"Moda(s): {resumen['modes']} ({resumen['mode_type']})")

print("\n--- Tabla de Frecuencia ---")
print(f"{'Valor':<10} | {'Conteo':<6} | {'Relativa':<8} | {'Acumulada':<9}")
print("-" * 40)

for fila in resumen['frequency_table']:
    valor = fila['value']
    conteo = fila['count']
    relativa = f"{fila['relative']:.1%}"
    acumulada = fila['cumulative']
    print(f"{valor:<10} | {conteo:<6} | {relativa:<8} | {acumulada:<9}")

#### Salida esperada
Variable: Sexo
Total de datos: 5
Moda(s): ['F'] (Unimodal)

--- Tabla de Frecuencia ---
Valor      | Conteo | Relativa | Acumulada
----------------------------------------
F          | 3      | 60.0%    | 3
M          | 2      | 40.0%    | 5


### Ejemplo 3: Uso con DataFrame directamente
from estadisticas_paquete.cualitativos import Cualitativos
from estadisticas_paquete.base_data import DataManager
import os

ruta_csv = os.path.join("pruebas", "datos_prueba.csv")
dm = DataManager(ruta_csv)
dm.leer_csv()

# Crear el analizador directamente desde el DataFrame
cuali_df = Cualitativos(dm.df)
tabla = cuali_df.build_frequency_table(columna="Sexo")

print("Tabla generada desde DataFrame:")
for fila in tabla:
    print(fila)

#### Salida esperada
Tabla generada desde DataFrame:
{'value': 'Yasmin', 'count': 1, 'relative': 0.2, 'cumulative': 1}
{'value': 'Luis', 'count': 1, 'relative': 0.2, 'cumulative': 2}
{'value': 'Marta', 'count': 1, 'relative': 0.2, 'cumulative': 3}
{'value': 'José', 'count': 1, 'relative': 0.2, 'cumulative': 4}
{'value': 'Lucía', 'count': 1, 'relative': 0.2, 'cumulative': 5}
