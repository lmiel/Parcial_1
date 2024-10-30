"""Explique en detalle el principio SOLID "Open/Closed" y proporcione un ejemplo de código en Python donde este principio se ha violado y cómo puede corregirlo.
"""
#El Principio Open/Closed establece que las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para su extensión, pero cerradas para su modificación. En otras palabras, deberíamos poder agregar nuevas funcionalidades sin alterar el código existente.

#Ejemplo de violación del principio Open/Closed:
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class GestorLibros:
    def guardar_libro(self, libro, metodo):
        if metodo == "DB":
            self._guardar_en_db(libro)
        elif metodo == "TXT":
            self._guardar_en_txt(libro)
        else:
            raise ValueError(f"Método de guardado no soportado: {metodo}")

    def _guardar_en_db(self, libro):
        print(f"Guardando '{libro.titulo}' de {libro.autor} en la Base de Datos.")

    def _guardar_en_txt(self, libro):
        print(f"Guardando '{libro.titulo}' de {libro.autor} en un archivo de texto.")

#Este ejemplo viola el principio Open/Closed porque para agregar un nuevo método de guardado, tendríamos que modificar la clase GestorLibros. Por lo que la clase GestorLibros no está cerrada para modificaciones, es decir, necesita ser cambiada para soportar nuevas funcionalidades.

#Corrección del código:
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class GestorLibros:
    def guardar_libro(self, libro, metodo):
        metodo.guardar(libro)

class GuardarEnDB:
    def guardar(self, libro):
        print(f"Guardando '{libro.titulo}' de {libro.autor} en la Base de Datos.")

class GuardarEnTXT:
    def guardar(self, libro):
        print(f"Guardando '{libro.titulo}' de {libro.autor} en un archivo de texto.")

#Ahora, si queremos agregar un nuevo método de guardado, simplemente creamos una nueva clase que implemente el método "guardar" y la pasamos al GestorLibros. De esta manera, la clase GestorLibros está cerrada para modificaciones y abierta para extensiones, cumpliendo así con el principio Open/Closed.
