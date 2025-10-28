import math

class Cuantitativos:
    """
    Calcula estadísticas descriptivas para variables cuantitativas
    utilizando únicamente Lógica Pura
    """

    def __init__(self, data: list):
        """
        El constructor de la clase.
        Prepara los datos y pre-calcula la media.
        """
        # Limpieza y ordenamiento de los datos 
        self.datos = sorted([num for num in data if isinstance(num, (int, float))])
        
        if not self.datos:
            raise ValueError("La lista no contiene datos numéricos válidos.")
            
        self.n = len(self.datos)
        
        # Pre-cálculo de la Media
        suma_total = 0
        for num in self.datos:
            suma_total += num
        
        # Guardamos la media calculada 
        self.media_calculada = suma_total / self.n

    # --- Media ---
    def calcular_media(self):
        """
        Devuelve la media de los datos.
        """
        return self.media_calculada
