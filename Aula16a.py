# TUPLAS
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')
print('Comprimento da Tupla lanche:',len(lanche))
'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}.')'''

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi demais!')

#print(sorted(lanche)) #ordenado