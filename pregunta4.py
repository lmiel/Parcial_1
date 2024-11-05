#Los principios DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid) son fundamentales para escribir código de alta calidad. Proporcione un ejemplo de un fragmento de código Python que viole estos principios. Describa cómo lo refactorizaría para adherirse a los principios DRY y KISS.

#Un ejemplo de un fragmento de código que viola los principios DRY y KISS es el siguiente:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def register(self):
        # Lógica para registrar al usuario en la base de datos
        print(f"Usuario '{self.name}' registrado con el correo '{self.email}'.")
    
    def login(self):
        # Lógica para autenticar al usuario
        print(f"Usuario '{self.name}' autenticado.")
        
    def send_email(self, subject, message):
        # Lógica para enviar un correo electrónico
        print(f"Correo enviado a '{self.email}' con el asunto '{subject}' y el mensaje '{message}'.")
        
class  Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def register(self):
        # Lógica para registrar al administrador en la base de datos
        print(f"Administrador '{self.name}' registrado con el correo '{self.email}'.")
    
    def login(self):
        # Lógica para autenticar al administrador
        print(f"Administrador '{self.name}' autenticado.")
        
    def send_email(self, subject, message):
        # Lógica para enviar un correo electrónico
        print(f"Correo enviado a '{self.email}' con el asunto '{subject}' y el mensaje '{message}'.")
        
#Este código viola el principio DRY (Don't Repeat Yourself) porque la clase User y la clase Admin tienen métodos y atributos similares, pero están duplicados en ambas clases. Además, viola el principio KISS (Keep It Simple, Stupid) porque la lógica para registrar, autenticar y enviar correos electrónicos está mezclada en las clases, lo que las hace más complejas de lo necesario.

#Para adherirse a los principios DRY y KISS, se podría refactorizar el código de la siguiente manera:

class Persona:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def get_name(self): 
        return self.name
    
    def get_email(self):
        return self.email
    
    def register(self):
        # Lógica para registrar a la persona en la base de datos
        print(f"Persona '{self.name}' registrada con el correo '{self.email}'.")
        
    def login(self):
        # Lógica para autenticar a la persona
        print(f"Persona '{self.name}' autenticada.")
        
    def send_email(self, subject, message):
        # Lógica para enviar un correo electrónico
        print(f"Correo enviado a '{self.email}' con el asunto '{subject}' y el mensaje '{message}'.")

class User(Persona):
    def __init__(self, name, email):
        super().__init__(name, email)
        
class Admin(Persona):
    def __init__(self, name, email):
        super().__init__(name, email)
    