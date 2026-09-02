/*4. Modificar el segundo problema resuelto de los ejemplos de la sección “Eventos
onMouseOver y onMouseOut.” Del material 11. (las casillas de la tabla que cambian el
color cuando ingresamos con el mouse) para permitir llamar mediante hipervínculos a
distintos programas que administran web-mail (Gmail, Hotmail y Yahoo!) */

function dirigir1(){
    let enlace=document.getElementById("yahoo")
    window.location.href=enlace.href
}

function dirigir2(){
    let enlace=document.getElementById("gmail")
    window.location.href=enlace.href 
}

function dirigir3(){
    let enlace=document.getElementById("hotmail")
    window.location.href=enlace.href 
}