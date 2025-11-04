import math
import pandas as pd
# Hereda de Estadisticos (la clase de stats_base.py)
from .stats_base import Estadisticos 

class Cualitativos(Estadisticos):

    def __init__(self, ruta_csv):
        """
        El constructor llama al padre (Estadisticos),
        que a su vez carga el CSV en self.df y clasifica las columnas.
        """
        super().__init__(ruta_csv)


    def _longitud(self, iterable):
        c = 0
        for _ in iterable:
            c = c + 1
        return c

    def _frecuencias_de_lista(self, lista):
        frec = {}
        for valor in lista:
            frec[valor] = frec.get(valor, 0) + 1
        return frec

    # 2. El "Puente": _obtener_lista
    def _obtener_lista(self, columna: str) -> list:
        """
        Obtiene la lista de valores limpios desde el DataFrame (self.df)
        que hemos heredado.
        """
        if self.df is None:
            raise RuntimeError("El DataFrame no ha sido cargado.")
            
        # Validamos que la columna sea cualitativa
        if columna not in self.cualitativas:
            raise ValueError(f"'{columna}' no es una columna cualitativa. Disponibles: {self.cualitativas}")
        
        # Esta lógica de limpieza ya la tenías y es excelente
        serie = self.df[columna].tolist()
        lista = []
        for v in serie:
            try:
                # Maneja NaNs de Pandas
                if isinstance(v, float) and math.isnan(v):
                    lista.append("Missing")
                    continue
            except Exception:
                pass
            # Maneja Nones de Python
            if v is None:
                lista.append("Missing")
            else:
                lista.append(str(v).strip())
        return lista

    # 3. Métodos Principales Adaptados
    # Ahora todos reciben 'columna' y la usan

    def build_frequency_table(self, columna: str, sort_by_count=False, descending=True):
        lista = self._obtener_lista(columna)
        counts = self._frecuencias_de_lista(lista)
        total = self._longitud(lista)
        rows = []

        if total == 0:
            return []
            
        for v in counts:
            c = counts[v]
            rel = c / total
            row = {'value': v, 'count': c, 'relative': rel, 'cumulative': None}
            rows.append(row)

        running = 0
        for i in range(0, self._longitud(rows)):
            running = running + rows[i]['count']
            rows[i]['cumulative'] = running

        if sort_by_count:
            n = self._longitud(rows)
            for i in range(0, n):
                for j in range(0, n - 1 - i):
                    a = rows[j]['count']
                    b = rows[j + 1]['count']
                    swap = (a < b) if descending else (a > b)
                    if swap:
                        rows[j], rows[j+1] = rows[j+1], rows[j]
            
            # Recalcular acumulados luego del ordenamiento
            running = 0
            for i in range(0, self._longitud(rows)):
                running = running + rows[i]['count']
                rows[i]['cumulative'] = running

        return rows

    def modes(self, columna: str):
        lista = self._obtener_lista(columna)
        counts = self._frecuencias_de_lista(lista)
        if not counts:
            return []
            
        max_count = 0
        for v in counts:
            if counts[v] > max_count:
                max_count = counts[v]
        
        if max_count <= 1 and self._longitud(lista) > 1:
            return [] # Amodal

        result = []
        for v in counts:
            if counts[v] == max_count:
                result.append(v)
        return result

    def moda(self, columna: str):
        mods = self.modes(columna)
        if len(mods) == 1:
            return mods[0] # Unimodal
        elif mods:
            return mods # Multimodal
        return None # Amodal

    def mode_type(self, columna: str):
        c = self._longitud(self.modes(columna))
        if c == 0:
            return "Amodal"
        elif c == 1:
            return "Unimodal"
        elif c == 2:
            return "Bimodal"
        else:
            return "Multimodal"

    def relative_frequencies(self, columna: str):
        lista = self._obtener_lista(columna)
        counts = self._frecuencias_de_lista(lista)
        total = self._longitud(lista)
        rel = {}
        if total == 0:
            return rel
            
        for v in counts:
            rel[v] = counts[v] / total
        return rel

    def summary(self, columna: str, include_table=True, sort_table_by_count=False):
        lista = self._obtener_lista(columna)
        total = self._longitud(lista)
        counts = self._frecuencias_de_lista(lista)
        unique = self._longitud(counts)
        
        res = {
            'variable': columna,
            'n': total,
            'unique': unique,
            'modes': self.modes(columna),
            'mode_type': self.mode_type(columna)
        }
        if include_table:
            res['frequency_table'] = self.build_frequency_table(
                columna, 
                sort_by_count=sort_table_by_count
            )
        return res
