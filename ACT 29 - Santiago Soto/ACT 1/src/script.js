/*Ejercicio 1: Guardar Preferencias de Usuario
Enunciado: Crear una función que guarde y recupere las preferencias de un usuario,
como su nombre y el color de fondo preferido, utilizando LocalStorage.
1. La función debe permitir al usuario ingresar su nombre y seleccionar su color
de fondo preferido desde una lista de opciones.
2. Los datos ingresados deben almacenarse en LocalStorage.
3. Cada vez que la página se recargue, las preferencias deben recuperarse de
LocalStorage y aplicarse automáticamente (mostrar el nombre del usuario y
cambiar el color de fondo). */
/*
let boton=document.getElementById("boton")

boton.addEventListener("click",function(){
    
let nombre=document.getElementById("nombre")
localStorage.setItem('nombre',nombre)
alert(nombre)
})

function colores(){
    let seleccion=document.getElementById("colores").options[document.getElementById('colores').selectedIndex].value;
let color = seleccion

}*/

 document.addEventListener("DOMContentLoaded", function() {
      cargarPreferencias();

      document.getElementById("botonGuardar").addEventListener("click", guardarPreferencias);
    });

    function guardarPreferencias() {
      let nombre = document.getElementById("nombre").value;
      let color = document.getElementById("select1").value;

      localStorage.setItem("nombreG", nombre);
      localStorage.setItem("selects", color); 

      cargarPreferencias();
    }


    function cargarPreferencias() {
      let nombre = localStorage.getItem("nombreG") || "";
      let color = localStorage.getItem("selects") || "#ffffff";

      document.body.style.backgroundColor = color;
      
      let texto = document.getElementById("text");
      if (nombre) {
        texto.textContent = "Buena eleccion " + nombre + ".";
      } else {
        texto.textContent = "";
      }
    }






