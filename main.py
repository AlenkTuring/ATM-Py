from services.account import Cuenta
from services.automatic_cashier import CajeroAutomatico
from context.bank import Banco
from getpass import getpass
from sys import exit
xbanco = Banco()

xbanco.agregar_cuenta(Cuenta(xnumero_cuenta=1234,xpin=5678,xsaldo=1000))
xbanco.agregar_cuenta(Cuenta(xnumero_cuenta=7412,xpin=4321,xsaldo=500))

xcajero = CajeroAutomatico(xbanco)

def main():

  is_authenticated = False
  tries = 0

  while not is_authenticated and tries < 3:
    print("Autenticación fallida" if tries else "Bienvenido al banco de Alenka" )
    numero_cuenta = int(input("Ingrese su número de cuenta \n"))
    pin = int(getpass("Ingrese su pin (no se mostrará por seguridad en pantalla) \n"))
    is_authenticated = xcajero.autenticar_usuario(xnumero_cuenta=numero_cuenta,xpin=pin)
    tries += 1

  if tries >= 3 and not is_authenticated:
    print("Ha excedido el número de intentos permitidos")
    return exit(1)


  while True:
    opcion = xcajero.mostrar_menu()
    if opcion == '1':
      xcajero.consultar_saldo()
    elif opcion == '2':
      xcantidad = float(input("Ingrese la cantidad a depositar: "))
      xcajero.depositar(xcantidad)
    elif opcion == '3':
      xcantidad = float(input("Ingrese la cantidad a retirar: "))
      xcajero.retirar(xcantidad)
    elif opcion == '4':
      xnumero_cuenta_destino = int(input("Ingrese la cuenta destino: "))
      xcantidad = float(input("Ingrese la cantidad a transferir: "))
      xcajero.transferir(xnumero_cuenta_destino, xcantidad)
    elif opcion == '5':
      break
    else:
      print("Opción no válida")


if __name__ == "__main__":
    main()
