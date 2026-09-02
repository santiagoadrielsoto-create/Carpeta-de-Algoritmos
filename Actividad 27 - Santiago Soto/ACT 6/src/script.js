/*6. Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT) */



function enviar(){

    let A=0
let E=0  

let seleccion1=document.getElementById("select1")
     let respuesta1=seleccion1.value
         let p1=document.getElementById("p1")
     if(respuesta1=="1"){
         A++
         p1.textContent=("Correcta")
     }
     else{
        E++
        p1.textContent=("Incorrecta")
     }
    
 let seleccion2=document.getElementById("select2")
     let respuesta2=seleccion2.value
       let p2=document.getElementById("p2")
     if(respuesta2=="1"){
         A++
p2.textContent=("Correcta")
     }
     else{
        E++
        p2.textContent=("Incorrecta")

     }
        let seleccion3=document.getElementById("select3")
     let respuesta3=seleccion3.value
       let p3=document.getElementById("p3")
     if(respuesta3=="1"){
       A++
p3.textContent=("Correcta")
     }
     else{
       E++
       p3.textContent=("Incorrecta")
     }
      let seleccion4=document.getElementById("select4")
     let respuesta4=seleccion4.value
       let p4=document.getElementById("p4")
     if(respuesta4=="1"){
         A++
         p4.textContent=("Correcta")

     }
     else{
        E++
        p4.textContent=("Incorrecta")
     }

let resultado=document.getElementById("resultado")
resultado.textContent=`La cantidad de respuestas correctas son ${A} y la cantidad de incorrectas son ${E}`
}