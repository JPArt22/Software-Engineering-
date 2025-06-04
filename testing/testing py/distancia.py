import math
import unittest

def calcular_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if not (isinstance(p1, tuple) and isinstance(p2, tuple)):
        raise TypeError("Ambos argumentos deben ser tuplas")
    else:
        distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        return distancia

print(calcular_distancia((1, -3), (-4, 5)))  

class test_calcular_distancia(unittest.TestCase):
    def test_puntos_positivos(self):
        self.assertAlmostEqual(calcular_distancia((1, 3), (4, 5)), 3.605551275463989)
    def test_puntos_negativos(self):
        self.assertAlmostEqual(calcular_distancia((-1, -3), (-4, -5)), 3.605551275463989)
    def test_puntos_mixtos(self):
        self.assertAlmostEqual(calcular_distancia((1, -3), (-4, 5)), 9.433981132056603)

unittest.main()