from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

p1 = Pet(name='Sparky', species='dog', photo_url='images/IMG_1403.jpeg',
         age=1, notes='none', available=0)

p2 = Pet(name='Spot', species='dog',
         photo_url='images/IMG_1341.jpeg', age=1, notes='none', available=0)

db.session.add(p1)
db.session.add(p2)
db.session.commit()





# name = db.Column(db.Text, nullable=False)
#    species = db.Column(db.Text, nullable=False)
#     photo_url = db.Column(db.Text)
#     age = db.Column(db.Integer)
#     notes = db.Column(db.Text)
#     available = db.Column(db.Boolean)
