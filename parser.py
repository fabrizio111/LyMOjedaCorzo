# Este es el alfabeto que contiene los elementos terminales del lenguaje
alfabeto = ["var", "PROC", "drop", "free", "walk","canWalk", "fi", "go", "GORP","do", "walk", "od", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else", "around"]
#El conjunto de elementos no terminales del lenguaje
metodos=["drop", "walk", "jump", "jumpTo", "veer", "look", "grab", "get", "free", "pop", "PROC", "do", "go",  "if", "while", "repeatTimes"]
condiciones =["isfacing", "isValid", "canWalk", "not"]
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
metodosnoconocidos=[]
variables=[]
parametros=[]
walk=["north", "south", "east", "west","right", "left", "front", "back"]
puntos_cardinales=["north", "south", "east", "west"]
veer_to=["right", "left","around"]
objetos=['balloons','chips']


#Analizador
def Parser()->bool:
    ruta = input("\nIngrese la ruta del archivo: ")
    archivo = open(ruta, "r")
    retorno = True
    lineas = archivo.read().replace("\n", " ")
    archivo.close()
    lineas.strip()
    retorno = recorrer(lineas)
    if(retorno==True):
      print("\nEl programa está escrito sintácticamente correcto.\n")
    else:
      print("\nEl programa está escrito sintácticamente incorrecto.\n")
  

#Method used to go over the whole .txt file in String form, calling the methods that verify sintax.
def recorrer(lineas:str)->bool:
  palabra = ""
  indice=0
  indice2=0
  retorno=True

  if lineas[0]=="P" and lineas[1]=="R" and lineas[2]=="O" and lineas[3]=="G":  
    if lineas[-1]=="P" and lineas[-2]=="R" and lineas[-3]=="O" and lineas[-4]=="G":
        retorno=True
    else:
        retorno=False
  else:
      retorno=False

  indice =4    
  while indice2< len(lineas)-5: 
    palabra+=lineas[indice2]
    if lineas[indice2+1]==",":
      variables.append(palabra)
      palabra=""
      indice2+=1
    elif lineas[indice2-1]=="," and lineas[indice2+1]==";":
      variables.append(palabra2)
      palabra2=""     
    indice2+=1  
    diferencia=indice2-indice
    indice+=diferencia
    indice+=1
  return retorno

#Method used to determine which reserved word is identified and call the corresponding verifier.
def call_method(palabra:str, indice:int, lineas:str)->tuple:
    tuplaverdadindice=(False, 0)
    if palabra == "drop":
        tuplaverdadindice=comparardrop(lineas, indice)
    elif palabra == "=":
        tuplaverdadindice=assignment(lineas, indice)
    elif palabra == "walkm":
        tuplaverdadindice=compararwalkmultiple(lineas, indice)    
    elif palabra == "jump":
        tuplaverdadindice=compararjump(lineas, indice)
    elif palabra == "jumpTo":
        tuplaverdadindice=compararjumpTo(lineas, indice) 
    elif palabra == "veer":
        tuplaverdadindice=compararveer(lineas, indice)
    elif palabra == "look":
        tuplaverdadindice=compararlook(lineas, indice)
    elif palabra == "grab":
        tuplaverdadindice=comparargrab(lineas, indice)
    elif palabra == "get":
        tuplaverdadindice=compararget(lineas, indice)
    elif palabra == "free":
        tuplaverdadindice=compararfree(lineas, indice)      
    elif palabra == "pop":
        tuplaverdadindice=compararpop(lineas, indice)
    elif palabra == "isfacing":
        tuplaverdadindice=compararisfacing(lineas, indice)
    elif palabra == "isValid":
        tuplaverdadindice=compararisValid(lineas, indice)
    elif palabra == "canWalk":
        tuplaverdadindice=compararcanwalkmultiple(lineas, indice)
    elif palabra == "not":
        tuplaverdadindice=compararnot(lineas, indice)
    elif palabra == "while":
        tuplaverdadindice=compararwhile(lineas, indice)
    elif palabra == "repeatTimes":
        tuplaverdadindice=compararrepeatTimes(lineas, indice)
    else:
        tuplelist = list(tuplaverdadindice)
        tuplelist[0]=False
        tuplaverdadindice = tuple(tuplelist)
    return tuplaverdadindice

#Funcion para saber cual condicional se va a usar y verificar si está sintacticamente correcto.
def compararcondicionales(name:str, number:int):
    number2=0
    if  name == "isfacing":
        number2=compararisfacing(number)
    elif name == "isValid":
        number2=compararisValid(number)
    elif name == "canWalk":
        number2=compararcanwalkmultiple(number)
    elif name == "not":
        number2=compararnot(number)
    else:
        number2 = 0 

    return number2

#Methods used to individually asses the the sintax of every declared method in the .txt file.

def assignment(name,number):
        result=0
        verificar=[]
        forma=[]
        resto=len(name)-(number+1)

        if resto>=3:
                
                verificar.append('=')
                contador = 1  
                

                while contador <= 4:

                   sub_number=number + contador
                   posicion=name[sub_number]
                   verificar.append(posicion)
                   contador += 1

                var_name=verificar[1]
                forma.append('=',var_name,numeros, ')')

                if len(verificar) == 4:
                        if verificar[-1] == forma[-1]:
                                for numero in numeros:
                                        if numero in verificar[2]:
                                                result=1

        return result

def comparardrop(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararwalkmultiple(lineas:str, indice:int)->tuple:
  bool = False
  if indice+3 == ")":#se podria mirar
    tuplasimple = compararwalksimple(lineas, indice)
  else:
    tuplacompuesta = compararwalkcompuesto(lineas, indice)
  if tuplasimple[0]==False or tuplacompuesta[0]==False:
    bool=False
  indicefinal =indice
  tupla= (True,indicefinal)
  return tupla

#walk

def compararwalksimple(name, number):

    result= 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 2:
        
        verificar.append('walk')
        forma.append('walk', numeros, ')')
        contador=1
        while contador <= 3:

            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 3:
            if verificar[-1] == forma[-1]:
                encontrado_numero= False
                encontrado_letra=False
                numero = 0
                letra = 0
                while encontrado_numero == False and numero <= len(numeros): 

                    if numeros[numero] in verificar[1]:
                        encontrado_numero = True
                        result = 1
                    numero += 1
                        
                while encontrado_letra == False and letra <= len(letras): 

                    if letras[letra] in verificar[1]:
                        encontrado_letra = True
                        result = 1
                    letra += 1 
                        

    return result

"""

def compararwalksimple(lineas, indice)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2:
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
                sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla = (longitud,sintaxis)
  return tupla

"""
def compararwalkcompuesto(lineas, indice)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  palabra2=""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+5 :
      for indicewalk in walk:
        palabra+=lineas[indice3]
        if palabra == indicewalk:
          longitudactual = lineas[indice3+len(palabra)]
          if lineas[len(longitudactual)+1]==",":
            longitudactual_2+=1
            while longitudactual_2<=longitudactual+1:
              palabra2+=lineas[longitudactual]
              for indicevar in variables:
                for indicepar in parametros:
                  if palabra2 == indicepar or palabra2 == indicevar or palabra2.isdigit() == True:
                    longitudactual3 = lineas[longitudactual+len(palabra2)]
                    if lineas[len(longitudactual3)+1]==")":
                      sintaxis = True
              longitudactual_2+=1          
      indice3+=1
  longitud = len(longitudactual3+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararjump(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararjumpTo(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  longitudactual=0
  indice4=0
  palabra2=""
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
      indice3+=1
  if longitudactual!=0:          
    if lineas[len(longitudactual)+1]==",":
      indice4=longitudactual+1
      while indice4<= indice4+2 :
        for indicevar in variables:
          for indicepar in parametros:
            palabra2+=lineas[indice4]
            if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
              longitudactual = lineas[indice4+len(palabra2)]   
              sintaxis = True
        indice4+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararveer(name, number):

    result = 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 3:

        verificar.append('veer')
        forma.append('veer',':',veer_to, ')')
        contador=1
        while contador <= 4:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador +=1

        if len(verificar) == 4:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    encontrado_veer= False
                    veer= 0
                    while encontrado_veer == False and veer <= len(veer_to): 

                        if veer_to[veer] in verificar[2]:
                            encontrado_veer = True
                            result = 1
                        veer += 1

    return result

"""
por si no sirve el de arriba
#veer
def compararveer(name, number):

    result = 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 3:

        verificar.append('veer')
        forma.append('veer', numeros, ')')
        contador=1
        while contador <= 4:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador +=1

        if len(verificar) == 4:
            if verificar[1] == forma[1]:
                if verificar[3] == forma[3]:
                    encontrado_veer= False
                    veer= 0
                    while encontrado_veer == True: 

                        if veer in verificar[1]:
                            encontrado_veer = True
                            result = 1

    return result
"""
def compararlook(name, number):

    result = 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 3:

        verificar.append('look')
        forma.append('look', ':', puntos_cardinales, ')')
        contador=1
        while contador <= 4:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 4:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    encontrado_look= False
                    look= 0
                    while encontrado_look == False and look <= len(puntos_cardinales): 

                        if puntos_cardinales[look] in verificar[2]:
                            encontrado_look = True
                            result = 1
                        look += 1

    return result

#Grab
def comparargrab(name, number):

    result = 0
    verificar = []
    forma = ['grab', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('grab')
        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 5:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                  if 'balloons' in verificar[2]:
                    encontrado  = False 
                    elemento = 0  
                    letra = 0
                    while encontrado == False and elemento <= len(objetos):

                        if verificar[2] == objetos[elemento]:
                            letra = 0
                            while encontrado == False and letra <= len(letras):

                                if letras[letra] in verificar[3]:
                                    result = 1
                                    encontrado == True
                                letra += 1
                        elemento += 1

    return result

"""
por si no sale bien el de arriba
def comparargrab(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla
"""
#get
def compararget(name, number):

    result = 0
    verificar = []
    forma = ['grab', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('grab')
        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 5:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                  if 'chips' in verificar[2]:
                    encontrado  = False 
                    elemento = 0  
                    letra = 0
                    while encontrado == False and elemento <= len(objetos):

                        if verificar[2] == objetos[elemento]:
                            letra = 0
                            while encontrado == False and letra <= len(letras):

                                if letras[letra] in verificar[3]:
                                    result = 1
                                    encontrado == True
                                letra += 1
                        elemento += 1

    return result

"""
ppor si no sale bien el de arriba
def compararget(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit()==True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla
"""
#drop
def drop(name, number):

    result = 0
    verificar = []
    forma = ['drop', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('drop')

        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 5:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    if 'chips' in verificar[2]:
                        letra= 0
                        while encontrado_letra == False and letra <= len(letras): 

                         if letras[letra] in verificar[3]:
                           encontrado_letra = True
                           result = 1
                           letra += 1

    return result

#free
def compararfree(name, number):

    result = 0
    verificar = []
    forma = ['free', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('free')

        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 5:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    if 'balloons' in verificar[2]:
                        letra= 0
                        while encontrado_letra == False and letra <= len(letras): 

                         if letras[letra] in verificar[3]:
                           encontrado_letra = True
                           result = 1
                           letra += 1

    return result

"""
por si no sale el de arriba

def compararfree(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() ==True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla
"""

def compararpop(lineas:str, indice:int)->tuple:
  indice2 = indice
  sintaxis = False
  palabra = ""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

#Condicionales
def compararisfacing(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+5 :
      for indiceface in facing:
        palabra+=lineas[indice3]
        if palabra == indiceface:
          longitudactual = lineas[indice3+len(palabra)]
          if lineas[len(longitudactual)+1]==")":
            sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararisValid(lineas:str, indice:int)->tuple:
  pass

def compararcanwalkmultiple(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  palabra2=""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+5 :
      for indicewalk in walk:
        palabra+=lineas[indice3]
        if palabra == indicewalk:
          longitudactual = lineas[indice3+len(palabra)]
          if lineas[len(longitudactual)+1]==",":
            longitudactual_2+=1
            while longitudactual_2<=longitudactual+1:
              palabra2+=lineas[longitudactual]
              for indicevar in variables:
                for indicepar in parametros:
                  if palabra2 == indicepar or palabra2 == indicevar or palabra2.isdigit() == True:
                    longitudactual3 = lineas[longitudactual+len(palabra2)]
                    if lineas[len(longitudactual3)+1]==")":
                      sintaxis = True
              longitudactual_2+=1          
      indice3+=1
  longitud = len(longitudactual3+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararnot(lineas:str, indice:int)->tuple:
  if lineas[indice+1] == "(":
    pass
  pass

def compararif(lineas:str, indice:int)->tuple:
  pass

def compararwhile(lineas:str, indice:int)->tuple:
  sintaxis = False
  flag = False
  longitudcondicional=9
  palabra=""
  if lineas[indice+1]=="(":
    indice+=1
    while indice <= indice+9 and not flag:
      palabra+=lineas[indice]
      if(palabra in condiciones):
        flag = True
        sintaxis = compararcondicionales(palabra, indice, lineas)
      indice+=1
  else:
    sintaxis = False

def compararrepeatTimes(lineas:str, indice:int)->tuple:
  pass

#Lines of code which call upon the main method and start the parser method as a whole.
print("\n---Welcome to the Java Program Parser---")
Parser()




#       # estructuras si no esta sacar el nombre e ir a posicion y evaluar
#                 """ 
#             else:
#               noencontrado=palabra
#               for indicea in range(len(alfabeto)):
#                 token = cadena[indicea]
#                 if token in noencontrado:
#                   noencontrado=""
#                      """     
# """  
# def verificador(lineas:list)->bool:
#   for lineap in lineas:
#     comparador(lineap)
   
# def comparador(lineacomparada: str)->bool:
#   palabra=""
#   for letra in lineacomparada:
#     palabra+= letra
#     if(palabra in metodos):
#       if palabra = "if":
#         compararif()
# """
  
# file1 = open("Text.txt", "r")
# print(file1.read())

# file = open("Text.txt", "r")
# for line in file:
#   print(line)