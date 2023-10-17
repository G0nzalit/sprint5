
class Cliente:
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.transacciones = transacciones

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


transacciones = [
    {"estado": "ACEPTADA", "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", "permitidoActualParaTransaccion": 9000, "monto": 1000, "fecha": "10/10/2022 16:00:55", "numero": 1},
    {"estado": "RECHAZADA", "tipo": "COMPRA_EN_CUOTAS_TARJETA_VISA", "permitidoActualParaTransaccion": 9000, "monto": 750000, "fecha": "10/10/2022 16:14:35", "numero": 2}
]

cliente = Cliente(numero=100001, nombre="Nicolas", apellido="Gaston", dni="29494777", tipo="BLACK", transacciones=transacciones)


reporte_html = generar_reporte(cliente)

with open("informe_cliente.html", "w") as file:
    file.write(reporte_html)

print("Informe generado y guardado en 'informe_cliente.html'.")
