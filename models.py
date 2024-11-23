from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author", cascade="all, delete")

    def __repr__(self):
        return self.name
    
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship("Author", back_populates="books")

    ## def __repr__(self):
    ##     return f"<Book(id={self.id}, title='{self.title}', author({self.author}))"
    