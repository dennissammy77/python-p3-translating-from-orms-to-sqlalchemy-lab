from models import Dog
from sqlalchemy import (
    create_engine
)
def create_table(base,engine):
    engine = create_engine('sqlite:///dogs.db')
    base.metadata.create_all(engine)

def save(session, dog):
    if isinstance(dog, Dog):
        session.add(dog)
        session.commit()
    pass

def get_all(session):
    return session.query(Dog)

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()

def find_by_id(session, id):
    return session.query(Dog).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(name),Dog.breed.like(breed)).first()

def update_breed(session, dog, breed):
    for d in session.query(Dog).filter(Dog.name.like(dog.name)):
        print(d)
        d.breed = breed
    
    session.commit()