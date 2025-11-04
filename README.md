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
**Fecha de entrega:** Martes 28 de Octubre de 2025   

## Descripción
Elaboramos una biblioteca integral diseñada para llevar a cabo el análisis estadístico descriptivo de datos de naturaleza tanto numérica (cuantitativa) como categórica (cualitativo).

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
```

**Salida esperada**
```
Commit 2: Datos cargados exitosamente. 5 filas.
Commit 3: Clasificación completada. Cuantitativas: ['Edad', 'Nota'], Cualitativas: ['Nombre', 'Sexo']
```

### Ejemplo 1: Calcualar moda y tipo de moda (Análisis cualitativo)
```python
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
```

**Salida esperada**
```
Moda: ['F']
Tipo de moda: Unimodal
```

### Ejemplo 2: Generar tablas de frecuencia (Análisis Cualitativo)
```python
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
```
**Salida esperada**
```
Variable: Sexo
Total de datos: 5
Moda(s): ['F'] (Unimodal)

--- Tabla de Frecuencia ---
Valor      | Conteo | Relativa | Acumulada
----------------------------------------
F          | 3      | 60.0%    | 3
M          | 2      | 40.0%    | 5
```

### Ejemplo 3: Uso con DataFrame directamente
```python
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
```

**Salida esperada**
```
Tabla generada desde DataFrame:
{'value': 'Yasmin', 'count': 1, 'relative': 0.2, 'cumulative': 1}
{'value': 'Luis', 'count': 1, 'relative': 0.2, 'cumulative': 2}
{'value': 'Marta', 'count': 1, 'relative': 0.2, 'cumulative': 3}
{'value': 'José', 'count': 1, 'relative': 0.2, 'cumulative': 4}
{'value': 'Lucía', 'count': 1, 'relative': 0.2, 'cumulative': 5}
```
### Ejemplo 4: Cálculo del las medidas de tendencia central (análisis cuantitativo)

```
# Importamos la clase desde el paquete
from estadisticas_paquete import Cuantitativos

# 1. Creamos la instancia pasándole la ruta del CSV
# La clase (gracias a la herencia) se encarga de cargar y 
# clasificar las columnas 'Nota' y 'Edad'
stats_cuanti = Cuantitativos("pruebas/datos_prueba.csv")

# 2. Llamamos a los métodos de cálculo pasando el nombre de la columna
print("--- Análisis de 'Nota' ---")
media_nota = stats_cuanti.calcular_media("Nota")
mediana_nota = stats_cuanti.calcular_mediana("Nota")
std_nota = stats_cuanti.calcular_desviacion_estandar("Nota")

print(f"Media: {media_nota:.2f}")
print(f"Mediana: {mediana_nota:.2f}")
print(f"Desviación Estándar: {std_nota:.2f}")

print("\n--- Análisis de 'Edad' ---")
asimetria_edad = stats_cuanti.calcular_asimetria_pearson("Edad")
cuartiles_edad = stats_cuanti.calcular_cuartiles_iqr("Edad")

print(f"Asimetría de Pearson (Edad): {asimetria_edad:.2f}")
print(f"Cuartiles (Edad): {cuartiles_edad}")
```
**Resultado**
```
--- Análisis de 'Nota' ---
Media: 16.60
Mediana: 17.00
Desviación Estándar: 2.07

--- Análisis de 'Edad' ---
Asimetría de Pearson (Edad): 1.50
Cuartiles (Edad): {'q1': 21.0, 'q3': 22.0, 'iqr': 1.0} 
```
###Ejemplo 5: Aplicación de análisis cuantitativo

```
stats_salarios = Cuantitativos("pruebas/salarios.csv")

# --- Análisis de la columna 'Salario' ---
print("--- Análisis de 'Salario' ---")
print(f"Media Salarial: {stats_salarios.calcular_media('Salario'):.2f}")
print(f"Mediana Salarial: {stats_salarios.calcular_mediana('Salario'):.2f}")
print(f"Desviación Estándar (Salario): {stats_salarios.calcular_desviacion_estandar('Salario'):.2f}")
print(f"Rango Salarial: {stats_salarios.calcular_rango('Salario')}")


