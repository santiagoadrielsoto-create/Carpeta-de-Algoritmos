/*Ejercicio 4: Algoritmo de Compresión de Texto (RLE)
Contexto: En telecomunicaciones se utiliza el algoritmo Run-Length Encoding (RLE) para
comprimir secuencias de caracteres repetidos y ahorrar ancho de banda.
Consigna: Escribir la función comprimir_rle(texto) que reciba una cadena de caracteres en
mayúsculas y devuelva su versión comprimida.
Requisitos:
● Contar las apariciones consecutivas de cada carácter.
● Construir una cadena resultante intercalando el carácter con su cantidad de
apariciones consecutivas.
Ejemplo de Entrada: &quot;AAABBCDDDD&quot; Salida Esperada: &quot;A3B2C1D4&quot; */
function carga(){
    let texto=(prompt("Ingrese el texto:"));
    return texto
}
function comprimirRle(texto){

    let resultado = "";
    let contador = 1;

    for(let i=0; i<texto.length-1; i++){

        if(texto[i] == texto[i+1]){
            contador = contador + 1;
        }else{
            resultado = resultado + texto[i] + contador;
            contador = 1;
        }
    }

    resultado = resultado + texto[texto.length-1] + contador;

    return resultado;
}

let texto=carga()
let resultado = comprimirRle(texto);

console.log("Texto comprimido:", resultado);