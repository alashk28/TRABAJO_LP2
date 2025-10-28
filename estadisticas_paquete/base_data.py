import pandas as pd

class DataManager:
    """
    Clase base encargada de gestionar la carga de datos y el DataFrame de Pandas"""
    def __init__(self, ruta_csv):
        self.ruta = ruta_csv
        self.df = None 
        self.cuantitativas = []
        self.cualitativas = []

    def leer_csv(self):
        """Implementa pd.read_csv() para cargar el DataFrame."""
        try:
            self.df = pd.read_csv(self.ruta)
            print(f"Commit 2: Datos cargados exitosamente. {len(self.df)} filas.")
            return True
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {self.ruta}")
            return False
        except Exception as e:
            print(f"Error al leer el CSV: {e}")
            return False