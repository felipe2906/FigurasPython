import math

class Punto:
  def __init__(self,x,y):
   self.x = x
   self.y = y

  def hallarDistancia(self,Punto):
        distancia=math.sqrt(math.pow(self.x- Punto.x,2)+math.pow(self.y-Punto.y,2))
        return distancia




