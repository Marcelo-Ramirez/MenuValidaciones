import random
 
#1 Validar numero aleatorio juego (del 1 al 3)
def validarNumAleat(num):
    numAleat = random.randint(1,3)
    if num == numAleat:
        return True
    else:
        return False
        

#2 Validar un numero capicua
def validNumCapi(num):
    numbinvert = 0
    contDig = 0
    numberDig = num
    numberInit = num
    n = 1
    while numberDig>0:
        numberDig = numberDig//10
        contDig += 1
    while num> 0:
        numb = num % 10
        num = num // 10
        numbinvert += numb * (10**(contDig-n))
        n += 1
    return numbinvert == numberInit

#3 Validar numero primo
def validNumPrim(num):
    numbase = [2,3,5,7]
    for i in numbase:
        if num == i:
            return True
        elif num % i == 0:
            return False
    return True

#4 Validar numero positivo
def validNumPos(num):
    if num > 0:
        return True
    else:
        return False
    
#5 Validar numero de digitos
def validNumDig(nDig, num):
    cont = 0
    while num > 0:
        num = num // 10
        cont += 1
    if nDig == cont:
        return True
    else:
        return False
    
#6 Validar rango
def validRang(Min, May, num):
    if Min<=num and May>=num:
        return True
    else:
        return False
    
#7 Contador de una letra en especifico
def contlett(str, lett):
    cont = 0
    for i in range(len(str)):
        if str[i] == lett:
            cont += 1
    return cont

#8 Contador de vocales en una cadena (mayusculas y minusculas)
def contVocals(str):
    cont = 0
    vocalsMin = 'aeiou'
    vocalsMay = 'AEIOU'
    for i in range(len(str)):
        for j in range(5):
            if vocalsMin[j] == str[i] or vocalsMay[j] == str[i]:
                cont += 1
    return cont
#9 Contador de palabras en una cadena.
def contWords(str):
    cont = 0
    word = ''
    for i in range(len(str)):
        if str[i] != ' ':
            word += str[i]
        else:
            if len(word)>0:
                cont += 1
                word = ''
    if len(word)>0:
        cont +=1
    return cont

#10 Imprimir en pantalla palabras con una letra en especifico
def printWordsLett(str, lett):
    word = ''
    sw = True
    for i in range(len(str)):
        if str[i] != ' ':
            word += str[i]
        else:
            if len(word)> 0:
                for j in range(len(word)):
                    if word[j] == lett:
                        print(word)
                        word = ''
                        sw = False
                        break
                word = ''
    for k in range(len(word)):
        if word[k] == lett:
            print(word)
            sw = False
            break
    if sw:
        print('No existen palabras con esa letra')

#11 Validar numero par
def validNumPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
