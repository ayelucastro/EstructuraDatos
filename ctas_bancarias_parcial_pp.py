class CuentaBancaria:

    def __init__ (self, numero, nombre):
        self.cuenta = numero
        self.titular = nombre
        self.saldo = 0

#depositar plata
    def depositar(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto

#extraer plata. El saldo puede quedar en negativo.
    def extraer (self, monto):
        self.saldo = self.saldo - monto

#transferencia bancaria a otra cuenta
    def transferencia (self, cuenta2, monto):   
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            cuenta2.saldo = cuenta2.saldo + monto
            print ('Transferencia ok!')
        else: 
            print ('No se puede efectuar la transacción')

#obtener estado de la cuenta
#informa 'Su saldo es acreedor' si el saldo es mayor o igual a 0 y 'Su saldo es deudor' en caso contrario
    def estadoCuenta (self):
        if self.saldo >= 0:
            print ('Su saldo es acreedor')
        else: 
            print ('Su saldo es deudor')

    def imprimirDatos (self):
        print (f'{self.titular} , titular de la cuenta {self.cuenta} , tiene un saldo de $ {self.saldo}')



#programa principal
 
cuenta1 = CuentaBancaria (123, 'Juan Perez')
cuenta1.depositar (1000)
cuenta1.extraer (1250)
cuenta1.imprimirDatos ()
cuenta1.estadoCuenta ()


cuenta2 = CuentaBancaria (456, 'Roberto Gomez')
cuenta2.depositar (3500)
cuenta2.extraer (1800)
cuenta2.imprimirDatos ()
cuenta2.estadoCuenta ()


cuenta2.transferencia (cuenta1 , 600)
cuenta1.imprimirDatos ()
cuenta1.estadoCuenta ()
cuenta2.imprimirDatos ()
cuenta2.estadoCuenta ()