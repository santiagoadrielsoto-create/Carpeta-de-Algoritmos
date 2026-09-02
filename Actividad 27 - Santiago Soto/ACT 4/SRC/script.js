/*4. Confeccionar una página que muestre un objeto SELECT con distintos
tipos de pizzas (Jamón y Queso, Muzzarella, Morrones). Al seleccionar
una, mostrar en un objeto de tipo TEXT el precio de la misma. */

function comprar(){
    let seleccion=document.getElementById("select1")
let precio = seleccion.value
document.getElementById("parrafo").value=precio

}