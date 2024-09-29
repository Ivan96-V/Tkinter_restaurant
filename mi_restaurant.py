from tkinter import *
import datetime
import random
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def revisar_check():
    x= 0
    for c in cuadro_comida:
        if variable_comida[x].get() == 1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() == '0':
                cuadro_comida[x].delete(0, END)
            cuadro_comida[x].focus()
        else:
            cuadro_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadro_bebida:
        if variable_bebida[x].get() == 1:
            cuadro_bebida[x].config(state=NORMAL)
            if cuadro_bebida[x].get() == '0':
                cuadro_bebida[x].delete(0, END)
            cuadro_bebida[x].focus()
        else:
            cuadro_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadro_postres:
        if variable_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == '0':
                cuadro_postres[x].delete(0, END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    p = 0
    subtotal_comida = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    print(subtotal_comida)

    p = 0
    subtotal_bebida = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    print(subtotal_bebida)

    p = 0
    subtotal_postres = 0
    for cantidad in texto_postres:
        subtotal_postres = subtotal_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
    print(subtotal_postres)

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postres
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    var_costos_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costos_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costos_postres.set(f'$ {round(subtotal_postres, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 99999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, 'Items:\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 73 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'$ {round(int(bebida.get()), 2) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'$ {int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 73 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costos_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costos_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costos_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 73 + '\n')
    texto_recibo.insert(END, f' Sub-Total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, 'Que tenga excelente dia y lo esperamos pronto!')


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Information', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postres:
        v.set(0)

    var_costos_comida.set('0')
    var_costos_bebida.set('0')
    var_costos_postres.set('0')
    var_subtotal.set('0')
    var_impuestos.set('0')
    var_total.set('0')




# Iniciador de la aplicacion
aplicacion = Tk()

# tamanio de la ventana
aplicacion.geometry('1150x580+0+0')


# No mover la aplicacion
aplicacion.resizable(0,0)


# Titulo de la aplicacion
aplicacion.title('Mi Restaurante - Sistema de Facturacion')

# Color de fondo
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4', font=('Dosis', 48), bg='burlywood',
                        width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=SUNKEN, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# panel comida
panel_comida = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=SUNKEN, fg='azure4')
panel_comida.pack(side=LEFT)

# panel bebida
panel_bebida = LabelFrame(panel_izquierdo, text='Bebida', font=('Dosis', 19, 'bold'), bd=1, relief=SUNKEN, fg='azure4')
panel_bebida.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='postres', font=('Dosis', 19, 'bold'), bd=1, relief=SUNKEN,
                           fg='azure4')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=SUNKEN, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=SUNKEN, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=SUNKEN, bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merlusa', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruto', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comida
variable_comida = []
cuadro_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # crear checkbuttons
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comida,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadro_comida[contador] = Entry(panel_comida,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador,
                                 column=1)
    contador += 1

# generar items bebida
variable_bebida = []
cuadro_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:

    # crear checkbuttons
    variable_bebida.append('')
    variable_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebida,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadro_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadro_bebida[contador] = Entry(panel_bebida,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])

    cuadro_bebida[contador].grid(row=contador,
                                 column=1)
    contador += 1

# generar items postres
variable_postres = []
cuadro_postres = []
texto_postres = []
contador = 0

for postres in lista_postres:

    # crear checkbuttons
    variable_postres.append('')
    variable_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variable_postres[contador],
                         command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # Crear los cuadros de entrada
    cuadro_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadro_postres[contador] = Entry(panel_postres,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postres[contador])
    cuadro_postres[contador].grid(row=contador,
                                 column=1)

    contador += 1

# variables
var_costos_comida = StringVar()
var_costos_bebida = StringVar()
var_costos_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# etiqueta de costo y campos de entrada comida
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo de comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costos_comida)
texto_costo_comida.grid(row=0, column=1)


# etiqueta de costo y campos de entrada bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo de bebida ',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costos_bebida)
texto_costo_bebida.grid(row=1, column=1,padx=41)


# etiqueta de costo y campos de entrada postres
etiqueta_costo_postres = Label(panel_costos,
                              text='Costo de postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costos_postres)
texto_costo_postres.grid(row=2, column=1,padx=41)


# etiqueta de costo y campos de entrada subtotal
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=9,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3,padx=41)


# etiqueta de costo y campos de entrada impuestos
etiqueta_impuesto = Label(panel_costos,
                              text='Impuesto',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=9,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuesto.grid(row=1, column=3,padx=41)

# etiqueta de costo y campos de entrada total
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=9,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3,padx=41)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 1

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 10, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# calculadora

visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=38,
                          bd=1,)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

# botones de la calculadora
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'Borrar', '0', '/']
botones_guardados = []


fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   width=8,
                   bd=1)
    boton.grid(row=fila,
               column=columna)

    botones_guardados.append(boton)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))





# Titulo de la aplicacion
aplicacion.mainloop()