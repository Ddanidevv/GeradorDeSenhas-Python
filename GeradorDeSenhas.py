'''
Gerador de senhas difíceis em python.
Python Orientado a objetos e algumas bibliotecas internas.
'''
import string
import random


class Senha:

    senha = []            #Barril
    nova_senha = ''              

    def __init__(self, num_char=8, contexto='email', nome= 'um desconhecido'):
        self.nome = nome
        self.num_char = int(num_char)
        self.contexto = contexto

    def gerar_senha(self):
        '''
        CAMADA 1: NÚMERO ALEATÓRIO
        CAMADA 2: LETRA ALEATÓRIA
        '''
        for i in range(self.num_char):
            if i % 2 == 0:               #NÚMERO PAR
                self.senha.append(random.randint(0, 9))
            if i % 2 == 1:               #NÚMERO ÍMPAR
                self.senha.append(random.choice(string.ascii_letters))
        for char in self.senha:
            self.nova_senha += f'{char}'
        return print(f'A senha do {self.contexto} de {self.nome} = {self.nova_senha}')


if __name__ == "__main__":
    maria = Senha(8, 'Senha', 'criada')
    maria.gerar_senha()


'''
Banco de dados SQLite3 para guardar os dados.
GUI.
'''