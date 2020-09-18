import unittest
import Circulo
import math

from Circulo import Circulo
from Punto import Punto


class Test(unittest.TestCase):
    def testDeterminarDentroCirculo(self):
         centro=Punto(1,2)
         r=3
         c1=Circulo(centro,r)
         p2=Punto(2,3)
         self.assertEqual(True,c1.determinarDentroCirculo(p2))

    def testHallarArea(self):
         centro=Punto(1,2)
         r=3
         c1=Circulo(centro,r)
         self.assertEqual(9*math.pi,c1.hallarArea())

    def testHallarPerimetro(self):
         centro=Punto(1,2)
         r=3
         c1=Circulo(centro,r)
         self.assertEqual(6*math.pi,c1.hallarPerimetro())
        
if __name__ == '__main__':
    unittest.main()