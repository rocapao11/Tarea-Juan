# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:50:58 2023

@author: and_p
"""
#V3 una frase es palindromo
print ("Este programa te indica si un texto es o no un palindomo")
def no_space(texto): #definimos una funcion para eliminar los espacios escritos
    new_tex=""
    for char in texto:
        if char != " ":
            new_tex += char
    return new_tex

def alrevez(texto): #definimos una funcion para poner alrevez lo escrito
    texto_alrevez = ""
    for char in texto:
        texto_alrevez = char + texto_alrevez
    return texto_alrevez


texto=input('introduce un texto \n')
texto = texto.lower()
texto = no_space(texto)
texto_alrevez = alrevez(texto)

if texto == texto_alrevez:
    print ("si es un palindromo")
else:
    print ("no es palindromo")

print ("fin del programa")

    