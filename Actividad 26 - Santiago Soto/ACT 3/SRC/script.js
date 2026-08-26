/*Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
 El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
 Si hay un empate, debe mostrar el mensaje “Hay un empate”.*/

let contador1=0
let contador2=0
let contador3=0



let boton1= document.getElementById("boton1")

boton1.addEventListener("click", function(){
    contador1= contador1+1
    alert("el candidato 1 recibio 1 voto")
    console.log("votos al candidato 1:", contador1)
    if (contador1> contador2 && contador1>contador3){
        console.log("El candidato 1 es el que mas votos lleva")
    } 
    else{
        console.log("Hay un empate")
    }
})

let boton2= document.getElementById("boton2")

boton2.addEventListener("click", function(){
    contador2= contador2+1
    alert("el candidato 2 recibio 1 voto")
   console.log("votos al candidato 2:", contador2)
    if ( contador2> contador1 && contador2>contador3){
        console.log("El candidato 2 es el que mas votos lleva")
    } 
    else{
        console.log("Hay un empate")
    }
})

let boton3= document.getElementById("boton3")

boton3.addEventListener("click", function(){
    contador3= contador3+1
    alert("el candidato 3 recibio 1 voto")
    console.log("votos al candidato 3:", contador3)
    if ( contador3> contador1 && contador3>contador2){
        console.log("El candidato 3 es el que mas votos lleva")
    } 
    else{
        console.log("Hay un empate")
    }
})
