import math
# Hereda de Estadisticos (la clase de stats_base.py)
from .stats_base import Estadisticos 

class Cuantitativos(Estadisticos):

    def __init__(self, ruta_csv):
        """
        El constructor llama al padre (Estadisticos),
        que a su vez carga el CSV en self.df y clasifica las columnas.
        """
        super().__init__(ruta_csv)

    def _get_data_list(self, columna: str) -> tuple[list, int]:
        """
        Función auxiliar CLAVE.
        Obtiene la lista de números limpios desde el DataFrame (self.df)
        que hemos heredado.
        """
        if self.df is None:
            raise RuntimeError("El DataFrame no ha sido cargado.")
            
        # Validamos que la columna sea cuantitativa (lista heredada de DataManager)
        if columna not in self.cuantitativas:
            raise ValueError(f"'{columna}' no es una columna cuantitativa. Disponibles: {self.cuantitativas}")
        
        # Limpia, quita NaNs, y ordena los datos de la columna
        datos = sorted([
            num for num in self.df[columna].dropna() 
            if isinstance(num, (int, float))
        ])
        
        if not datos:
            raise ValueError(f"La columna '{columna}' no tiene datos numéricos válidos.")
            
        return datos, len(datos) # Devuelve la lista y su tamaño

    # --- INICIO DE LÓGICA PURA ADAPTADA ---
    # Todos los métodos de 'rama-cuantitativa' ahora reciben 'columna'

    def calcular_media(self, columna: str):
        datos, n = self._get_data_list(columna)
        
        suma_total = 0
        for num in datos:
            suma_total += num
        
        if n == 0:
            return float('nan')
        return suma_total / n

    def calcular_mediana(self, columna: str):
        datos, n = self._get_data_list(columna)
        
        if n == 0:
            return float('nan')

        if n % 2 == 1:
            indice = n // 2
            return datos[indice]
        else:
            indice_sup = n // 2
            indice_inf = indice_sup - 1
            return (datos[indice_inf] + datos[indice_sup]) / 2

    def calcular_varianza(self, columna: str, es_muestra: bool = True):
        datos, n = self._get_data_list(columna)
        if n == 0:
            return float('nan')
            
        media = self.calcular_media(columna)
        
        suma_diferencias_sq = 0
        for x in datos:
            suma_diferencias_sq += (x - media) ** 2
        
        denominador = (n - 1) if (es_muestra and n > 1) else n
        
        if denominador == 0:
            return 0
        return suma_diferencias_sq / denominador

    def calcular_desviacion_estandar(self, columna: str, es_muestra: bool = True):
        varianza = self.calcular_varianza(columna, es_muestra=es_muestra)
        return math.sqrt(varianza)

    def _calcular_percentil(self, datos_lista: list, n_lista: int, p: float):
        """
        Función auxiliar para calcular percentiles sobre una lista dada.
        """
        posicion = (n_lista - 1) * p
        k = int(posicion)
        d = posicion - k
        
        if d == 0:
            return datos_lista[k]
        else:
            if k + 1 < n_lista:
                return datos_lista[k] + d * (datos_lista[k+1] - datos_lista[k])
            else:
                return datos_lista[k]

    def calcular_cuartiles_iqr(self, columna: str):
        datos, n = self._get_data_list(columna)
        if n == 0:
            return {"q1": float('nan'), "q3": float('nan'), "iqr": float('nan')}
            
        q1 = self._calcular_percentil(datos, n, 0.25)
        q3 = self._calcular_percentil(datos, n, 0.75)
        iqr = q3 - q1
        
        return {
            "q1": q1,
            "q3": q3,
            "iqr": iqr
        }

    def calcular_moda(self, columna: str):
        datos, n = self._get_data_list(columna)
        if n == 0:
            return []

        frecuencias = {}
        for num in datos:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        
        if not frecuencias:
            return []

        max_frecuencia = 0
        for num in frecuencias:
            if frecuencias[num] > max_frecuencia:
                max_frecuencia = frecuencias[num]

        if max_frecuencia == 1 and n > 1:
            return [] 

        modas = []
        for num in frecuencias:
            if frecuencias[num] == max_frecuencia:
                modas.append(num)
        
        return modas[0] if len(modas) == 1 else modas

    def calcular_rango(self, columna: str):
        datos, n = self._get_data_list(columna)
        if n == 0:
            return float('nan')
        return datos[n - 1] - datos[0]

    def calcular_coeficiente_variacion(self, columna: str, es_muestra: bool = True):
        media = self.calcular_media(columna)
        if media == 0:
            return float('nan') 
            
        desviacion = self.calcular_desviacion_estandar(columna, es_muestra=es_muestra)
        return (desviacion / media)

    def calcular_asimetria_pearson(self, columna: str, es_muestra: bool = True):
        media = self.calcular_media(columna)
        mediana = self.calcular_mediana(columna)
        desviacion = self.calcular_desviacion_estandar(columna, es_muestra=es_muestra)

        if desviacion == 0:
            return 0
            
        return (3 * (media - mediana)) / desviacion