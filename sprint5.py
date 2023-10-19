
from enum import Enum

class TipoCuenta(Enum):
    CAJA_AHORRO_PESOS = "Caja de Ahorro en Pesos"
    CAJA_AHORRO_DOLARES = "Caja de Ahorro en Dólares"
    CUENTA_CORRIENTE_PESOS = "Cuenta Corriente en Pesos"
    CUENTA_CORRIENTE_DOLARES = "Cuenta Corriente en Dólares"
    CUENTA_INVERSION = "Cuenta Inversión"

class TipoTarjeta(Enum):
    DEBITO = "Tarjeta de Débito"
    VISA = "Tarjeta VISA"
    MASTERCARD = "Tarjeta Mastercard"
    AMEX = "Tarjeta American Express"

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones=None):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.transacciones = transacciones if transacciones else []

        
        if tipo == "Classic":
            self.tarjetas_debito = 1
            self.cajas_ahorro_pesos = 1
            self.cajas_ahorro_dolares = 0
            self.retiro_efectivo_gratuito = 5
            self.tarifa_retiro_excedido = 10
            self.limite_retiro_diario = 10000
            self.acceso_tarjeta_credito = False
            self.comision_transferencia_saliente = 0.01
            self.comision_transferencia_entrante = 0.005
        elif tipo == "Gold":
            self.tarjetas_debito = 1
            self.cajas_ahorro_pesos = 2
            self.cuenta_corriente = 1
            self.cajas_ahorro_dolares_extra = 0
            self.retiro_gratuito_diario = 20000
            self.acceso_cuentas_inversion = True
            self.chequera = True
            self.comision_transferencia_saliente = 0.005
            self.comision_transferencia_entrante = 0.001
        elif tipo == "Black":
            self.tarjetas_debito = 5
            self.cajas_ahorro_pesos = 5
            self.cuentas_corrientes = 3
            self.retiro_gratuito_mensual = True
            self.acceso_cuentas_inversion = True
            self.chequeras = 2
            self.comision_transferencia_saliente = 0
            self.comision_transferencia_entrante = 0

    def agregar_tarjeta_debito(self):
        if self.tarjetas_debito < 1:
            self.tarjetas_debito += 1
            print(f"Se ha agregado una tarjeta de débito. Total: {self.tarjetas_debito}")
        else:
            print("No se pueden agregar más tarjetas de débito. Límite alcanzado.")

    def realizar_retiro_efectivo(self, monto):
        if monto <= self.limite_retiro_diario:
            if hasattr(self, 'retiro_gratuito_diario') and self.retiro_gratuito_diario >= monto:
                print(f"Retiro de ${monto} realizado con éxito. Le quedan ${self.retiro_gratuito_diario - monto} de retiro gratuito hoy.")
                self.retiro_gratuito_diario -= monto
            else:
                tarifa_extra = 0.02 * monto
                print(f"Retiro de ${monto} realizado con una tarifa de ${tarifa_extra}.")
        else:
            print(f"Error: El monto de retiro (${monto}) excede el límite diario permitido (${self.limite_retiro_diario}).")

    

def generar_reporte(cliente):
    html = f"<h1>Resumen de Movimientos - Cliente {cliente.numero}</h1>"
    html += f"<p>Nombre: {cliente.nombre} {cliente.apellido}</p>"
    html += f"<p>DNI: {cliente.dni}</p>"
    html += f"<p>Tipo de Cliente: {cliente.tipo}</p>"
    html += "<h2>Transacciones:</h2>"
    html += "<ul>"
    for transaccion in cliente.transacciones:
        estado = "Aceptada" if transaccion["estado"].upper() == "ACEPTADA" else "Rechazada"
        html += f"<li>Estado: {estado}</li>"
        html += f"<li>Tipo: {transaccion['tipo']}</li>"
        html += f"<li>Permitido Actual para Transacción: {transaccion['permitidoActualParaTransaccion']}</li>"
        html += f"<li>Monto: {transaccion['monto']}</li>"
        html += f"<li>Fecha: {transaccion['fecha']}</li>"
        html += f"<li>Número: {transaccion['numero']}</li>"
        html += "<br>"
    html += "</ul>"
    return html


transacciones_cliente1 = [
    {"estado": "ACEPTADA", "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", "permitidoActualParaTransaccion": 9000, "monto": 1000, "fecha": "10/10/2022 16:00:55", "numero": 1},
    {"estado": "RECHAZADA", "tipo": "COMPRA_EN_CUOTAS_TARJETA_VISA", "permitidoActualParaTransaccion": 9000, "monto": 750000, "fecha": "10/10/2022 16:14:35", "numero": 2}
]

transacciones_cliente2 = [
    {"estado": "ACEPTADA", "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", "permitidoActualParaTransaccion": 8000, "monto": 500, "fecha": "11/10/2022 14:30:20", "numero": 1},
    {"estado": "ACEPTADA", "tipo": "COMPRA_CON_DEBITO", "permitidoActualParaTransaccion": 7500, "monto": 2000, "fecha": "11/10/2022 15:45:10", "numero": 2}
]


cliente1 = Cliente(numero=100001, nombre="Nicolas", apellido="Gaston", dni="29494777", tipo="Black", transacciones=transacciones_cliente1)
cliente2 = Cliente(numero=100002, nombre="María", apellido="López", dni="12345678", tipo="Classic", transacciones=transacciones_cliente2)


reporte_cliente1 = generar_reporte(cliente1)
reporte_cliente2 = generar_reporte(cliente2)


with open("informe_cliente1.html", "w") as file:
    file.write(reporte_cliente1)

with open("informe_cliente2.html", "w") as file:
    file.write(reporte_cliente2)

print("Informes generados y guardados en 'informe_cliente1.html' e 'informe_cliente2.html'.")
