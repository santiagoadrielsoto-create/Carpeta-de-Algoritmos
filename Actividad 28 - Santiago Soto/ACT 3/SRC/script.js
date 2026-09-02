/*3. Solicitar que se ingrese el nombre y la clave de un usuario. Mostrar una ventana de
alerta si en la clave se ingresan menos de 7 caracteres o más de 20 (capturar el evento
onBlur) */

function clave(){
    let a=document.getElementById("contraseña")
    if(a.value.length< 7 || a.value.length>20 ){
        if(a.value.length< 7){
            alert("La contraseña debe tener mas de 7 caracteres")
        }
        else{
            alert("La contraseña debe tener menos de 20 caracteres")
        }
    }
    else{
        alert("Contraseña guardada")
    }
}