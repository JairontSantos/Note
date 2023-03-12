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
        self.head.prev = None

    def revision(self):
        current = self.head
        contagem = 0
        while current is not None:
            print(f'O nome do livro é: {current.name}')
            print(f'E seu autor é : {current.author}')
            print('=' * 55)
            current = current.next
            contagem += 1
        print(f'A quantidade de livros na estante é {contagem}!')
        print('=' * 55)

list = Estante()

li = Livro(name='Alice', author='JK Rowling')
li1 = Livro(name='Minecraft', author='N/A')
li2 = Livro(name='JoJo', author='Araki')
li3 = Livro(name='1984', author='Não sei')

list.prepend(li)
list.prepend(li2)
list.prepend(li1)
list.append(li3)

list.remove_last()
list.remove_last()
list.remove_first()


list.revision()
