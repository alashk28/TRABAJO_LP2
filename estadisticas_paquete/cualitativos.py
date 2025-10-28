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

