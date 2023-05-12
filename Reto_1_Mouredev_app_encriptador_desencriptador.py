import pandas as pd
import tkinter as tk


diccionario = pd.ExcelFile('C:/Users/francisco.perez/Documents/Python Scripts/Diccionario_Hacker.xlsx')
df = diccionario.parse('Diccionario')


def encriptar_desencriptar():
    texto_inp = entrada_texto.get()
    accion = int(entrada_accion.get())

    if accion == 1:
        for n in range(0, 26):
            c1 = df.loc[n, 'Letra']
            c2 = df.loc[n, 'Sustitucion']
            texto_inp = texto_inp.replace(str(c1), str(c2))

    else:
        for n in range(0, 26):
            c1 = df.loc[n, 'Letra']
            c2 = df.loc[n, 'Sustitucion']
            texto_inp = texto_inp.replace(str(c2), str(c1))

    salida_texto.delete(0, tk.END)
    salida_texto.insert(0, texto_inp)


def copiar():
    texto_copiado = salida_texto.get()
    ventana.clipboard_clear()
    ventana.clipboard_append(texto_copiado)


ventana = tk.Tk()
ventana.title('Encriptador/Desencriptador')
ventana.geometry('400x200')

etiqueta_texto = tk.Label(ventana, text='Texto:')
etiqueta_texto.pack()

entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack()

etiqueta_accion = tk.Label(ventana, text='Acción (1: encriptar, 2: desencriptar):')
etiqueta_accion.pack()

entrada_accion = tk.Entry(ventana, width=50)
entrada_accion.pack()

boton_encriptar = tk.Button(ventana, text='Encriptar/Desencriptar', command=encriptar_desencriptar)
boton_encriptar.pack()

etiqueta_salida = tk.Label(ventana, text='Texto resultante:')
etiqueta_salida.pack()

salida_texto = tk.Entry(ventana, width=50)
salida_texto.pack()

boton_copiar = tk.Button(ventana, text='Copiar resultado', command=copiar)
boton_copiar.pack()

ventana.mainloop()