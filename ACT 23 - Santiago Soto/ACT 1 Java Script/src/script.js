/*Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.*/

function cargar(){
    let sala =[[1,0,0,0,1],
            [0,1,0,1,1],
            [0,0,0,0,0],
            [1,1,1,0,0],
            [1,0,0,0,1]
    ]
    let entrada = parseInt(prompt("¿Cuántas entradas quiere sacar? "))
    let fila = parseInt(prompt("¿En qué fila? (1 al 5): "))
    fila=fila -1 
    let datos = [sala, fila, entrada]

    return datos
}

function reservar_consecutivos(datos){
    let sala = datos[0]
    let fila = datos[1]
    let entrada = datos[2]

    let contador = 0
    for (let i=0;i<sala[fila].length;i++){

        if (sala[fila][i] == 0){
            contador = contador + 1}
        else{
            contador = 0}
        if (contador == entrada){
            let inicio = i - entrada + 1
            for(let j=inicio ; j<i +1 ; j++){
                datos[0][fila][j] = 1
            }
            console.log("Reserva realizada.")
            console.log("Las columnas asignadas son:")
            for(let j=inicio;j<i+1;j++){
                console.log("Columna", j+1)
            }

            return
        }

    console.log("No fue posible realizar la reserva.")
}
}

let datos = cargar()
reservar_consecutivos(datos)
console.log("Sala actualizada")
for(let f=0;f<1;f++){
    console.log(datos[f])
}
