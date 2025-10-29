from .stats_base import Estadisticos
import pandas as pd

class Cualitativos(Estadisticos):
    def __init__(self, ruta_csv):
        super().__init__(ruta_csv)

    def moda(self, columna):
        try:
            return self.df[columna].mode()[0]
        except Exception as e:
            print("Error al calcular la moda:", e)
            return None
