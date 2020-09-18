import math
from Punto import Punto
class Triangulo:
  def __init__(self,p1=Punto,p2=Punto,p3=Punto):
    self.p1=p1
    self.p2=p2
    self.p3=p3

  def determinarTipoTriangulo(self):
        distanciap1p2=self.p1.hallarDistancia(self.p2)
        distanciap2p3=self.p2.hallarDistancia(self.p3)
        distanciap3p1=self.p3.hallarDistancia(self.p1)
        tipo=""
        if (distanciap1p2==distanciap2p3 and distanciap2p3==distanciap3p1):
            tipo="Equilatero"
        elif(distanciap1p2==distanciap3p1 and distanciap2p3!=distanciap3p1  ):
            tipo="Isoceles"
        else:
            tipo="Escaleno"
        return tipo
    
  def hallarPerimetro(self):
        distanciap1p2=self.p1.hallarDistancia(self.p2)
        distanciap2p3=self.p2.hallarDistancia(self.p3)
        distanciap3p1=self.p3.hallarDistancia(self.p1)
        perimetro=distanciap1p2+distanciap2p3+distanciap3p1
        return perimetro

  def hallarArea(self):
        tipo=self.determinarTipoTriangulo()
        area=0
        distanciap1p2=self.p1.hallarDistancia(self.p2)
        distanciap2p3=self.p2.hallarDistancia(self.p3)
        distanciap3p1=self.p3.hallarDistancia(self.p1)
        if (tipo=="Equilatero"):
            area=(distanciap1p2*math.pow(3,1/3))/4
        elif(tipo=="Isoceles"):
            altura=math.sqrt((math.pow(distanciap1p2,2))-(math.pow(distanciap2p3,2)/4))
            area=(distanciap2p3*altura)/(2)
        else:
            s=(distanciap1p2+distanciap2p3+distanciap3p1)/2
            area=math.sqrt(s*(s-distanciap1p2)*(s-distanciap2p3)*s-distanciap3p1)
        
        return area


