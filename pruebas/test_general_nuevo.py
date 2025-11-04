import sys
import os
import pprint # Importamos pprint para imprimir diccionarios de forma legible

# --- Configuración del PATH ---
# Esto añade el directorio raíz (TRABAJO_LP2) al path de Python
# para que podamos importar 'estadisticas_paquete'
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

# --- Importaciones del Paquete ---
# Importamos las clases finales que el usuario debe usar
from estadisticas_paquete import Cuantitativos, Cualitativos

def run_cuantitativos_tests(stats_cuanti):
    """
    Ejecuta todas las pruebas para la clase Cuantitativos.
    Usaremos las columnas 'Nota' y 'Edad'.
    """
    print("=" * 40)
    print("📊 INICIANDO PRUEBAS CUANTITATIVAS 📊")
    print("=" * 40)
    
    columnas_cuanti = ['Nota', 'Edad']
    
    for col in columnas_cuanti:
        print(f"\n--- Pruebas para la columna: '{col}' ---")
        
        try:
            # --- Métodos de Lógica Pura ---
            print(f"Media:                 {stats_cuanti.calcular_media(col)}")
            print(f"Mediana:               {stats_cuanti.calcular_mediana(col)}")
            print(f"Moda(s):               {stats_cuanti.calcular_moda(col)}")
            print(f"Varianza (muestra):    {stats_cuanti.calcular_varianza(col, es_muestra=True)}")
            print(f"Desv. Estándar (m):    {stats_cuanti.calcular_desviacion_estandar(col, es_muestra=True)}")
            print(f"Rango:                 {stats_cuanti.calcular_rango(col)}")
            print(f"Coef. de Variación:    {stats_cuanti.calcular_coeficiente_variacion(col)}")
            print(f"Asimetría (Pearson):   {stats_cuanti.calcular_asimetria_pearson(col)}")
            
            # Prueba de Cuartiles (devuelve un diccionario)
            cuartiles = stats_cuanti.calcular_cuartiles_iqr(col)
            print(f"Cuartiles (Q1, Q3):    Q1={cuartiles['q1']}, Q3={cuartiles['q3']}")
            print(f"Rango Intercuartil:    {cuartiles['iqr']}")

        except Exception as e:
            print(f"ERROR al procesar la columna '{col}': {e}")

def run_cualitativos_tests(stats_cuali):
    """
    Ejecuta todas las pruebas para la clase Cualitativos.
    Usaremos las columnas 'Sexo' y 'Nombre'.
    """
    print("\n" + "=" * 40)
    print("📋 INICIANDO PRUEBAS CUALITATIVAS 📋")
    print("=" * 40)
    
    # --- PRUEBA 1: Columna 'Sexo' (tiene datos repetidos) ---
    col_sexo = 'Sexo'
    print(f"\n--- Pruebas para la columna: '{col_sexo}' ---")
    
    try:
        # Prueba de métodos individuales
        print(f"Moda (primer valor):   {stats_cuali.moda(col_sexo)}")
        print(f"Modas (lista):         {stats_cuali.modes(col_sexo)}")
        print(f"Tipo de Moda:          {stats_cuali.mode_type(col_sexo)}")
        
        # Prueba de Frecuencias Relativas (devuelve dict)
        print("\nFrecuencias Relativas:")
        pprint.pprint(stats_cuali.relative_frequencies(col_sexo))

        # Prueba de Tabla de Frecuencias (formateada)
        print("\nTabla de Frecuencias (ordenada por valor):")
        tabla_sexo = stats_cuali.build_frequency_table(col_sexo, sort_by_count=False)
        print_frequency_table(tabla_sexo)

        # Prueba de SUMMARY (El método más completo)
        print(f"\nResumen (Summary) para '{col_sexo}':")
        # El summary ya incluye la tabla, la pedimos ordenada por conteo
        resumen_sexo = stats_cuali.summary(col_sexo, include_table=True, sort_table_by_count=True)
        pprint.pprint(resumen_sexo)
        
    except Exception as e:
        print(f"ERROR al procesar la columna '{col_sexo}': {e}")

    # --- PRUEBA 2: Columna 'Nombre' (no tiene datos repetidos) ---
    col_nombre = 'Nombre'
    print(f"\n--- Pruebas para la columna: '{col_nombre}' ---")
    
    try:
        # Debería ser Amodal
        print(f"Moda (primer valor):   {stats_cuali.moda(col_nombre)}")
        print(f"Modas (lista):         {stats_cuali.modes(col_nombre)}")
        print(f"Tipo de Moda:          {stats_cuali.mode_type(col_nombre)}")

        # Prueba de Summary (sin tabla)
        print(f"\nResumen (Summary) para '{col_nombre}' (sin tabla):")
        resumen_nombre = stats_cuali.summary(col_nombre, include_table=False)
        pprint.pprint(resumen_nombre)
        
    except Exception as e:
        print(f"ERROR al procesar la columna '{col_nombre}': {e}")


def print_frequency_table(table: list):
    """Función auxiliar para imprimir la tabla de frecuencias bonita."""
    if not table:
        print("Tabla vacía.")
        return
        
    print("-" * 45)
    print(f"{'Valor':<12} | {'Conteo':<8} | {'Relativa':<10} | {'Acumulada':<9}")
    print("-" * 45)
    
    for fila in table:
        valor = str(fila['value'])
        conteo = str(fila['count'])
        relativa = f"{fila['relative']:.1%}" # Formato de porcentaje
        acumulada = str(fila['cumulative'])
        
        print(f"{valor:<12} | {conteo:<8} | {relativa:<10} | {acumulada:<9}")
    print("-" * 45)


def main():
    """
    Función principal que carga los datos e inicia las pruebas.
    """
    print("Iniciando Test General del Paquete de Estadísticas...")
    
    # 1. Definir la ruta al archivo CSV
    # __file__ es la ruta de este script (test_general_nuevo.py)
    ruta_csv = os.path.join(os.path.dirname(__file__), "datos_prueba.csv")
    
    if not os.path.exists(ruta_csv):
        print(f"ERROR FATAL: No se encontró el archivo 'datos_prueba.csv' en {ruta_csv}")
        return

    print(f"Usando datos de: {ruta_csv}\n")
    
    try:
        # 2. Inicializar las clases
        # Gracias a la herencia, solo necesitamos la ruta.
        # Ambas clases cargarán los datos automáticamente.
        stats_cuantitativos = Cuantitativos(ruta_csv)
        stats_cualitativos = Cualitativos(ruta_csv)
        
        # 3. Verificar que los datos se cargaron
        if stats_cuantitativos.df is None:
            print("ERROR FATAL: El DataFrame no se cargó en Cuantitativos.")
            return
            
        if stats_cualitativos.df is None:
            print("ERROR FATAL: El DataFrame no se cargó en Cualitativos.")
            return

        print("\n--- Carga de Datos Exitosa ---")
        print(f"Columnas Cuantitativas detectadas: {stats_cuantitativos.cuantitativas}")
        print(f"Columnas Cualitativas detectadas:  {stats_cualitativos.cualitativas}")
        print("---------------------------------\n")

        # 4. Ejecutar los módulos de prueba
        run_cuantitativos_tests(stats_cuantitativos)
        run_cualitativos_tests(stats_cualitativos)
        
        print("\n--- Pruebas Finalizadas ---")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado durante la inicialización: {e}")

# --- Punto de Entrada ---
if __name__ == "__main__":
    main()  