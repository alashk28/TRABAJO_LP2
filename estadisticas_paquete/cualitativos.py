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