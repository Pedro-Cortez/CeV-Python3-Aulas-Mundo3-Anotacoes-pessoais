try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print(f'Impossível dividir um número por zero.')
except KeyboardInterrupt:
    print(f'O usuário não informou os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}.')
finally:
    print(f'Volte sempre! Muito Obrigado.')
