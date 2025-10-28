# Establecer la herencia de DataManager
from .base_data import DataManager

class Estadisticos(DataManager):
    def __init__(self, ruta_csv):
        super().__init__(ruta_csv)
        
        self.leer_csv()
        self.clasificar_columnas()

    def get_cuantitativos_df(self):
        return self.df[self.cuantitativas]

    def get_cualitativos_df(self):
        return self.df[self.cualitativas]