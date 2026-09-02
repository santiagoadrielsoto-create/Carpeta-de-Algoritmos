/*5. Generar un presupuesto de un equipo de computación a partir de tres
objetos de tipo SELECT que nos permiten seleccionar:
Procesador (Intel I3 - $400, Intel I5 $600, Intel I7 $800).
Monitor (Samsung 20&#39; - $250, Samsung 22&#39; - $350, Samsung 26&#39; - $550)
Disco Duro(500 Gb - $300, 1 Tb - $440, 3 Tb - $500)
Para cada característica indicamos string a mostrar (Ej. Intel I3) y el
valor asociado a dicho string (Ej. 400).
Al presionar un botón &quot;Calcular&quot; mostrar el presupuesto en un objeto de
tipo TEXT. */

function procesador(){
    let seleccion=document.getElementById("select1").options[document.getElementById('select1').selectedIndex].value;
let precio1 = seleccion
document.getElementById("parrafo1").value=precio1

}
function monitor(){
    let seleccion=document.getElementById("select2").options[document.getElementById('select2').selectedIndex].value;
let precio2 = seleccion
document.getElementById("parrafo2").value=precio2

}
function disco(){
    let seleccion=document.getElementById("select3").options[document.getElementById('select3').selectedIndex].value;
let precio3 = seleccion
document.getElementById("parrafo3").value=precio3


}

function calcular() {
    let precio=0
    let p1=parseInt(document.getElementById("parrafo1").value)
    let p2=parseInt(document.getElementById("parrafo2").value)
    let p3=parseInt(document.getElementById("parrafo3").value)
    precio=precio+p1+p2+p3
   let parrafo=document.getElementById("presupuesto")
  parrafo.textContent=`El precio final es de : $${precio}`
console.log(`El precio final es de : $${precio}`)
}