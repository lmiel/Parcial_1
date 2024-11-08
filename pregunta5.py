#El patrón de diseño "Observer" permite que un objeto notifique a otros objetos sobre los cambios en su estado. Describa una situación en el contexto de la ingeniería matemática donde este patrón sería útil. Implemente un ejemplo simple de este patrón en Python para ilustrar su respuesta.

#Observer es un patrón de diseño de comportamiento que te permite definir un mecanismo de suscripción para notificar a varios objetos sobre cualquier evento que le suceda al objeto que están observando.

from abc import ABC, abstractmethod

class Sujeto(ABC):    
    def __init__(self):
        self._observadores = []
    
    def agregar_observador(self, observador): #Añade un observador a la lista.
        self._observadores.append(observador)
    
    def eliminar_observador(self, observador):#Elimina un observador de la lista.
        self._observadores.remove(observador)
    
    def notificar_observadores(self, dato): #Notifica a todos los observadores sobre un cambio."""
        for observador in self._observadores:
            observador.actualizar(dato)
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            self.notify()
            
class Observador(ABC):

    @abstractmethod
    def actualizar(self, dato): #Método que se llama cuando el sujeto cambia
        pass


#Imaginemos que estamos desarrollando una aplicación sencilla donde una variable matemática (Variable) puede cambiar su valor, y queremos que diferentes componentes reaccionen automáticamente a estos cambios. 

class DoubleCalculator(Observer):
    
    def update(self, value):
        doble = value * 2
        print(f"DoubleCalculator: El doble de {value} es {doble}.")

class Visualizer(Observer):
    
    def update(self, value):
        print(f"Visualizer: La variable ha sido actualizada a {value}.")

class Variable:
    
    def __init__(self, initial_value=0):
        self._subject = Subject()
        self._subject.value = initial_value
    
    def attach(self, observer):
        self._subject.attach(observer)
    
    def detach(self, observer):
        self._subject.detach(observer)
    
    @property
    def value(self):
        return self._subject.value
    
    @value.setter
    def value(self, new_value):
        self._subject.value = new_value


def main():
    # Crear la variable observada
    variable = Variable(10)
    
    # Crear observadores
    doble_calculator = DoubleCalculator()
    visualizer = Visualizer()
    
    # Registrar observadores
    variable.attach(doble_calculator)
    variable.attach(visualizer)
    
    # Cambiar el valor de la variable
    print("Actualizando la variable a 15:")
    variable.value = 15
    
    print("\nActualizando la variable a 20:")
    variable.value = 20
    
    # Desconectar un observador
    variable.detach(doble_calculator)
    
    print("\nActualizando la variable a 25 (sin DoubleCalculator):")
    variable.value = 25

if __name__ == "__main__":
    main()
