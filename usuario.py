class Usuario:
    def __init__(self,nombre, email, password):
        self.nombre=nombre
        self.email=email
        self.password=password
    
    def toDBCollection(self):
        return{
            'nombre': self.nombre,
            'email': self.email,
            'password': self.password,
            
        }  
