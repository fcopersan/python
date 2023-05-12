""" 
Reto #1: EL "LENGUAJE HACKER"

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 
"""
import pandas as pd

diccionario = pd.ExcelFile('C:/Users/francisco.perez/Documents/Python Scripts/Diccionario_Hacker.xlsx')

df=diccionario.parse('Diccionario')

texto_inp = input('¿Texto?: ')


action = int(input ('1:Encriptar ; 2:Desencriptar: '))

if action ==1:
    for n in range(0, 26):
        c1 = df.loc[n, 'Letra']
        c2 = df.loc[n, 'Sustitucion']
        texto_out = texto_inp.replace(str(c1), str(c2))
        texto_inp = texto_out
        
    print(texto_out)    
    
else:    
    for n in range(0, 26):
        c1 = df.loc[n, 'Letra']
        c2 = df.loc[n, 'Sustitucion']
        texto_out = texto_inp.replace(str(c2), str(c1))
        texto_inp = texto_out
        
    print(texto_out)    


