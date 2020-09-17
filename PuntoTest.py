import unittest
import Punto

from Punto import Punto


class Test(unittest.TestCase):
    def test(self):
         p1=Punto(1,0)
         p2=Punto(-1,0)
         distancia=p1.hallarDistancia(p2)
         self.assertEqual(2,distancia)
        
if __name__ == '__main__':
    unittest.main()