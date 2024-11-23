from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, Book


engine = create_engine('sqlite:///library.db')

Session = sessionmaker(bind=engine)

def add_author(name):
    with Session() as session:
        author = Author(name=name)
        session.add(author)
        session.commit()
        ## print(f"Добавлен автор: {author}")
        print(f"Добавлен автор: {author.name}")

def add_book(title, author_name):
    with Session() as session:
        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            print(f"Автор '{author_name}' не найден. Сначала добавьте автора.")
            return
        book = Book(title=title, author=author)
        session.add(book)
        session.commit()
        ## print(f"Добавлена книга: {book}")
        print(f"Добавлена книга: {book.author} '{book.title}'")

def list_authors():
    with Session() as session:
        authors = session.query(Author).all()
        if not authors:
            print("Авторы не найдены")
            return
        for author in authors:
            ## print(author)
            print(f"id({author.id}) {author.name}")

def list_books():
    with Session() as session:
        books = session.query(Book).all()
        if not books:
            print("Книги не найдены")
            return
        for book in books:
            ## print(book)
            print(f"id({book.id}) {book.author} '{book.title}'")

def delete_author(author_name):
    with Session() as session:
        author = session.query(Author).filter_by(name=author_name).first()
        if author:
            session.delete(author)
            session.commit()
            print(f"Автор '{author_name}' и связанные с ним книги удалены.")
        else:
            print(f"Автор '{author_name}' не найден.")

def delete_book(title):
    with Session() as session:
        book = session.query(Book).filter_by(title=title).first()
        if book:
            session.delete(book)
            session.commit()
            print(f"Книга '{title}' удалена.")
        else:
            print(f"Книга '{title}' не найдена.")

def menu():
    while True:
        print("\n=== Меню ===")
        print("1. Добавить автора")
        print("2. Добавить книгу")
        print("3. Список авторов")
        print("4. Список книг")
        print("5. Удалить автора")
        print("6. Удалить книгу")
        print("7. Выход")

        choice = input("Выберете действие:")
        if choice == '1':
            name = input("Введите имя автора: ")
            add_author(name)
        elif choice == '2':
            title = input("Введите название книги: ")
            author_name = input("Введите имя автора: ")
            add_book(title, author_name)
        elif choice == '3':
            list_authors()
        elif choice == '4':
            list_books()
        elif choice == '5':
            author_name = input("Введите имя автора для удаления: ")
            delete_author(author_name)
        elif choice == '6':
            title = input("Введите название книги для удаления: ")
            delete_book(title)
        elif choice == '7':
            print("Выход.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()