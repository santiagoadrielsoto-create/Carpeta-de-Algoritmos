"""
1. Desarrollar una función que reciba una lista de string y nos retorne el que
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=[&quot;enero&quot;, &quot;febrero&quot;, &quot;marzo&quot;, &quot;abril&quot;, &quot;mayo&quot;, &quot;junio&quot;]
print(&quot;Palabra con mas caracteres:&quot;,mascaracteres(palabras))
(La lista debe tener la misma cantidad de elementos, pero los textos los
eligen ustedes)
"""

def mascaracteres(lista):

    mayor=lista[0]
    for i in range(len(lista)):
       
        if len(lista[i]) > len(mayor):
            mayor = lista[i]  

        elif len(lista[i]) == len(mayor):
  
            if lista[i] < mayor: 
                mayor = lista[i]
        
    return(mayor)

palabra=["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
print(F"La palabra con mas caracteres es {mascaracteres(palabra)}.")