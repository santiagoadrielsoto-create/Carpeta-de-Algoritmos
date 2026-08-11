"""Ejercicio 2: Detector de Transacciones Sospechosas (Parseo)
Contexto: Un banco recibe un lote diario de movimientos en un único texto largo con el
formato &quot;ID:TIPO:MONTO&quot;, donde TIPO puede ser I (Ingreso) o E (Egreso), separados por
comas.
Consigna: Crear una función procesar_transacciones(cadena_texto) que reciba el texto de
movimientos y realice el procesamiento completo.
Requisitos:
● Parsear la cadena de texto separando cada registro.
● Calcular y retornar el balance total de la cuenta (Ingresos suman, Egresos restan).
● Generar y retornar una lista con los IDs de las transacciones consideradas
&quot;sospechosas&quot;. Una transacción es sospechosa si es un Egreso superior a
$50.000.
Ejemplo de Entrada: &quot;TX101:I:120000, TX102:E:15000, TX103:E:85000,
TX104:I:3000&quot; Salida Esperada:
● Balance final: $23.000
● Transacciones sospechosas: [&#39;TX103&#39;]"""

def carga():
    texto = input("Ingrese las transacciones: ")
    return texto

def procesar_transacciones(texto):

    registros = texto.split(",")

    balance = 0
    sospechosas = []

    for i in range(len(registros)):

        datos = registros[i].strip().split(":")

        id = datos[0]
        tipo = datos[1]
        monto = int(datos[2])

        if tipo == "I":
            balance = balance + monto
        else:
            balance = balance - monto

            if monto > 50000:
                sospechosas.append(id)

    return balance, sospechosas


def aviso(balance,sospechosas):
    print("Balance final:", balance)
    print("Transacciones sospechosas:")

    for i in range(len(sospechosas)):
        print(sospechosas[i])

texto=carga()
balance, sospechosas = procesar_transacciones(texto)
aviso(balance,sospechosas)