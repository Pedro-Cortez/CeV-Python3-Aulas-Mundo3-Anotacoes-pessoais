'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a #unir as tuplas
print(c)
print(len(c)) #tamanho da tupla
print(c.count(5)) #contagem do número 5
print(c.index(8)) #posicão do número 8
print(c.index(5, 1)) #busca a posição do objeto a partir da posição 1'''

#As tuplas aceitam objetos de tipos diferentes:
pessoa = ('Gustavo', 39, 'M', 99.88)
'''del(pessoa) #Apesar de imutável, é possível apagar uma tupla inteira'''
print(pessoa)

'''from random import randint
print(' SORTEANDO DE NÚMEROS '.center(60, '#'))
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}.')
print(f'O menor valor sorteado foi {min(sorteio)}.')'''