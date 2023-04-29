#Listas
num = [2, 5, 9, 1]
num[2] = 3 #Alteração de valores
num.append(7) #Adição de valor
num.sort(reverse=True) #ordenação de valores
num.insert(2, 2) #Insere valor em posição especificada
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
#num.remove(2) #Remove o elemento independente da posição
#num.pop() #Elimina o valor da última posição
#num.pop(2) #Elimina valor em posição especificada
print(num)
print(f'Essa lista tem {len(num)} elementos')
