# Contenido para estadisticas_paquete/cuantitativos.py
from .stats_base import Estadisticos
import pandas as pd

class Cuantitativos(Estadisticos):

    # Debe aceptar ruta_csv para que la herencia de Estadisticos funcione
    def __init__(self, ruta_csv):
        super().__init__(ruta_csv)

    def media(self, columna):
        try:
            # self.df (el DataFrame) es heredado de Estadisticos
            return self.df[columna].mean()
        except Exception as e:
            print(f"Error al calcular la media: {e}")
            return None

    def mediana(self, columna):
        try:
            return self.df[columna].median()
        except Exception as e:
            print(f"Error al calcular la mediana: {e}")
            return None

    def desviacion_estandar(self, columna):
        try:
            return self.df[columna].std()
        except Exception as e:
            print(f"Error al calcular la desviación estándar: {e}")
            return None