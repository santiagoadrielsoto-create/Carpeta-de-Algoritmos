/*Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
 El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
 Si hay un empate, debe mostrar el mensaje “Hay un empate”. */
function carga(){
let boton1= document.getElementById("btn1")
let boton3= document.getElementById("btn2")
let boton2= document.getElementById("btn3")
let suma1= 1
let suma2= 1
let suma3= 1
return boton1,boton2,boton3,suma1,suma2,suma3
}
function sumas(boton1,boton2,boton3,suma1,suma2,suma3){
boton1.onclick=function(){
    suma1=suma1+1
    alert("Votos totales del candidato 1 es de",suma1)
}
boton2.onclick=function(){suma2=suma2+1
    alert("Votos totales del candidato 2 es de",suma2)}
boton3.onclick=function(){
    suma3=suma3+1
    alert("Votos totales del candidato 3 es de",suma3)
}
 let Sumas=[suma1,suma2,suma3]
 return Sumas
}
function mayorV(Sumas){
 let mayor=0
 let c=0
for(let i=0;i<3;i++){
    if (Sumas[i]>mayor){
        mayor=Sumas[i]
        c=i
    }
    
}

for(let j=0;j<3;j++){
    if (mayor==Sumas[j]){
        console.log("Hay un empate")
        alert("hay un empate")
    }
    else{
        console.log("Va ganando el candidato ",(c+1)," con un total de votos de ", nayor)
    }
}
}
let boton1,boton2,boton3,suma1,suma2,suma3=carga()
let Sumas= sumas(boton1,boton2,boton3,suma1,suma2,suma3)
mayorV(Sumas)
