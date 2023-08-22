class Calculadora:

  def __init__(self,a,b):
    self.numero1=a
    self.numero=b
  def suma(self): 
    print(self.numero+self.numero1)
  def resta(self):
    print(self.numero-self.numero1)
  def multiplicacion(self):
    print(self.numero*self.numero1)
  def potencia(self):
    print(self.numero**self.numero1)
  def dividir(self):
    print(self.numero/self.numero1)