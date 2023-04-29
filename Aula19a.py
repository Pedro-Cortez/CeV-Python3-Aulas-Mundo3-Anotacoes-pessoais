#Dicionário
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
'''print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''
'''del pessoas['sexo']'''
pessoas['nome'] = 'Pedro'
pessoas['peso'] = 80.0
for k, v in pessoas.items():
    print(f'{k} = {v}')
