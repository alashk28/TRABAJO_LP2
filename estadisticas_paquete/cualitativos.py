from .stats_base import Estadisticos

class Cualitativos(Estadisticos): 
    def __init__(self, ruta_csv):
        super().__init__(ruta_csv) 
    
    pass