import pandas as pd

class Cualitativos:
    """
    Clase para estadísticas cualitativas.
    Soporta:
      - Inicializar con lista/iterable: Cualitativos(['F','M',...])
      - Inicializar con DataFrame: Cualitativos(df)
        y luego usar métodos indicando columna: moda('Sexo'), summary(columna='Sexo')
    """

    def __init__(self, datos=None, nombre="Variable_Cualitativa"):
        self.nombre = nombre
        self.datos = []
        self._df = None
        if datos is not None:
            if isinstance(datos, pd.DataFrame):
                self._df = datos
            else:
                for x in datos:
                    self.datos.append(x)
        self._tabla = None
        self._modas = None

    # ---------- utilidades primarias ----------
    def _longitud(self, iterable):
        c = 0
        for _ in iterable:
            c = c + 1
        return c

    def _es_nan(self, valor):
        """Detecta si un valor es NaN sin usar math ni numpy."""
        try:
    
            return valor != valor
        except Exception:
            return False

    def _obtener_lista(self, columna=None):
        """
        Devuelve la lista de valores sobre la cual operar.
        Si se inicializó con DataFrame, se debe pasar el nombre de la columna.
        """
        if self._df is not None:
            if columna is None:
                raise ValueError("La instancia fue creada con un DataFrame; debe indicar 'columna'.")
            if columna not in list(self._df.columns):
                raise KeyError(f"Columna '{columna}' no encontrada. Columnas: {list(self._df.columns)}")

            serie = self._df[columna].tolist()
            lista = []
            for v in serie:
                if v is None or self._es_nan(v):
                    lista.append("Missing")
                else:
                    lista.append(str(v).strip())
            return lista
        else:
            return self.datos

    def _frecuencias(self, lista):
        frec = {}
        for valor in lista:
            if valor in frec:
                frec[valor] = frec[valor] + 1
            else:
                frec[valor] = 1
        return frec

    # ---------- tabla de frecuencias ----------
    def build_frequency_table(self, sort_by_count=False, descending=True, columna=None):
        lista = self._obtener_lista(columna)
        counts = self._frecuencias(lista)
        total = self._longitud(lista)
        rows = []

        for v in counts:
            c = counts[v]
            rel = c / total if total != 0 else 0
            row = {'value': v, 'count': c, 'relative': rel, 'cumulative': None}
            rows.append(row)

        # acumulada
        running = 0
        for i in range(0, self._longitud(rows)):
            running = running + rows[i]['count']
            rows[i]['cumulative'] = running

        # ordenamiento burbuja
        if sort_by_count:
            n = self._longitud(rows)
            for i in range(0, n):
                for j in range(0, n - 1 - i):
                    a = rows[j]['count']
                    b = rows[j + 1]['count']
                    swap = False
                    if descending and a < b:
                        swap = True
                    elif not descending and a > b:
                        swap = True
                    if swap:
                        tmp = rows[j]
                        rows[j] = rows[j + 1]
                        rows[j + 1] = tmp
            running = 0
            for i in range(0, self._longitud(rows)):
                running = running + rows[i]['count']
                rows[i]['cumulative'] = running

        self._tabla = rows
        return rows

    # ---------- moda(s) ----------
    def modes(self, columna=None):
        lista = self._obtener_lista(columna)
        counts = self._frecuencias(lista)
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
        """Alias en español para modes()."""
        return self.modes(columna)

    def mode_type(self, columna=None):
        mods = self.modes(columna)
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
        lista = self._obtener_lista(columna)
        counts = self._frecuencias(lista)
        total = self._longitud(lista)
        rel = {}
        for v in counts:
            rel[v] = counts[v] / total if total != 0 else 0
        return rel

    # ---------- resumen ----------
    def summary(self, include_table=True, sort_table_by_count=False, columna=None):
        lista = self._obtener_lista(columna)
        total = self._longitud(lista)
        counts = self._frecuencias(lista)
        unique = 0
        for _ in counts:
            unique = unique + 1
        res = {
            'variable': columna if columna is not None else self.nombre,
            'n': total,
            'unique': unique,
            'modes': self.modes(columna),
            'mode_type': self.mode_type(columna)
        }
        if include_table:
            res['frequency_table'] = self.build_frequency_table(sort_by_count=sort_table_by_count, columna=columna)
        return res

    # ---------- modificación manual ----------
    def add(self, value):
        if self._df is not None:
            raise RuntimeError("No se puede usar add() con DataFrame.")
        self.datos.append(value)
        self._tabla = None
        self._modas = None

    def extend(self, iterable):
        if self._df is not None:
            raise RuntimeError("No se puede usar extend() con DataFrame.")
        for x in iterable:
            self.datos.append(x)
        self._tabla = None
        self._modas = None

    # ---------- representación ----------
    def __str__(self):
        if self._df is not None:
            cols = list(self._df.columns)
            return "<Cualitativos DataFrame cols={} rows={}>".format(cols, self._df.shape[0])
        total = self._longitud(self.datos)
        counts = self._frecuencias(self.datos)
        unique = 0
        for _ in counts:
            unique = unique + 1
        return "<Cualitativos variable='{}' n={} categories={}>".format(
            self.nombre, total, unique
        )

