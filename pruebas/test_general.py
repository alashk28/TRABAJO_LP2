import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import os

from estadisticas_paquete.cualitativos import Cualitativos

from estadisticas_paquete.base_data import DataManager
from estadisticas_paquete.cuantitativos import Cuantitativos

# --- Carga de Datos ---
ruta_csv = os.path.join(os.path.dirname(__file__), "datos_prueba.csv")
print("Cargando datos desde:", ruta_csv)

# Usaremos DataManager SÓLO para leer el CSV y tener el DataFrame
data_manager = DataManager(ruta_csv)
data_manager.leer_csv()

# --- Prueba Cuantitativos  ---
print("\nProbando funciones cuantitativas:")

cuant = Cuantitativos(ruta_csv) 
if cuant.df is not None:
    print("Media de la columna 'Nota':", cuant.media('Nota'))
    print("Mediana:", cuant.mediana('Nota'))
    print("Desviación estándar:", cuant.desviacion_estandar('Nota'))
else:
    print("No se pudieron calcular las estadísticas cuantitativas.")


# --- PRUEBA CUALITATIVOS  ---
print("\n Probando funciones cualitativas (Nueva Clase):")

if data_manager.df is not None:
    # 1. Extraemos la columna 'Sexo' del DataFrame y la convertimos en una LISTA
    try:
        lista_sexo = data_manager.df['Sexo'].tolist()
        
        # 2. Pasamos la LISTA a la nueva clase Cualitativos
        cuali_sexo = Cualitativos(datos=lista_sexo, nombre="Sexo")

        # 3. ¡Llamamos al método summary() para obtener la tabla!
        #    Usamos sort_table_by_count=True para ordenarla.
        resumen = cuali_sexo.summary(include_table=True, sort_table_by_count=True)

        # 4. Imprimimos los resultados de la tabla
        print(f"\n--- Tabla de Frecuencia para: {resumen['variable']} ---")
        print(f"Total de datos: {resumen['n']}")
        print(f"Moda(s): {resumen['modes']} ({resumen['mode_type']})")
        
        print("\n" + "-"*30)
        print(f"{'Valor':<10} | {'Conteo':<6} | {'Relativa':<8} | {'Acumulada':<9}")
        print("-" * 30)

        # Iteramos sobre la tabla de frecuencia generada
        if 'frequency_table' in resumen:
            for fila in resumen['frequency_table']:
                # Formateamos la salida para que se vea como una tabla
                valor = str(fila['value'])
                conteo = str(fila['count'])
                relativa = f"{fila['relative']:.1%}" # Formato de porcentaje
                acumulada = str(fila['cumulative'])
                
                print(f"{valor:<10} | {conteo:<6} | {relativa:<8} | {acumulada:<9}")
        print("-" * 30)

    except KeyError:
        print("Error: La columna 'Sexo' no se encontró en el CSV.")
    except Exception as e:
        print(f"Ocurrió un error al analizar datos cualitativos: {e}")
        
else:
    print("No se guardaron resultados porque la carga de datos falló.")