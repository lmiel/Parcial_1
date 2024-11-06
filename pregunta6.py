"""Se le proporciona un fragmento de código Python que maneja diferentes tipos de formas geométricas. Actualmente, el código viola el Principio de Responsabilidad Única (SRP) y el Principio Abierto/Cerrado (OCP) de SOLID. Su tarea es refactorizar este código para que se adhiera a estos principios.


class Shape:
    def __init__(self, type):
        self.type = type

class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            if shape.type == "circle":
                radius = 1.0  # Supongamos que el radio es siempre 1 para este ejemplo
                total += 3.14159 * radius * radius
            elif shape.type == "square":
                side = 1.0  # Supongamos que el lado es siempre 1 para este ejemplo
                total += side * side
        return total

shapes = [Shape("circle"), Shape("square")]
calculator = AreaCalculator(shapes)
print(calculator.total_area())
Pregunta Práctica 2: Implementación de Patrón de Diseño Estrategia(2,5 Puntos)

En ingeniería matemática, es común que necesitemos intercambiar diferentes algoritmos dependiendo de la situación. Considere una aplicación que debe realizar la integración numérica de una función. Hay diferentes métodos para realizar esta integración, como el método del trapecio, el método de Simpson, la cuadratura gaussiana, entre otros.

Se le pide que implemente este escenario utilizando el patrón de diseño estrategia. Debe proporcionar una estructura que permita cambiar fácilmente el método de integración. Incluya al menos dos métodos específicos (por ejemplo, Trapecio y Simpson) y demuestre cómo se podrían cambiar estos métodos en tiempo de ejecución.
"""

class Shape():
    def calcular_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    def calcular_area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side=1):
        self.side = side

    def calcular_area(self):
        return self.side * self.side

class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calcular_area()
        return total
