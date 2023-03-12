# Projeto biblioteca

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

    def append(self, new_livro: Livro):
        
        if self.head is None:
            print('=' * 55)
            print(f'Você está colocando o primeiro livro na prateleira! Obrigado!')
            print('=' * 55)
        else: 
            print(f'Você está colocando o livro: {self.head.name}, do autor: {self.head.author}, no final da prateleira! Obrigado! ')
            print('=' * 55)
        
        if self.head is None:
            self.head = new_livro
            self.tail = new_livro
            return
        
        new_livro.prev = self.tail
        self.tail.next = new_livro
        self.tail = new_livro

    def prepend(self, new_livro: Livro):

        if self.head is None:
            print('=' * 55)
            print(f'Você está colocando o primeiro livro na prateleira! Obrigado!')
            print('=' * 55)
        else: 
            print(f'Você está colocando o livro: {self.head.name}, do autor: {self.head.author}, no inicio da prateleira! Obrigado! ')
            print('=' * 55)

        if self.head is None:
            self.head = new_livro
            self.tail = new_livro
            return

        new_livro.next = self.head
        self.head.prev = new_livro
        self.head = new_livro

    def remove_end(self):
        if self.head is None:  # Lista vazia
            return
        
        if self.head.prev and self.head.next is None:  # A lista tem apenas um nó
            self.head = None
            self.tail = None
            return

        print(f'Você está tirando o livro: {self.head.name}, do final da estante!')
        print('=' * 55)

        self.tail = self.tail.prev
        self.tail.next = None



    def remove_beginning(self):
        if self.head is None:
            return 0
        
        if self.head.prev and self.head.next is None:
            self.head = None
            self.tail = None
            return 
        
        print(f'Você está tirando o livro: {self.head.name}, do ínicio da estante!')
        print('='* 55)

        NotImplemented


    def revision(self):
        contagem = 0
        current = self.head
        while current is not None:
            print(f'O nome do livro é: {current.name}')
            print(f'E seu autor é : {current.author}')
            current = current.next
            print('=' * 55)
            contagem += 1
        print(f'Estamos no momento com {contagem} livros na estante')
        print('=' * 55)

estante = Estante()

li = Livro(name='Alice', author='JK Rowling')
li2 = Livro(name='Academia do Grego', author='Platão')
li3 = Livro(name='Diário de um Banana', author='N/A')
li4 = Livro(name='Manga JoJo', author='Araki')

estante.prepend(li)
estante.prepend(li2)
estante.append(li3)

estante.remove_end()

estante.revision()
