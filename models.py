from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    all = []

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)
    fav_genre = Column('favorite genre', String)
    email = Column('email', String)
    phone_number = Column('phone number', Integer)

    def __repr__(self):
        return f'''
            id: {self.id}
            name: {self.name},
            age:{self.age},
            fav_genre:{self.fav_genre},
            email:{self.email},
            phone_number:{self.phone_number}
        '''
    

class Books(Base):
    __tablename__ = 'books'

    all = []

    id = Column(Integer(), primary_key=True)
    title = Column('title', String())
    author = Column('author', String())
    read = Column('read', String())

    def __repr__(self):
        return f'''
            id: {self.id},
            title: {self.title},
            author: {self.author},
            read: {self.read}
        '''

class Reviews(Base):
    __tablename__ = 'reviews'

    all = []

    id = Column(Integer(), primary_key=True)
    review = Column('review', String())
    rating = Column('rating out of 5', Integer())
    book_id = Column(Integer(), ForeignKey('books.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

    def __repr__(self):
        return f'''
            review: {self.review},
            rating: {self.rating},
            book_id: {self.book_id},
            user_id: {self.user_id}
        '''

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)