# --- Análisis de la columna 'Experiencia' ---
print("\n--- Análisis de 'Experiencia' ---")
print(f"Media de Experiencia: {stats_salarios.calcular_media('Experiencia'):.2f}")
print(f"Mediana de Experiencia: {stats_salarios.calcular_mediana('Experiencia'):.2f}")
cuartiles_exp = stats_salarios.calcular_cuartiles_iqr('Experiencia')
print(f"Cuartiles (Experiencia): {cuartiles_exp}")
```
**Resultado**
```
--- Análisis de 'Salario' ---
Media Salarial: 73250.00
Mediana Salarial: 67500.00
Desviación Estándar (Salario): 40523.25
Rango Salarial: 115000

--- Análisis de 'Experiencia' ---
Media de Experiencia: 6.00
Mediana de Experiencia: 5.50
Cuartiles (Experiencia): {'q1': 1.75, 'q3': 8.5, 'iqr': 6.75}
```

##Jerarquía del clases
```
DataManager (en base_data.py)
  │   - Carga el CSV con Pandas
  │   - Clasifica columnas (cuantitativas, cualitativas)
  ↓
Estadisticos (en stats_base.py)
  │   - Hereda de DataManager
  │   - En su __init__, ejecuta leer_csv() y clasificar_columnas()
  │   - Guarda el self.df listo para usar
  ↓
┌─┴─────────────────────────────────┐
│                                 │
Cuantitativos                     Cualitativos
 - Hereda de Estadisticos          - Hereda de Estadisticos
 - Métodos:                        - Métodos:
   - calcular_media(col)             - summary(col)
   - calcular_mediana(col)           - build_frequency_table(col)
   - calcular_moda(col)              - modes(col)
   - calcular_varianza(col)          - moda(col)
   - calcular_desviacion_estandar(col) - mode_type(col)
   - calcular_cuartiles_iqr(col)     - relative_frequencies(col)
   - calcular_rango(col)
   - calcular_coeficiente_variacion(col)
   - calcular_asimetria_pearson(col)
```

## Conceptos de POO usados en el proyecto
Nuestro proyecto aplica los **cuatro pilares fundamentales de la POO**:  
**Abstracción, Encapsulamiento, Herencia y Polimorfismo**, en el contexto del análisis estadístico de datos cuantitativos y cualitativos.

---

### 1. **Abstracción**
La **abstracción** nos permite representar los componentes esenciales del análisis estadístico mediante clases, ocultando los detalles complejos de implementación.

```python
class Cualitativos:
    """Clase para estadísticas cualitativas (tablas de frecuencia, moda, etc.)"""
    def __init__(self, datos=None, nombre="Variable_Cualitativa"):
        self.nombre = nombre
        self.datos = []
        if datos is not None:
            for x in datos:
                self.datos.append(x)
```
### 2. **Encapsulamiento**
El **encapsulamiento** protege los datos internos de las clases, limitando el acceso directo y controlando su modificación mediante métodos internos.
```python
class Cualitativos:
    def __init__(self, datos=None, nombre="Variable_Cualitativa"):
        self.nombre = nombre
        self.datos = []
        self._tabla = None
        self._modas = None

    def _frecuencias_de_lista(self, lista):
        frec = {}
        for valor in lista:
            if valor in frec:
                frec[valor] = frec[valor] + 1
            else:
                frec[valor] = 1
        return frec
```

### 3. **Herencia**
La **herencia** permite reutilizar código existente para crear nuevas clases más específicas sin volver a escribir la lógica básica.
```python
from .base_data import DataManager

class Estadisticos(DataManager):
    def __init__(self, ruta_csv):
        super().__init__(ruta_csv)
        self.leer_csv()
        self.clasificar_columnas()
```
### 4. **Polimorfismo**
El **polimorfismo** se aplica cuando diferentes clases comparten métodos con el mismo nombre, pero cada uno se comporta de forma distinta según el contexto.
```python
# En cuantitativos.py (cálculo de moda numérica)
def calcular_moda(self):
    # cuenta frecuencias en self.datos y devuelve:
    # - [] si no hay moda
    # - un solo número si es unimodal
    # - una lista si es multimodal
    frecuencias = {}
    for num in self.datos:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    # ... lógica para obtener modas ...
    return modas  # puede ser [] / valor único / lista

def modes(self, columna=None):
    lista = self._obtener_lista(columna=columna)
    counts = self._frecuencias_de_lista(lista)
    return result 
def moda(self, columna=None):
    return self.modes(columna=columna)  # alias en español

```
