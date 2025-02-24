from sqlalchemy import String, Integer, Float, Column, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class BooksLibrary(Base):
    """Creating a db class using declarative base"""
    __tablename__ = "books"
    book_id = Column("book_id", Integer, primary_key=True, auto_increment=True)
    book_title = Column("book_title", String, nullable=False, unique=True)
    book_author = Column("book_author", String, nullable=False)
    book_rating = Column("book_rating", Float, nullable=False)

    def __init__(self, book_title, book_author, book_rating):
        super().__init__()
        self.book_title = book_title.title()
        self.book_author = book_author.title()
        self.book_rating = float(book_rating)

    def __repr__(self):
        return f"{self.book_id} {self.book_title} {self.book_author} {self.book_rating}"

# Creating a db
engine = create_engine("sqlite:///books-collection.db", echo=True)
Base.metadata.create_all(bind=engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

def get_all_books():
    return [{"title":book.book_title, "author":book.book_author, "rating":book.book_rating} for book in session.query(BooksLibrary).all()]

def create_book(title, author, rating):
    book = BooksLibrary(title, author, rating)
    session.add(book)
    session.commit()

def delete_book(title):
    """Given a book's title it deletes the book
    from the db else returns -1"""
    book_title = title.title()
    query_response = session.query(BooksLibrary).filter_by( book_title = book_title).first()
    if query_response:
        session.delete(query_response)
        session.commit()
        return True
    else:
        return False

def change_rating(book_title, rating):
    """Given the book_title and its rating
    changes the books rating, else returns -1"""
    book_title = book_title.title()
    query_response = session.query(BooksLibrary).filter_by( book_title = book_title).first()
    if query_response:
        query_response.book_rating = rating
        session.commit()
        return True
    else:
        return False

# create_book("green country", "sown mower", 4)
# book = "Green country"
# book_title = book.title()
# query_response = session.query(BooksLibrary).filter_by( book_title = book_title).first()
# if query_response:
#     session.delete(query_response)
#     session.commit()
# print(get_all_books())
