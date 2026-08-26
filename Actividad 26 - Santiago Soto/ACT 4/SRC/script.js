
/*Ejercicio 04: Lista de Compras Dinámica

Confeccionar una página con un campo de texto y un botón “Agregar”.
Cada vez que se presione el botón, el producto ingresado en el campo debe añadirse
a una lista (&lt;ul&gt;).
Además:
 La lista debe permitir eliminar un producto haciendo clic sobre él.
 En consola debe mostrarse en todo momento la cantidad de productos
actuales en la lista. */

let boton= document.getElementById("boton")
let lista=document.getElementById("lista")
let productosA= document.getElementById("lista").children.length
console.log("La cantidad de productos actuales son de ",productosA)

boton.addEventListener("click", function(){

let nuevoElemento=document.createElement("li")
let producto=prompt("Ingrese el articulo nuevo")
nuevoElemento.textContent= producto
document.getElementById("lista").appendChild(nuevoElemento)

productosA=productosA+1
console.log("La cantidad de productos actuales son de ",productosA)

nuevoElemento.onclick=function(){
    lista.removeChild(nuevoElemento)
    productosA=productosA-1
    console.log("La cantidad de productos actuales son de ",productosA)
}
})
