from Punto import Punto
class Rectangulo:
  def __init__(self,p1=Punto,p2=Punto,p3=Punto,p4=Punto):
   self.p1=p1
   self.p2=p2
   self.p3=p3
   self.p4=p4

  def hallarPerimetro(self):
         distanciap1p2=self.p1.hallarDistancia(self.p2)
         distanciap2p3=self.p2.hallarDistancia(self.p3)
         distanciap3p4=self.p3.hallarDistancia(self.p4)
         distanciap4p1=self.p4.hallarDistancia(self.p1)
         perimetro=distanciap1p2+distanciap2p3+distanciap4p1+distanciap3p4
         return perimetro
    

  def hallarArea(self):
         distanciap1p2=self.p1.hallarDistancia(self.p2)
         distanciap2p3=self.p2.hallarDistancia(self.p3)
         area=distanciap1p2*distanciap2p3
         return area

   

p1=Punto(-1,2)
p2=Punto(2,2)    
p3=Punto(2,0)    
p4=Punto(-1,0)
R=Rectangulo(p1,p2,p3,p4)   
print(R.hallarPerimetro())
print(R.hallarArea())  