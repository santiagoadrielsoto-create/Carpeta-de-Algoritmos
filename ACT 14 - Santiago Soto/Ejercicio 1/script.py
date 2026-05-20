#1. Definir una lista que almacene por asignación los nombres de 5 personas.
#contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.

nombres = ["lucas", "pablo", "santi", "lolo", "sebas"]
contador = 0
for x in nombres:
    if len(x) >= 5:
        print(f"El nombre {x} contiene 5 o más caracteres")
        contador += 1

print(f"Total de nombres con 5 o más caracteres: {contador}")