# Clase CuentaBancaria con saldo privado, ingresar, retirar (valida saldo suficiente) y propiedad saldo de solo lectura.


class SaldoInsuficiente(Exception):
    """Mensaje de error para saldo insuficiente"""

class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    def retirar(self, cantidad):
        if cantidad < self._saldo:
            self._saldo -= cantidad
            print("Saldo retirado: ", cantidad, ", saldo restante: ",self.saldo)
        else:
            raise SaldoInsuficiente("No puedes retirar una cantidad mayor a tu saldo")
    
cuenta = CuentaBancaria("Selu", 20)
print(cuenta.saldo)
try:
    cuenta.retirar(100)
except (SaldoInsuficiente) as e:
    print(str(e))
try:
    cuenta.retirar(10)
except (SaldoInsuficiente) as e:
    print(str(e))