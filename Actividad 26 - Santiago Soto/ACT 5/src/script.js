/*Ejercicio 05: Control de Temperatura
Diseñar una página con un campo de texto para ingresar una temperatura y un botón
“Verificar”.
Cuando el usuario haga clic:
 Si la temperatura es menor a 10, mostrar en el documento el mensaje “Hace
frío” en azul.
 Si está entre 10 y 25, mostrar “Clima agradable” en verde.
 Si es mayor a 25, mostrar “Hace calor” en rojo.
Además, cada verificación debe registrarse en consola con la fecha y hora
exacta (usando Date()). */



let boton=document.getElementById("boton")
let textarea=document.getElementById("textarea")
let parrafo=document.getElementById("parrafo")

boton.addEventListener("click",function(){
    let texto=textarea.value
    if( texto<10 ){
    parrafo.style.color="blue"
    parrafo.textContent="Hace frio"

    }
    else if( texto>10 && texto<25 ){
    parrafo.style.color="green"
    parrafo.textContent="Hay un clima agradable"
        
    }

    else{

    parrafo.style.color="red"
    parrafo.textContent="Hace calor"
    }
      console.lof("La fecha de verificacio es ", new Date())
    }
)

