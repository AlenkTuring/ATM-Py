class Cuenta:
  def __init__(self,xnumero_cuenta,xpin,xsaldo=0):
    self.__numero_cuenta = xnumero_cuenta
    self.__pin = xpin
    self.__saldo = xsaldo

  def verificar_pin(self,xpin):
    return self.__pin == xpin

  def depositar(self, xcantidad):
    self.__saldo += xcantidad

  def retirar(self, xcantidad):
    if self.__saldo >= xcantidad:
      self.__saldo -= xcantidad
      return True

    return False

  def obtener_saldo(self):
    return self.__saldo

  def transferir(self, xcuenta_destino, xcantidad):
    if self.retirar(xcantidad):
      xcuenta_destino.depositar(xcantidad)
      return True

    return False

  def obtener_numero_cuenta(self):
    return self.__numero_cuenta
