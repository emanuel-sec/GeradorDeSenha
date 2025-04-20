"""
Gerador de Senhas
Crie um programa que gere uma senha aleatória com letras, números e caracteres especiais.
"""

import random
import string

pontuacao_personalizada = "!#$%&*@"

user = int(input("Escolha uma opção: \n 1 -> 8 caracteres \n 2 -> 12 caracteres \n 3 -> 15 caracteres \n 4 -> 20 caracteres\n: "))
if user == 1:
    senha = ''.join(random.choices(string.ascii_letters + string.digits + pontuacao_personalizada, k=8))
    print(senha)
elif user == 2:
    senha = ''.join(random.choices(string.ascii_letters + string.digits + pontuacao_personalizada, k=12))
    print(senha)
elif user == 3:
    senha = ''.join(random.choices(string.ascii_letters + string.digits + pontuacao_personalizada, k=15))
    print(senha)
elif user == 4:
    senha = ''.join(random.choices(string.ascii_letters + string.digits + pontuacao_personalizada, k=20))
    print(senha)
else:
    print('Opção Inválida!')