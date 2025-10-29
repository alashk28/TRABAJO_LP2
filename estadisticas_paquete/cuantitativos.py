from .stats_base import Estadisticos
import pandas as pd

class Cuantitativos(Estadisticos):
    def __init__(self, df):
        # Guardamos directamente el DataFrame que ya fue cargado
        self.df = df

    def media(self, columna):
        try:
            return self.df[columna].mean()
        except Exception as e:
            print("Error al calcular la media:", e)
            return None

    def mediana(self, columna):
        try:
            return self.df[columna].median()
        except Exception as e:
            print("Error al calcular la mediana:", e)
            return None

    def desviacion_estandar(self, columna):
        try:
            return self.df[columna].std()
        except Exception as e:
            print("Error al calcular la desviación estándar:", e)
            return None
