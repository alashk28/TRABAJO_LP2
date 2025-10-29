class Cualitativos:
    """
    Clase para estadísticas cualitativas.
    Métodos:
      - build_frequency_table(sort_by_count=False)
      - modes()
      - moda(columna=None)  # alias en español
      - mode_type()
      - relative_frequencies()
      - summary(include_table=True, sort_table_by_count=False)
      - add(value), extend(iterable)
      - __str__()
    """

    def __init__(self, datos=None, nombre="Variable_Cualitativa"):
        self.nombre = nombre
        self.datos = []
        if datos is not None:
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

    def _contar_elementos(self):
        return self._longitud(self.datos)

    def _frecuencias(self):
        frec = {}
        for valor in self.datos:
            if valor in frec:
                frec[valor] = frec[valor] + 1
            else:
                frec[valor] = 1
        return frec

    # ---------- tabla de frecuencias ----------
    def build_frequency_table(self, sort_by_count=False, descending=True):
        """
        Retorna lista de filas: {'value', 'count', 'relative', 'cumulative'}.
        Si sort_by_count=True aplica un bubble sort primitivo por 'count'.
        """
        counts = self._frecuencias()
        total = self._contar_elementos()
        rows = []
        for v in counts:
            c = counts[v]
            rel = c / total if total != 0 else 0
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
            
            running = 0
            for i in range(0, self._longitud(rows)):
                running = running + rows[i]['count']
                rows[i]['cumulative'] = running

        self._tabla = rows
        return rows

    # ---------- moda(s) ----------
    def modes(self):
        """Devuelve lista con la(s) moda(s)."""
        if self._modas is not None:
            return self._modas
        counts = self._frecuencias()
        if not counts:
            self._modas = []
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
        self._modas = result
        return result

    def moda(self, columna=None):
        """
        Alias en español para modes().
        """
        return self.modes()

    def mode_type(self):
        """Devuelve 'Amodal', 'Unimodal', 'Bimodal' o 'Multimodal'."""
        mods = self.modes()
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
    def relative_frequencies(self):
        """Retorna diccionario {valor: proporción (0..1)}."""
        counts = self._frecuencias()
        total = self._contar_elementos()
        rel = {}
        for v in counts:
            rel[v] = counts[v] / total if total != 0 else 0
        return rel

    # ---------- resumen y modificaciones ----------
    def summary(self, include_table=True, sort_table_by_count=False):
        """Devuelve diccionario resumen con info solicitada."""
        total = self._contar_elementos()
        counts = self._frecuencias()
        unique = 0
        for _ in counts:
            unique = unique + 1
        res = {
            'variable': self.nombre,
            'n': total,
            'unique': unique,
            'modes': self.modes(),
            'mode_type': self.mode_type()
        }
        if include_table:
            res['frequency_table'] = self.build_frequency_table(sort_by_count=sort_table_by_count)
        return res

    def add(self, value):
        """Añade un valor y limpia caches."""
        self.datos.append(value)
        self._tabla = None
        self._modas = None

    def extend(self, iterable):
        for x in iterable:
            self.datos.append(x)
        self._tabla = None
        self._modas = None

    # ---------- representación ----------
    def __str__(self):
        total = self._contar_elementos()
        counts = self._frecuencias()
        unique = 0
        for _ in counts:
            unique = unique + 1
        return "<Cualitativos variable='{}' n={} categories={}>".format(
            self.nombre, total, unique
        )
        