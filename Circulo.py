
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
    

centro=Punto(2,3)
r=4
c1=Circulo(centro,r)
p2=Punto(-2,3)
print(str(c1.determinarDentroCirculo(p2)))




