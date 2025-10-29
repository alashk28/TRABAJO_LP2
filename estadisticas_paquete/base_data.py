import pandas as pd

class DataManager:
    """
    Clase base encargada de gestionar la carga de datos y el DataFrame de Pandas
    """
    def __init__(self, ruta_csv):
        self.ruta = ruta_csv
        self.df = None
        self.cuantitativas = []
        self.cualitativas = []

    def leer_csv(self, encoding='latin1'):
        """
        Carga un archivo CSV en un DataFrame de Pandas.
        Permite definir el encoding del archivo.
        """
        try:
            self.df = pd.read_csv(self.ruta, encoding=encoding)
            print(f"Commit 2: Datos cargados exitosamente. {len(self.df)} filas.")
            return True
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {self.ruta}")
            return False
        except Exception as e:
            print(f"Error al leer el CSV: {e}")
            return False

    def clasificar_columnas(self):
        """
        Clasifica las columnas en cuantitativas y cualitativas utilizando los tipos de datos de Pandas.
        """
        if self.df is None:
            print("Error: DataFrame no cargado.")
            return [], []

        self.cuantitativas = []
        self.cualitativas = []

        for columna in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[columna]):
                self.cuantitativas.append(columna)
            else:
                self.cualitativas.append(columna)

        print(f"Commit 3: Clasificación completada. Cuantitativas: {self.cuantitativas}, Cualitativas: {self.cualitativas}")
        return self.cuantitativas, self.cualitativas
