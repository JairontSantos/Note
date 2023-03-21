# Projeto biblioteca

import time

class Livro:

    def __init__(self, prev=None, next=None, name=None, author=None):
        self.prev = prev
        self.next = next
        self.name = name
        self.author = author

class Estante:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_livro:Livro):

        if self.head is None:
            print('=' * 55)
            print(f'Você está colocando o primeiro livro na prateleira! Obrigado! ')

        if self.head is None:
            self.head = new_livro
            self.tail = new_livro
            return

        new_livro.prev = self.tail
        self.tail.next = new_livro
        self.tail = new_livro

        print('=' * 55)
        print(f'Você está colocando o livro {self.tail.name} do autor {self.tail.author} no final da prateleira! Obrigado! ')

    def prepend(self, new_livro:Livro):

        if self.head is None:
            print('=' * 55)
            print(f'Você está colocando o primeiro livro na prateleira! Obrigado! ')
            self.head = new_livro
            self.tail = new_livro
            return

        new_livro.next = self.head
        self.head.prev = new_livro
        self.head = new_livro

        print('=' * 55)
        print(f'Você está colocando o livro {self.head.name} do autor {self.head.author} no inicio da prateleira! Obrigado! ')

    def remove_last(self):

        if self.head is None:
            print(f'=' * 55)
            print('Não possui nenhum livro na estante para tirar!')
            return
        
        if self.head.next is None: 
            self.head = None
            self.tail = None
            return

        print('=' * 55)
        print(f'Você está tirando o livro: {self.tail.name}, do autor {self.tail.author} do final da estante!')

        self.tail = self.tail.prev
        self.tail.next = None

    def remove_first(self):
        if self.head is None:
            print('Não possui nenhum livro na estante para tirar!')
            print(f'=' * 55)
            return 
        
        if self.head.prev and self.head.next is None:
            self.head = None
            self.tail = None
            return 
        
        print('=' * 55)
        print(f'Você está tirando o livro: {self.head.name}, do autor {self.head.author} do ínicio da estante!')
        print('='* 55)

        self.head = self.head.next

    def search(self, name):
        current = self.head
        while current is not None:
            if current.name == name:
                print(f'O livro {current.name} foi encontrado!')
                print('=' * 55)
                return current
            current = current.next
        print(f'O livro {name} não foi encontrado!')
        print('=' * 55)
        return None

    def remove(self, name):
        livro = self.search(name)
        if livro is None:
            return
        if livro.prev is None:
            self.remove_first()
            return
        if livro.next is None:
            self.remove_last()
            return
        livro.prev.next = livro.next
        livro.next.prev = livro.prev
        print(f'O livro {livro.name} foi removido!')
        print('=' * 55)
        return livro

    def revision(self):
        current = self.head
        contagem = 0
        while current is not None:
            print('=' * 55)
            print(f'O nome do livro é: {current.name}')
            print(f'E seu autor é : {current.author}')
            print('=' * 55)
            current = current.next
            contagem += 1
        print('=' * 55)
        print(f'A quantidade de livros na estante é {contagem}!')
        print('=' * 55)

estante = Estante()

def menu():
    print('=' * 55)
    print('Bem vindo a Estante Virtual!')
    print('=' * 55)
    print('Escolha uma opção:')
    print('1 - Adicionar um livro no final da estante')
    print('2 - Adicionar um livro no começo da estante')
    print('3 - Remover um livro do final da estante')
    print('4 - Remover um livro do começo da estante')
    print('5 - Procurar um livro')
    print('6 - Remover um livro')
    print('7 - Listar os livros')
    print('8 - Sair')
    print('=' * 55)

def main():
    while True:
        menu()
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            name = input('Digite o nome do livro: ')
            author = input('Digite o nome do autor: ')
            livro = Livro(name=name, author=author)
            estante.append(livro)
            tempo()
        elif opcao == 2:
            name = input('Digite o nome do livro: ')
            author = input('Digite o nome do autor: ')
            livro = Livro(name=name, author=author)
            estante.prepend(livro)
            tempo()
        elif opcao == 3:
            estante.remove_last()
            tempo()
        elif opcao == 4:
            estante.remove_first()
            tempo()
        elif opcao == 5:
            name = input('Digite o nome do livro: ')
            estante.search(name)
            tempo()
        elif opcao == 6:
            name = input('Digite o nome do livro: ')
            estante.remove(name)
            tempo()
        elif opcao == 7:
            estante.revision()
            tempo()
        elif opcao == 8:
            break
        else:
            print('Opção inválida!')
            tempo()

def tempo():
    time.sleep(3)


main()
