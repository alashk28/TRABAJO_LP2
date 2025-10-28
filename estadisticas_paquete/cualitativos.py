class Cualitativos:
    """Clase para estadísticas cualitativas (esqueleto inicial)."""
    pass
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
        """Devuelve diccionario {valor: conteo}."""
        frec = {}
        for valor in self.datos:
            if valor in frec:
                frec[valor] = frec[valor] + 1
            else:
                frec[valor] = 1
        return frec

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

    def build_frequency_table(self):
        """
        Devuelve lista de filas: {'value': v, 'count': c, 'relative': r, 'cumulative': None}
        (aún no calcula acumulados)
        """
        counts = self._frecuencias()
        total = self._contar_elementos()
        rows = []
        for v in counts:
            c = counts[v]
            rel = c / total if total != 0 else 0
            row = {'value': v, 'count': c, 'relative': rel, 'cumulative': None}
            rows.append(row)
        self._tabla = rows
        return rows

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

    def build_frequency_table(self):
        """Devuelve lista de filas con acumulados calculados.
        El orden actual es el orden de aparición de las categorías"""
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

        self._tabla = rows
        return rows

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
        """Devuelve tabla con acumulados; si sort_by_count=True hace bubble sort por 'count'."""
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
            running = 0
            for i in range(0, self._longitud(rows)):
                running = running + rows[i]['count']
                rows[i]['cumulative'] = running

        self._tabla = rows
        return rows


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
        running = 0
        for i in range(0, self._longitud(rows)):
            running = running + rows[i]['count']
            rows[i]['cumulative'] = running

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
            running = 0
            for i in range(0, self._longitud(rows)):
                running = running + rows[i]['count']
                rows[i]['cumulative'] = running

        self._tabla = rows
        return rows

    def modes(self):
        """Devuelve lista con la(s) moda(s)."""
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
        running = 0
        for i in range(0, self._longitud(rows)):
            running = running + rows[i]['count']
            rows[i]['cumulative'] = running

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
        """Devuelve tipo: 'Amodal', 'Unimodal', 'Bimodal' o 'Multimodal'."""
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
        """Retorna dict {valor: relativa (0..1)}"""
        counts = self._frecuencias()
        total = self._contar_elementos()
        rel = {}
        for v in counts:
            rel[v] = counts[v] / total if total != 0 else 0
        return rel


