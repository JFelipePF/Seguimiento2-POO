class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta.lower()  # "ahorros" o "corriente"
        self.saldo = 0.0  # Saldo inicial en cero

    def imprimir_info(self):
        print("Información de la cuenta bancaria:")
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta.capitalize()}")
        print(f"Saldo actual: ${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"\nSaldo consultado: ${self.saldo:.2f}")
        print()

    def consignar(self, valor):
        
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor:.2f} en la cuenta. El nuevo saldo es ${self.saldo:.2f}")
            print()
            return True
        else:
            print("Consignación denegada, el saldo debe ser positivo")
            print()
            return False

    def retirar(self, valor):
        
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor:.2f} de la cuenta. El nuevo saldo es ${self.saldo:.2f}")
            print()
            return True
        else:
            print("Retiro denegado, saldo insuficiente")
            print()
            return False

# Clase de prueba
class POO202502_A02_E25:
    def main():
        cuenta = CuentaBancaria(
            nombres="Juan Felipe",
            apellidos="Pérez Vera",
            numero_cuenta="1234567890",
            tipo_cuenta="ahorros"
        )
    
        cuenta.imprimir_info()
        cuenta.consultar_saldo()
    
       
        cuenta.consignar(55000)
    
        
        cuenta.retirar(20000)
    
        
        cuenta.retirar(40000)
    
        
        cuenta.consignar(-100)

    

if __name__ == "__main__":
    POO202502_A02_E25.main()
