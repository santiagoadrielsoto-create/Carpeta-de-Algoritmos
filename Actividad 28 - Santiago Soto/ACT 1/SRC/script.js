/*1. Confeccionar una página que muestre dos objetos de la clase RADIO solicitando que
seleccione si es mayor de 18 años o no. Al presionar un botón mostrar un alert
indicando si puede ingresar al sitio o no. */

function clickear(){
    if(document.getElementById("radio1").checked){
        alert("Puedes ingresar, eres mayor de edad")
    }
    else if(document.getElementById("radio2").checked){
        alert("No puedes ingresar a la pagina, eres menor de edad.")
    }
}