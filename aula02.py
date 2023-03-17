#def teste(numero ):
#    print('numero escolhido', numero)
#    if (numero == 0):
#         return 0 
#    return numero * teste( numero - 1)
#retorno = teste(10)
#print(retorno)
####################################################
#def soma(*args):
#    result = 0
#    for i in args:
#        result += i
#    return result
#print (soma(1, 2, 3, 4, 5))
#################################################################

#def argumento(arg1, arg2, arg3):
#     somartorio = arg1 + arg2 + arg3 
#     return somartorio

#a = float(input("Digite o segundo numero: "))
#b = float(input("Digite o segundo numero: "))
#c = float(input("Digite o terceiro numero: "))
#print(argumento(a, b, c))
#print(argumento(3, 3, 3))
################################################################
#def caracter(a):
#   if a >= 1:
#     print ('p')
#   else:
#     print('n')
#caracter(1)
#################################################################
#def contar_vezes(letra):
#    vezes = 0
#    for letter in letra:
#        if letter == 'a':
#            vezes = vezes + 1
#    print(vezes)
#
#palavra = str(input('digite :' ))
#contar_vezes(palavra)
########################################################
#def valor(conta):
#    porcento = conta * 0.10
#    print(porcento)
#valor(100.00)
##############################################################
def prefixo(a,b):
    if len(a) > len(b):
        return False
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
        i = i + 1
    return True
palavra = str(input('digite :' ))
palavra1 = str(input('digite :' ))
prefixo(palavra, palavra1)