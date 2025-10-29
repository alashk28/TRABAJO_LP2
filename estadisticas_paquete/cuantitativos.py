from .stats_base import Estadisticos
import pandas as pd

class Cuantitativos(Estadisticos):
    def __init__(self, df):
        super().__init__(df)

    def media(self, columna):
        try:
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
