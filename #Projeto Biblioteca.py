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

estante = Estante()

li = Livro(name='Alice', author='JK Rowling')
li2 = Livro(name='Academia do Grego', author='Platão')

estante.prepend(li)
estante.prepend(li2)

estante.revision()
