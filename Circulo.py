import math
from Punto import Punto
class Circulo:
  def __init__(self,Punto,radio):
   self.centro = Punto
   self.radio=radio

  def determinarDentroCirculo(self,Punto):
     
        distanciaCp=self.centro.hallarDistancia(Punto)
        if distanciaCp<=self.radio:
            result=True
        else :
            result=False
        return result
    
  def hallarPerimetro(self):
        perimetro=2*math.pi*self.radio
        return perimetro
    

  def hallarArea(self):
        area=math.pi*math.pow(self.radio,2)
        return area
    



centro=Punto(2,3)
r=4
c1=Circulo(centro,r)
p2=Punto(-2,3)
print((c1.hallarPerimetro()))
print((c1.hallarArea()))




