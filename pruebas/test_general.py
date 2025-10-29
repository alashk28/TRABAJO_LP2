# Inicializando
import sys
import os
import pandas as pd

# Esto permite importar tu paquete desde la carpeta padre
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estadisticas_paquete.base_data import DataManager
from estadisticas_paquete.cuantitativos import Cuantitativos
from estadisticas_paquete.cualitativos import Cualitativos

# Cargando CSV
ruta_csv = os.path.join(os.path.dirname(__file__), "datos_prueba.csv")
print("Cargando datos desde:", ruta_csv)

data_manager = DataManager(ruta_csv)
# Intentamos leer el CSV con encoding utf-8-sig para evitar errores con BOM
if not data_manager.leer_csv(encoding='utf-8-sig'):
    print("No se pudo cargar el CSV. Saliendo...")
    sys.exit(1)

# Prueba para variables cuantitativas
print("\nProbando funciones cuantitativas:")
cuant = Cuantitativos(data_manager.df)
print("Media de la columna 'Nota':", cuant.media('Nota'))
print("Mediana:", cuant.mediana('Nota'))
print("Desviación estándar:", cuant.desviacion_estandar('Nota'))

# Prueba para variables cualitativas
print("\nProbando funciones cualitativas:")
cuali = Cualitativos(data_manager.df)
print("Moda de 'Sexo':", cuali.moda('Sexo'))

# Guardando resultados en la carpeta 'salidas'
ruta_salida = os.path.join(os.path.dirname(__file__), "..", "salidas", "resultados.txt")
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)  # Asegura que la carpeta exista

with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write("RESULTADOS DE LAS PRUEBAS\n\n")
    f.write("Media de Nota: " + str(cuant.media('Nota')) + "\n")
    f.write("Mediana: " + str(cuant.mediana('Nota')) + "\n")
    f.write("Desviación estándar: " + str(cuant.desviacion_estandar('Nota')) + "\n")
    f.write("Moda de Sexo: " + str(cuali.moda('Sexo')) + "\n")

print(f"\nResultados guardados en: {ruta_salida}")
