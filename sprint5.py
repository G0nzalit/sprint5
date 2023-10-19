class cuentas():
    def __init__(self, numero, clase, moneda):
        self.numero = numero
        self.clase = clase
        self.moneda = moneda

class CajaAhorroPesos(cuentas):
    def __init__(self, numero, clase, moneda):
        super().__init__(numero, clase, moneda)

class CajaAhorroDolares(cuentas):
    def __init__(self, numero, clase, moneda):
        super().__init__(numero, clase, moneda)

class CuentaCorrientePesos(cuentas):
    def __init__(self, numero, clase, moneda):
        super().__init__(numero, clase, moneda)

class CuentaCorrienteDolares(cuentas):
    def __init__(self, numero, clase, moneda):
        super().__init__(numero, clase, moneda)

class CuentaInversion(cuentas): 
    def __init__(self, numero, clase, moneda):
        super().__init__(numero, clase, moneda)

class Tarjeta:
    def __init__(self, limite_retiro_diario, limite_pago, limite_cuotas):
        self.limite_retiro_diario = limite_retiro_diario
        self.limite_pago = limite_pago
        self.limite_cuotas = limite_cuotas

class TarjetaDebito(Tarjeta):
    def __init__(self, limite_retiro_diario):
        super().__init__(limite_retiro_diario, 0, 0)


class TarjetaAmex(Tarjeta):
    def __init__(self, limite_retiro_diario, limite_pago, limite_cuotas):
        super().__init__(limite_retiro_diario, limite_pago, limite_cuotas)

class TarjetaMastercard(Tarjeta):
    def __init__(self, limite_retiro_diario, limite_pago, limite_cuotas):
        super().__init__(limite_retiro_diario, limite_pago, limite_cuotas)

class TarjetaVisa(Tarjeta):
    def __init__(self, limite_retiro_diario, limite_pago, limite_cuotas):
        super().__init__(limite_retiro_diario, limite_pago, limite_cuotas)


class Cliente:
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.transacciones = transacciones
        self.limite_retiro_diario = self._establecer_limite_retiro()
        self.limite_pago, self.limite_cuotas = self._establecer_limites_tarjeta()

    def _establecer_limite_retiro(self):
        if self.tipo == "Classic":
            return 10000
        elif self.tipo == "Gold":
            return 15000
        elif self.tipo == "Black":
            return 20000
        
    def _establecer_limites_tarjeta(self):
        if self.tipo == "Classic":
            return 500000, 600000
        elif self.tipo == "Gold":
            return 800000, 1000000
        elif self.tipo == "Black":
            return 1000000, 1200000    

class Classic(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, "Classic", transacciones)
        self.tarjeta_debito = TarjetaDebito("Classic")
        self.cajas_ahorro_pesos = 1
        self.cajas_ahorro_dolares = 0
        self.cargo_caja_dolares_mensual = 0
        self.retiro_efectivo_gratuito = 5
        self.tarifa_retiro_excedido = 10
        self.acceso_tarjeta_credito = False
        self.comision_transferencia_saliente = 0.01
        self.comision_transferencia_entrante = 0.005
    
    def agregar_tarjeta_debito(self):
        if self.tarjetas_debito < 1:
            self.tarjetas_debito += 1
            print(f"Se ha agregado una tarjeta de débito. Total: {self.tarjetas_debito}")
        else:
            print("No se pueden agregar más tarjetas de débito. Límite alcanzado.")


    def realizar_retiro_efectivo(self, monto):
        if self.retiro_efectivo_gratuito > 0 and monto <= self.limite_retiro_diario:
            print(f"Retiro de ${monto} realizado con éxito. Le quedan {self.retiro_efectivo_gratuito - 1} retiros gratuitos.")
            self.retiro_efectivo_gratuito -= 1
        else:
            if monto > self.limite_retiro_diario:
                print(f"Error: El monto de retiro (${monto}) excede el límite diario permitido (${self.limite_retiro_diario}).")
            else:
                print(f"Error: Se agotaron los retiros gratuitos. Tarifa de ${self.tarifa_retiro_excedido} aplicada.")


class Gold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, "Gold", transacciones)
        self.tarjeta_debito = TarjetaDebito("Gold")
        self.cajas_ahorro_pesos = 2
        self.cuenta_corriente = 1
        self.cajas_ahorro_dolares_extra = 0
        self.cargo_caja_dolares_mensual_extra = 10
        self.tarjetas_visa = 1
        self.extensiones_visa = 5
        self.tarjetas_mastercard = 1
        self.extensiones_mastercard = 5
        self.acceso_cuentas_inversion = True
        self.chequera = True
        self.comision_transferencia_saliente = 0.005
        self.comision_transferencia_entrante = 0.001

    def agregar_tarjeta_debito(self):
        if self.tarjetas_debito < 1:
            self.tarjetas_debito += 1
            print(f"Se ha agregado una tarjeta de débito. Total: {self.tarjetas_debito}")
        else:
            print("No se pueden agregar más tarjetas de débito. Límite alcanzado.")

    def realizar_retiro_efectivo(self, monto):
        if monto <= self.limite_retiro_diario:
            if self.retiro_gratuito_diario >= monto:
                print(f"Retiro de ${monto} realizado con éxito. Le quedan ${self.retiro_gratuito_diario - monto} de retiro gratuito hoy.")
                self.retiro_gratuito_diario -= monto
            else:
                tarifa_extra = 0.02 * monto
                print(f"Retiro de ${monto} realizado con una tarifa de ${tarifa_extra}.")
        else:
            print(f"Error: El monto de retiro (${monto}) excede el límite diario permitido (${self.limite_retiro_diario}).")

class Black(Cliente):
    def __init__(self, numero, nombre, apellido, dni, transacciones):
        super().__init__(numero, nombre, apellido, dni, "Black", transacciones)
        self.tarjeta_debito = TarjetaDebito("Black")
        self.cajas_ahorro_dolares = 5
        self.cuentas_corrientes = 3
        self.tarjetas_visa = 1
        self.extensiones_visa = 10
        self.tarjetas_mastercard = 1
        self.extensiones_mastercard = 10
        self.tarjetas_amex = 1
        self.extensiones_amex = 10
        self.retiro_gratuito_mensual = True
        self.acceso_cuentas_inversion = True
        self.chequeras = 2
        self.comision_transferencia_saliente = 0
        self.comision_transferencia_entrante = 0

    def agregar_tarjeta_debito(self):
        if self.tarjetas_debito < 5:
            self.tarjetas_debito += 1
            print(f"Se ha agregado una tarjeta de débito. Total: {self.tarjetas_debito}")
        else:
            print("No se pueden agregar más tarjetas de débito. Límite alcanzado.")

    def realizar_retiro_efectivo(self, monto):
        if monto <= self.limite_retiro_diario:
            print(f"Retiro de ${monto} realizado con éxito.")
        else:
            print(f"Error: El monto de retiro (${monto}) excede el límite diario permitido (${self.limite_retiro_diario}).")

def calcular_monto_total(precio_dolar, cantidad, impuesto_pais, ganancias):
    monto_total = cantidad * precio_dolar
    monto_total += monto_total * (impuesto_pais / 100)
    monto_total += monto_total * (ganancias / 100)
    return monto_total

def descontar_comision(monto, comision_porcentajes):
    monto_descontado = monto - (monto * (comision_porcentajes / 100))
    return monto_descontado

def calcular_monto_plazo_fijo(monto, interes):
    monto_final = monto + monto * (interes / 100)
    return monto_final
    

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

