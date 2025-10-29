import math
import pandas as pd

class Cualitativos:
    """
    Clase para estadísticas cualitativas (implementación primitiva).
    Soporta:
      - Inicializar con lista/iterable de valores: Cualitativos(['a','b',...])
      - Inicializar con DataFrame: Cualitativos(df)
        y luego usar métodos indicando columna: moda('Sexo'), summary(columna='Sexo')
    Métodos (todos aceptan opcionalmente `columna`):
      - build_frequency_table(sort_by_count=False, columna=None)
      - modes(columna=None)
      - moda(columna=None)  # alias en español
      - mode_type(columna=None)
      - relative_frequencies(columna=None)
      - summary(include_table=True, sort_table_by_count=False, columna=None)
      - add(value), extend(iterable)  (sólo si se usó lista)
      - __str__()
    """

    def __init__(self, datos=None, nombre="Variable_Cualitativa"):
        self.nombre = nombre
        self.datos = []
        self._df = None  # si el usuario pasa un DataFrame
        if datos is not None:
            # Si es DataFrame, lo guardamos
            if isinstance(datos, pd.DataFrame):
                self._df = datos
            else:
                # asumimos iterable de valores
                for x in datos:
                    self.datos.append(x)
        self._tabla = None
        self._modas = None

    # ---------- utilidades primarias (sin usar len/sum/etc) ----------
    def _longitud(self, iterable):
        c = 0
        for _ in iterable:
            c = c + 1
        return c

    def _contar_elementos_de_lista(self, lista):
        c = 0
        for _ in lista:
            c = c + 1
        return c

    def _frecuencias_de_lista(self, lista):
        frec = {}
        for valor in lista:
            if valor in frec:
                frec[valor] = frec[valor] + 1
            else:
                frec[valor] = 1
        return frec

    def _obtener_lista(self, columna=None):
        """
        Devuelve la lista de valores sobre la cual operar.
        - Si self._df no es None y columna es un nombre válido -> devuelve df[columna].tolist()
        - Si self._df es None -> devuelve self.datos (lista)
        - Si self._df no es None y columna es None -> error (pedir columna)
        """
        if self._df is not None:
            if columna is None:
                raise ValueError("La instancia fue creada con un DataFrame; debe indicar 'columna' en los métodos.")
            # verificar columna
            if columna not in list(self._df.columns):
                raise KeyError(f"Columna '{columna}' no encontrada en el DataFrame. Columnas disponibles: {list(self._df.columns)}")
            # obtener serie y normalizar NaN -> 'Missing', convertir todo a str
            serie = self._df[columna].tolist()
            lista = []
            for v in serie:
                try:
                    # pandas NaN detection
                    if isinstance(v, float) and math.isnan(v):
                        lista.append("Missing")
                        continue
                except Exception:
                    pass
                if v is None:
                    lista.append("Missing")
                else:
                    lista.append(str(v).strip())
            return lista
        else:
            # si no hay DataFrame, usamos la lista almacenada
            return self.datos

    # ---------- tabla de frecuencias ----------
    def build_frequency_table(self, sort_by_count=False, descending=True, columna=None):
        """
        Retorna lista de filas: {'value', 'count', 'relative', 'cumulative'}.
        Si se inicializó con DataFrame, debe pasarse columna.
        """
        lista = self._obtener_lista(columna=columna)
        counts = self._frecuencias_de_lista(lista)
        total = self._contar_elementos_de_lista(lista)
        rows = []
        for v in counts:
            c = counts[v]
            rel = c / total if total != 0 else 0
            row = {'value': v, 'count': c, 'relative': rel, 'cumulative': None}
            rows.append(row)

        # calcular acumulados en el orden actual
        running = 0
        for i in range(0, self._longitud(rows)):
            running = running + rows[i]['count']
            rows[i]['cumulative'] = running

        # ordenar si piden (burbuja primitiva)
        if sort_by_count:
            n = self._longitud(rows)
            for i in range(0, n):
                for j in range(0, n - 1 - i):
                    a = rows[j]['count']
                    b = rows[j + 1]['count']
                    swap = False
                    if descending:
                        if a < b:
                            swap = True
                    else:
                        if a > b:
                            swap = True
                    if swap:
                        tmp = rows[j]
                        rows[j] = rows[j + 1]
                        rows[j + 1] = tmp
            # recalcular acumulados luego del ordenamiento
            running = 0
            for i in range(0, self._longitud(rows)):
                running = running + rows[i]['count']
                rows[i]['cumulative'] = running

        self._tabla = rows
        return rows

    # ---------- moda(s) ----------
    def modes(self, columna=None):
        """Devuelve lista con la(s) moda(s)."""
        lista = self._obtener_lista(columna=columna)
        counts = self._frecuencias_de_lista(lista)
        if not counts:
            return []
        max_count = None
        for v in counts:
            c = counts[v]
            if max_count is None or c > max_count:
                max_count = c
        result = []
        for v in counts:
            if counts[v] == max_count:
                result.append(v)
        return result

    def moda(self, columna=None):
        """
        Alias en español para modes(). Acepta columna opcional para compatibilidad con tests.
        """
        return self.modes(columna=columna)

    def mode_type(self, columna=None):
        """Devuelve 'Amodal', 'Unimodal', 'Bimodal' o 'Multimodal'."""
        mods = self.modes(columna=columna)
        c = self._longitud(mods)
        if c == 0:
            return "Amodal"
        elif c == 1:
            return "Unimodal"
        elif c == 2:
            return "Bimodal"
        else:
            return "Multimodal"

    # ---------- frecuencias relativas ----------
    def relative_frequencies(self, columna=None):
        """Retorna diccionario {valor: proporción (0..1)}."""
        lista = self._obtener_lista(columna=columna)
        counts = self._frecuencias_de_lista(lista)
        total = self._contar_elementos_de_lista(lista)
        rel = {}
        for v in counts:
            rel[v] = counts[v] / total if total != 0 else 0
        return rel

    # ---------- resumen y modificaciones ----------
    def summary(self, include_table=True, sort_table_by_count=False, columna=None):
        """Devuelve diccionario resumen con info solicitada."""
        lista = self._obtener_lista(columna=columna)
        total = self._contar_elementos_de_lista(lista)
        counts = self._frecuencias_de_lista(lista)
        unique = 0
        for _ in counts:
            unique = unique + 1
        res = {
            'variable': columna if columna is not None else self.nombre,
            'n': total,
            'unique': unique,
            'modes': self.modes(columna=columna),
            'mode_type': self.mode_type(columna=columna)
        }
        if include_table:
            res['frequency_table'] = self.build_frequency_table(sort_by_count=sort_table_by_count, columna=columna)
        return res

    def add(self, value):
        """Añade un valor y limpia caches. (válido solo si se usó lista en __init__)"""
        if self._df is not None:
            raise RuntimeError("No puede usar add() cuando la instancia fue creada con un DataFrame.")
        self.datos.append(value)
        self._tabla = None
        self._modas = None

    def extend(self, iterable):
        if self._df is not None:
            raise RuntimeError("No puede usar extend() cuando la instancia fue creada con un DataFrame.")
        for x in iterable:
            self.datos.append(x)
        self._tabla = None
        self._modas = None

    # ---------- representación ----------
    def __str__(self):
        if self._df is not None:
            # si fue inicializado con DataFrame mostramos info mínima
            cols = list(self._df.columns)
            return "<Cualitativos DataFrame cols={} rows={}>".format(cols, self._df.shape[0])
        total = self._contar_elementos_de_lista(self.datos)
        counts = self._frecuencias_de_lista(self.datos)
        unique = 0
        for _ in counts:
            unique = unique + 1
        return "<Cualitativos variable='{}' n={} categories={}>".format(
            self.nombre, total, unique
        )

        