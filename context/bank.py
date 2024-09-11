class Banco:
  def __init__(self):
      self.__cuentas = {}

  def agregar_cuenta(self, xcuenta):
      self.__cuentas[xcuenta.obtener_numero_cuenta()] = xcuenta

  def obtner_cuenta(self, xnumero_cuenta):
      return self.__cuentas.get(xnumero_cuenta)

