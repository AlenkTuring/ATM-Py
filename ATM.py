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
        else:
            return False

    def obtener_saldo(self):
        return self.__saldo

    def transferir(self, xcuenta_destino, xcantidad):
        if self.retirar(xcantidad):
            xcuenta_destino.depositar(xcantidad)
            return True
        else:
            return False

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta


class Banco:
    def __init__(self):
        self.__cuentas = {}

    def agregar_cuenta(self, xcuenta):
        self.__cuentas[xcuenta.obtener_numero_cuenta()] = xcuenta

    def obtner_cuenta(self, xnumero_cuenta):
        return self.__cuentas.get(xnumero_cuenta)


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
        if self.__cuenta_actual:
            xcuenta_destino = self.__banco.obtner_cuenta(xnumero_cuenta_destino)

            if xcuenta_destino:
                if self.__cuenta_actual.transferir(xcuenta_destino, xcantidad):
                    print("Se han transferido ",xcantidad)
                else:
                    print("Fondos insuficientes")
            else:
                print("Cuenta destino no encontrada")


xbanco = Banco()

xbanco.agregar_cuenta(Cuenta(xnumero_cuenta=1234,xpin=5678,xsaldo=1000))
xbanco.agregar_cuenta(Cuenta(xnumero_cuenta=7412,xpin=4321,xsaldo=500))


xcajero = CajeroAutomatico(xbanco)

if xcajero.autenticar_usuario(xnumero_cuenta=1234,xpin=5678):
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
    else:
        print("Autenticación fallida")
            
     

                
                
    

    
        
            
        

    
            
        
    



        
        
            
        



    
        
       


    

        
