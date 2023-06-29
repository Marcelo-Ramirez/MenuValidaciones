import funciones

def menuPY():
    print("""
    ---> Menu

    1. Juego adivina un numero del 1 al 3
    2. Validacion de numero capicua
    3. validacion de numero primo
    4. validacion de numero positivo
    5. validar si un numero tiene n digitos
    6. validar un numero en un rango
    7. contador de cuanto se repite una letra en un texto
    8. contador de vocales en una texto
    9. contador de palabras en un texto
    10. imprimir palabras con una letra en especifico
    11. validar Numero par
    12. validar Numero impar

    """)
    digMenu = int(input('Selecciona una opcion: '))

    if digMenu == 1:
        val = int(input('Ingresa el numero que crees que genero la maquina: '))
        while True:
            if funciones.validarNumAleat(val):
                print('Correcto')
                break
            else:
                val = int(input('Intentalo denuevo: '))
        menuPY()
    elif digMenu == 2:
        val = int(input('Ingresa un numero y te dire si es capicua ej:(12321 es capicua): '))
        while True:
            if funciones.validNumCapi(val):
                print('Correcto')
                break
            else:
                val = int(input('Intentalo denuevo: '))
        menuPY()
    elif digMenu == 3:
        val = int(input('Ingresa un numero primo: '))
        while True:
            if funciones.validNumPrim(val):
                print('Correcto')
                break
            else:
                val = int(input('Intentalo denuevo: '))
        menuPY()
    elif digMenu == 4:
        val = int(input('Ingresa un numero positivo: '))
        while True:
            if funciones.validNumPos(val):
                print('Correcto')
                break
            else:
                val = int(input('Intentalo denuevo: '))
        menuPY()
    elif digMenu == 5:
        dig = int(input('Ingresa el numero de digitos que quieres validar: '))
        val = int(input('Ingresa un numero: '))
        while True:
            if funciones.validNumDig(dig, val):
                print('Correcto')
                break
            else:
                val = int(input('Intentalo denuevo: '))
        menuPY()
    elif digMenu == 6:
        min = int(input('Ingresa el valo minimo: '))
        may = int(input('Ingresa el valor maximo: '))
        val = int(input('Ingresa el numero que quieres verificar: '))
        while True:
            if funciones.validRang(min, may, val):
                print('Correcto')
                break
            else:
                val = int(input('Intentalo denuevo: '))
        menuPY()
    elif digMenu == 7:
        text = input('Ingresa un texto: ')
        lett = input('Ingresa la letra que quieres saber cuanto se repite: ')
        print(f'La letra {lett} se repite {funciones.contlett(text, lett)} veces')
        menuPY()
    elif digMenu == 8:
        text = input('Ingresa un texto: ')
        print(f'El texto tiene {funciones.contVocals(text)} vocales')
        menuPY()
    elif digMenu == 9:
        text = input('Ingresa un texto: ')
        print(f'El texto tiene {funciones.contWords(text)} palabras')
        menuPY()
    elif digMenu == 10:
        text = input('Ingresa un texto o la ruta del archivo .txt: ')
        lett = input('Ingresa la letra que deben tener las palabras que se imprimiran: ')
        if text[0]+text[1] == 'C:' or text[0]+text[1] == 'D:' or text[0]+text[1] == 'F:' or text[0]+text[1] == 'E:':
            file = open(text)
            tex = file.read()
            file.close
            funciones.printWordsLett(tex, lett)
            menuPY()
        else:
            funciones.printWordsLett(text, lett)
            menuPY()
    elif digMenu == 11:
        val = int(input('Ingresa un numero par'))
        while True:
            if funciones.validNumPar(val):
                print('Correcto')
                break
            else:
                val = int(input('Intentalo denuevo: '))
        menuPY()
    elif digMenu == 12:
        val = int(input('Ingresa un numero inpar'))
        while True:
            if funciones.validNumPar(val):
                val = int(input('Intentalo denuevo: '))
            else:
                print('Correcto')
                break
        menuPY()
    else:
        print("""Numero no Valido""")
        menuPY()

menuPY()