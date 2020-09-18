import unittest
import Rectangulo

from Punto import Punto
from Rectangulo import Rectangulo


class Test(unittest.TestCase):

    def testHallarArea(self):
         p1=Punto(-1,2)
         p2=Punto(2,2)    
         p3=Punto(2,0)    
         p4=Punto(-1,0)
         R=Rectangulo(p1,p2,p3,p4)
         self.assertEqual(6,R.hallarArea())

    def testHallarPerimetro(self):
         p1=Punto(-1,2)
         p2=Punto(2,2)    
         p3=Punto(2,0)    
         p4=Punto(-1,0)
         R=Rectangulo(p1,p2,p3,p4)
         self.assertEqual(10,R.hallarPerimetro())
        
if __name__ == '__main__':
    unittest.main()