#programa para saber si una palabra es un palidromo
print("programa para saber si una palabra es un palidromo")
palabra="tacocat"
print(palabra, "¿Es un palindromo?")

alrevez=""
for i in range(len(palabra)-1,-1,-1): #iteracion del final al principio
    alrevez += palabra[i]
    
c=alrevez==palabra #alrevez es igual a palabra?
print(c)
