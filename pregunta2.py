"""Describa el patrón de diseño "Factory". ¿En qué situaciones sería útil este patrón? Proporcione un ejemplo de cómo implementaría este patrón en Python para un problema relacionado con la ingeniería matemática, como la creación de diferentes tipos de funciones matemáticas.
"""

#El patrón de diseño "Factory" es un patrón de diseño creacional, es decir, se encarga de la creación de objetos.  En lugar de instanciar objetos directamente usando sus constructores, se delega la responsabilidad de creación a una "factory" (fábrica), que decide qué clase concreta instanciar en función de ciertos parámetros o condiciones.

#El patrón Factory es útil en situaciones donde se necesita crear un objeto pero no se conoce exactamente qué clase concreta se necesita hasta tiempo de ejecución. Por ejemplo, cuando se necesita crear diferentes tipos de objetos basados en ciertos parámetros o condiciones.

#Ejemplo de implementación:

from abc import ABC, abstractmethod

#Definimos una clase abstracta para las funciones matemáticas
class Funcion(ABC):
    @abstractmethod
    #Evaluar la función en un punto x
    def evaluar(self, x):
        pass

    #Descripción de la función
    @abstractmethod
    def descripcion(self):
        pass

#definimos una clase para las funciones lineales

class FuncionLineal(Funcion):
    def __init__(self, pendiente, ordenada):
        self.pendiente = pendiente
        self.ordenada = ordenada
    
    def evaluar(self, x):
        return self.pendiente * x + self.ordenada

    def descripcion(self):
        return f"Función Lineal: y = {self.pendiente}x + {self.ordenada}"
    

#definimos una clase para las funciones cuadráticas
class FuncionCuadratica(Funcion):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluar(self, x):
        return self.a * x**2 + self.b * x + self.c

    def descripcion(self):
        return f"Función Cuadrática: y = {self.a}x^2 + {self.b}x + {self.c}"

#Factory para crear diferentes tipos de funciones
#La fábrica se encarga de instanciar la clase concreta adecuada en función del tipo de función que se desea crear.
class FuncionFactory:
    #Método estático para crear una función
    #El metodo estatico sirve para no tener que instanciar la clase y poder llamar a la funcion directamente
    @staticmethod
    def crear_funcion(tipo, *args):
        if tipo == "lineal":
            return FuncionLineal(*args)
        elif tipo == "cuadratica":
            return FuncionCuadratica(*args)
        else:
            raise ValueError(f"Tipo de función no soportado: {tipo}")
    
