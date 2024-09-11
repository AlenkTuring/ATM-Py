
class CajeroAutomatico:
  def __init__(self, xbanco):
    self.__banco = xbanco
    self.cuenta_actual = None

  def autenticar_usuario(self, xnumero_cuenta, xpin):
    cuenta = self.__banco.obtner_cuenta(xnumero_cuenta)
    if cuenta and cuenta.verificar_pin(xpin):
        self.__cuenta_actual = cuenta
        return True
    else:
        return False

  def mostrar_menu(self):
    if self.__cuenta_actual:
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Transferir")
        print("5. Salir")
        print("-"*50)
        opcion = input("Elija una opción:")
        return opcion
    else:
        print("No hay usuario autenticado")
        return None

  def depositar(self, xcantidad):
    if self.__cuenta_actual:
        self.__cuenta_actual.depositar(xcantidad)
        print("Se han depositado ",xcantidad)

  def retirar(self, xcantidad):
    if self.__cuenta_actual.retirar(xcantidad):
        print("Se han retirado ",xcantidad)
    else:
        print("Fondos insuficientes")

  def consultar_saldo(self):
    if self.__cuenta_actual:
        saldo = self.__cuenta_actual.obtener_saldo()
        print("Su saldo es",saldo)

  def transferir(self, xnumero_cuenta_destino, xcantidad):
    if not self.__cuenta_actual:
       return

    xcuenta_destino = self.__banco.obtner_cuenta(xnumero_cuenta_destino)

    if xcuenta_destino:
      if self.__cuenta_actual.transferir(xcuenta_destino, xcantidad):
        print("Se han transferido ",xcantidad)
      else:
        print("Fondos insuficientes")
    else:
      print("Cuenta destino no encontrada")
