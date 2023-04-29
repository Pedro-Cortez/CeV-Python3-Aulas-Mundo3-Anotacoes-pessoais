#Parâmetros Opcionais

def somar(a=0, b=0, c=1): #O parâmetro igualado a um número qualquer torna-se opcional.
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 3, 5)
somar(3, 3)
somar(3)
somar()

#Escopo de variáveis

def teste():
    x = 8 #Variável de escopo local
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


#programa principal
n = 2 #Variável de escopo global
print(f'No programa principal, n vale {n}.')
teste()
print(f'No programa principal, x vale {x}.') #Comando retornará um erro.
