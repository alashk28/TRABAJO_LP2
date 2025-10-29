from .stats_base import Estadisticos
import pandas as pd

class Cualitativos(Estadisticos):
    def __init__(self, df):
        # Guardamos directamente el DataFrame que ya fue cargado
        self.df = df

    def moda(self, columna):
        try:
            return self.df[columna].mode()[0]
        except Exception as e:
            print("Error al calcular la moda:", e)
            return None
