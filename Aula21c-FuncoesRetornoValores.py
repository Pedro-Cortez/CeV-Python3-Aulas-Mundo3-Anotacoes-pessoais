def somar(a=0, b=0, c=0):
    s = a + b + c
    return s #Envia o resultado da soma para as variáveis r(1,2,3) do programa principal.


#Programa principal
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Os resultados das somas foram {r1}, {r2} e {r3}.')


#Aplicação Prática
def fatorial(num=1):
    f = 1
    for cont in range(num, 0, -1):
        f = f * cont
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
