print('Bienvenido a la biblioteca')

class book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(sefl):
        if self.availible:
            self.availible = False
            print('El libro {} ha sido prestado'.format(self.title))
        else:
            print('El libro {} no esta disponible'.format(self.title))
    
    def return_book(self):
        self.available = True
        print('El libro {} ha sido devuelto'.format(self.title))
        

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_book = []

    def borrow_books(self,book):
        if book.availible:
            book.borrow()
            self.borrow_books.append(book)
        else:
            print('El libro {} no esta disponible'.format(book.title))
    
    def return_book(self,book):
        if book in self.borrowed_book:
            book.return_book(0)
            self.borrowed_book.remove(book)
        else:
            print('El libro {} no esta en la lista de  prestados'.format(book.title))


class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(sefl, book):
        self.books.append(book)
        print('El libro {} ha sido agregado'.format(book.title))

    def register_user(self, user):
        self.users.append(user)
        print('El usuario {}'.format(user.name))

    def shoe_available_books(self):
        print('Libros disponibles')
        for book in self.books:
            if book.available:
                print(f'{book.title} por {book. author}')


#crear los libros