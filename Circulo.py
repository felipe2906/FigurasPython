import math
from Punto import Punto
from Figura import Figura
class Circulo(Figura):
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
    








