# estadisticas_paquete/cuantitativos.py
# Versión retrocompatible: acepta DataFrame, ruta (csv) o lista.
# Implementación "primitiva" (solo lógica básica, sin math import)

import pandas as pd
import os

class Cuantitativos:
    """
    Clase para estadísticas cuantitativas.
    """

    def __init__(self, data):
        # Guardamos una referencia interna. Si es ruta, intentamos leer CSV.
        self._df = None
        self._lista = None

        # Si le pasaron una cadena que existe como ruta, intentar leer CSV
        if isinstance(data, str) and os.path.exists(data):
            try:
                self._df = pd.read_csv(data, encoding='utf-8-sig')
            except Exception:
                # fallback: intentar sin especificar encoding
                self._df = pd.read_csv(data)
            return

        # Si es un DataFrame
        if isinstance(data, pd.DataFrame):
            self._df = data
            return

        # Si es iterable (lista) de números
        try:
            lista = []
            for x in data:
                # filtrar por int/float (aceptar strings convertibles opcionalmente)
                if isinstance(x, (int, float)):
                    lista.append(x)
                else:
                    # intentar convertir si es string que representa número
                    try:
                        val = float(str(x).strip())
                        lista.append(val)
                    except Exception:
                        # ignorar valores no numéricos
                        pass
            if not lista:
                raise ValueError("No hay datos numéricos válidos en la lista.")
            # ordenar primitivo
            # implementar ordenamiento simple (bubble sort) para mantener primitivo
            n = 0
            for _ in lista:
                n += 1
            # bubble sort
            for i in range(0, n):
                for j in range(0, n - 1 - i):
                    if lista[j] > lista[j+1]:
                        tmp = lista[j]
                        lista[j] = lista[j+1]
                        lista[j+1] = tmp
            self._lista = lista
            # precálculos
            self.n = 0
            suma = 0
            for v in lista:
                self.n += 1
                suma += v
            self.media_calculada = suma / self.n if self.n != 0 else 0.0
            return
        except TypeError:
            raise ValueError("Tipo de dato para Cuantitativos no soportado. Pase lista, DataFrame o ruta CSV.")

    # Util: obtener lista numérica a partir del estado y una columna opcional
    def _obtener_lista(self, columna=None):
        if self._df is not None:
            if columna is None:
                raise ValueError("Instancia creada con DataFrame: debe indicar 'columna'.")
            # intentar convertir columna a numérico (coerce)
            serie = self._df[columna].tolist()
            lista = []
            for v in serie:
                try:
                    if isinstance(v, (int, float)):
                        lista.append(v)
                    else:
                        lista.append(float(str(v).strip()))
                except Exception:
                    # ignorar no convertibles
                    pass
            if not lista:
                raise ValueError(f"No hay datos numéricos en la columna '{columna}'.")
            # ordenar primitivo (burbuja)
            n = 0
            for _ in lista:
                n += 1
            for i in range(0, n):
                for j in range(0, n - 1 - i):
                    if lista[j] > lista[j+1]:
                        tmp = lista[j]
                        lista[j] = lista[j+1]
                        lista[j+1] = tmp
            return lista
        else:
            if self._lista is None:
                raise RuntimeError("No hay datos disponibles.")
            return list(self._lista)  # copia segura

    # media
    def media(self, columna=None):
        lista = self._obtener_lista(columna)
        n = 0
        suma = 0
        for v in lista:
            n += 1
            suma += v
        return suma / n if n != 0 else 0.0

    # mediana
    def mediana(self, columna=None):
        lista = self._obtener_lista(columna)
        n = 0
        for _ in lista:
            n += 1
        if n == 0:
            return None
        mid = n // 2
        if n % 2 == 1:
            return lista[mid]
        else:
            return (lista[mid - 1] + lista[mid]) / 2

    # varianza (muestral por defecto)
    def varianza(self, columna=None, es_muestra=True):
        lista = self._obtener_lista(columna)
        n = 0
        suma = 0
        for v in lista:
            n += 1
            suma += v
        if n == 0:
            return 0.0
        media = suma / n
        suma_diff = 0
        for v in lista:
            suma_diff += (v - media) ** 2
        denom = (n - 1) if es_muestra and n > 1 else n
        return suma_diff / denom if denom != 0 else 0.0

    # desviación estándar (muestral por defecto)
    def desviacion_estandar(self, columna=None, es_muestra=True):
        var = self.varianza(columna=columna, es_muestra=es_muestra)
        return var ** 0.5  # sqrt primitivo

    # alias y compatibilidad con nombres antiguos
    def calcular_media(self):
        return self.media()

    def calcular_mediana(self):
        return self.mediana()

    def calcular_varianza(self, es_muestra=True):
        return self.varianza(es_muestra=es_muestra)

    def calcular_desviacion_estandar(self, es_muestra=True):
        return self.desviacion_estandar(es_muestra=es_muestra)
