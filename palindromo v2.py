# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 00:38:53 2023

@author: and_p
"""
#este es un programa para saber si una palabra es un palindromo VERSION INTERACTIVO
print("programa para saber si una palabra es un palidromo")

palabra=input('introduce tu palabra \n') #El usuario teclea su palabra, \n deja un espacio

print("¿es un palindromo?")
alrevez="" 
for i in range(len(palabra)-1,-1,-1): #iteracion del final al principio
    alrevez += palabra[i]
    
print("la palabra escrita alrevez es:", alrevez)

if palabra == alrevez:
    print ("si es un palindromo")
else:
    print ("no es palindromo")

