
class Cualitativos:
    """Clase para estadísticas cualitativas."""

    def __init__(self, datos=None, nombre="Variable_Cualitativa"):
        self.nombre = nombre
        self.datos = []
        if datos is not None:
            for x in datos:
                self.datos.append(x)
        self._tabla = None
        self._modas = None

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

    def build_frequency_table(self, sort_by_count=False, descending=True):
        counts = self._frecuencias()
        total = self._contar_elementos()
        rows = []
        for v in counts:
            c = counts[v]
            rel = c / total if total != 0 else 0
            row = {'value': v, 'count': c, 'relative': rel, 'cumulative': None}
            rows.append(row)

        # Primero, calcular acumulados en el orden de aparición
        running = 0
        for i in range(0, self._longitud(rows)):
            running = running + rows[i]['count']
            rows[i]['cumulative'] = running

        # Segundo, ordenar si se solicita (Bubble Sort)
        if sort_by_count:
            n = self._longitud(rows)
            for i in range(0, n):
                for j in range(0, n - 1 - i):
                    a = rows[j]['count']
                    b = rows[j+1]['count']
                    swap = False
                    if descending:
                        if a < b:
                            swap = True
                    else:
                        if a > b:
                            swap = True
                    if swap:
                        tmp = rows[j]
                        rows[j] = rows[j+1]
                        rows[j+1] = tmp

            # Tercero, recalcular acumulados DESPUÉS de ordenar
            running = 0
            for i in range(0, self._longitud(rows)):
                running = running + rows[i]['count']
                rows[i]['cumulative'] = running

        self._tabla = rows
        return rows

    def modes(self):
        counts = self._frecuencias()
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
        self._modas = result
        return result

    def mode_type(self):
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

    def relative_frequencies(self):
        counts = self._frecuencias()
        total = self._contar_elementos()
        rel = {}
        for v in counts:
            rel[v] = counts[v] / total if total != 0 else 0
        return rel

    def summary(self, include_table=True, sort_table_by_count=False):
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
            res['frequency_table'] = self.build_frequency_table(sort_table_by_count=sort_table_by_count)
        return res

    def add(self, value):
        self.datos.append(value)
        self._tabla = None
        self._modas = None

    def extend(self, iterable):
        for x in iterable:
            self.datos.append(x)
        self._tabla = None
        self._modas = None

    def __str__(self):
        total = self._contar_elementos()
        counts = self._frecuencias()
        unique = 0
        for _ in counts:
            unique = unique + 1
        return "<Cualitativos variable='{}' n={} categories={}>".format(
            self.nombre, total, unique
        )