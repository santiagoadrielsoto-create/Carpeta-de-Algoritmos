#3. Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 -
#16 - 24, etc.
multiplos=0
for j in range (8,500, 8):
    print(f"{j} es multiplo de 8")
    multiplos= multiplos +1

print(f"El total de multiplos de 8 que hay en 500 es de {multiplos}" )