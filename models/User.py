from config import db #SQLALCHEMY ES EL ORM PARA HACER LA TABLA
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)

    def __init__(self): #NO ES NECESARIO QUE LO VUELVAS A LLAMAR (SELF)
        self.name = name
        self.email = email
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
        }