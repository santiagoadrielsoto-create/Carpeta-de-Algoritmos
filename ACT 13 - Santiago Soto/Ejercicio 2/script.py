#2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada
#cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe
#finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un
#programa que lea los datos de las cuentas corrientes e informe:
#● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo,
#sabiendo que:
#○ Estado de la cuenta:
#○ “Acreedor” si el saldo es &gt; 0.
#○ “Deudor” si el saldo es &lt; 0.
#○ “Nulo” si el saldo es = 0.
#● b) La suma total de los saldos acreedores.

#n=int(input(f"Cuantos clientes tiene en el banco?"))
total=0
for x in range(999999999999999999999999999999999999999999999999):
    Idcuenta=int(input(f"Ingrese el numero de  la cuenta {x+1}"))
    if Idcuenta<0:
        break
    else:
        saldoActual=int(input(f"Ingrese el saldo actual de la cuenta."))

        if saldoActual>0:
            print(f"En la cuenta {Idcuenta}")
            print(f"El estado de la cuenta es acredor con un saldo de {saldoActual}")
            total=total+saldoActual
        else:
            if saldoActual<0: 
                print(f"En la cuenta {Idcuenta}")
                print(f"El estado de la cuenta es deudor con un saldo de {saldoActual}")

            else:
                print(f"En la cuenta {Idcuenta}")
                print(f"El estado de la cuenta es nulo con un saldo de {saldoActual}")

print(f"La suma total de todas las cuentas acredoras es de {total}")