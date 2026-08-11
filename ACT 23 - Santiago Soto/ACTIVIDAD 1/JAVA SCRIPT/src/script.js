/* Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
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
    let sala = [
        [1,0,0,0,1],
        [0,1,0,1,1],
        [0,0,0,0,0],
        [1,1,1,0,0],
        [1,0,0,0,1]
    ]

    let cantidad = parseInt(prompt("¿Cuántas entradas quiere sacar? "))
    let fila = parseInt(prompt("¿En qué fila? (1 al 5): ")) - 1

    let datos = [sala, fila, cantidad]

    return datos
}

function reservarConsecutivos(datos){

    let sala = datos[0]
    let fila = datos[1]
    let cantidad = datos[2]
    let contador = 0;

    let respuesta=[]
    for(let i=0; i<sala[fila].length; i++){
        
        if(sala[fila][i] == 0){
            contador = contador + 1;
        }else{
            contador = 0;
        }

        if(contador == cantidad){

            let inicio = i - cantidad + 1;
            let columnas=[]

            for(let j=inicio; j<i+1; j++){
            columnas.push[j]
            }
            for (let m=inicio;m<i+1;m++){
                console.log["Reserva realizada en las columnas:", columnas[m]];
            }
            for(let j=inicio; j<i+1; j++){
                sala[fila][j] = 1;
                respuesta=[sala]
            }
            console.log("Estado de la sala:")
           console.log(respuesta[0])  
        }
    
    }
    console.log["No fue posible realizar la reserva", []];
}
let datos=cargar() 
reservarConsecutivos(datos)
