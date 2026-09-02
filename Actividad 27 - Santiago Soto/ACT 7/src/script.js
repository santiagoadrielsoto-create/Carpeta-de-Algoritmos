/*7. Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
Mostrar al presionar un botón los deportes que eligió. */

function clicker(){
let cant=0
  let parrafo1=document.getElementById("parrafo1")
  let parrafo2=document.getElementById("parrafo2")
    let parrafo3=document.getElementById("parrafo3")
if(document.getElementById("Futbol").checked){
  cant++
 
  parrafo1.textContent=("El usuario juega a futbol")

}

if(document.getElementById("Basquet").checked){
  cant++
  if(cant>1){
   parrafo2.textContent=("El usuario tambien juega a basquet")
  }
  else{
  parrafo2.textContent=("El usuario juega a basquet")
  }
}

if(document.getElementById("Tenis").checked){
  cant++
  if(cant>1){
     parrafo3.textContent=("El usuario tambien juega a Tenis")
  }
  else{
     parrafo3.textContent=("El usuario juega a Tenis")
  }
}

}