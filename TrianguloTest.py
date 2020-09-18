import unittest
import Triangulo
import math

from Triangulo import Triangulo
from Punto import Punto


class Test(unittest.TestCase):
    def testDeterminarTiporiangulo(self):
         p1=Punto(-1,1)
         p2=Punto(1,0)    
         p3=Punto(-1,0) 
         t=Triangulo(p1,p2,p3)  
         self.assertEqual("Escaleno",t.determinarTipoTriangulo())

    def testHallarPerimetro(self):
         p1=Punto(-1,1)
         p2=Punto(1,0)    
         p3=Punto(-1,0) 
         t=Triangulo(p1,p2,p3)  
         self.assertEqual(5.23606797749979,t.hallarPerimetro())

    def testHallarArea(self):
         p1=Punto(0,3)
         p2=Punto(1,0)    
         p3=Punto(-1,0) 
         t=Triangulo(p1,p2,p3) 
         self.assertEqual(3.0000000000000004,t.hallarArea())
        
if __name__ == '__main__':
    unittest.main()