# Projeto biblioteca

class Livros:


    def __init__(self, prev=None, next=None, name=None, author=None):
        self.prev = prev
        self.next = next
        self.name = name
        self.author = author

class Biblioteca:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_livro=Livros):
        if self.head is None:
            self.head = new_livro
            self.tail = new_livro
            return
        
        new_livro.prev = self.tail
        self.tail.next = new_livro
        self.tail = new_livro

    def prepend(self, new_livro=Livros):

        if self.head is None:
            self.head = new_livro
            self.tail = new_livro
            return

        new_livro.next = self.head
        self.head.prev = new_livro
        self.head = new_livro
        if self.head.next is not None:
            print('=' * 50)
            print(f'Você está colocando o livro {self.head.next.name} do autor {self.head.next.author} no inicio da prateleira! Obrigado! ')
            print('=' * 50)
        else:
            print('=' * 50)
            print(f'Você está colocando o primeiro livro na prateleira! Obrigado! ')
            print('=' * 50)

    def revision(self):
        current = self.head
        while current is not None:
            print(f'O nome do livro é: {current.name}')
            print(f'E seu autor é : {current.author}')
            current = current.next

list = Biblioteca()

li = Livros(name='Alice', author='JK Rowling')

list.prepend(li)

list.revision()
