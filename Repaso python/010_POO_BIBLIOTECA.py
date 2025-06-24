class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if  self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")

        else: 
            print(f"El libro {self.title}, No esta disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title}, ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        
        else:
            print("El libro {self.title} no esta disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"Este libro {book.title} no esat en tu coleccion d elibros") 

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agregado con exito')

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido agregado")
        
    def show_available_books(self):
        print("Libros disponibles")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

#crear los libros
libro1=book('Los pesares de un hombre','Juan Daniel')
libro2=book('1994','George Orwell')
libro3=book('El arte de la guerra','Sun Tzu')

#crar usuarios
usuario=User('Juan D','001')

#crear biblioteca
librari = Library()

#agragando libros a la biblioteca
librari.add_book(libro1)
librari.add_book(libro2)
librari.add_book(libro3)

#registar usuarios 
librari.register_user(usuario)

#mostrar libros disponibles
librari.show_available_books()

#realizar prestamo
usuario.borrow_book(libro1)

#mostrar libros disponibles
librari.show_available_books()

#devolver un libro
usuario.return_book(libro1)

#mostrar libros disponibles
librari.show_available_books()