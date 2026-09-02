/*2. Confeccionar una página de visitas a un sitio, solicitar ingresar el nombre de una
persona, su mail y los comentarios (TEXTAREA). Mostrar luego llamando a la función
alert los datos ingresados. */

function mostrar(){

let nom=document.getElementById("nombre").value
let gma=document.getElementById("gmail").value
let com=document.getElementById("comentarios").value
alert(`nombre: ${nom} | Gmail: ${gma} | comentario: ${com}`)
}