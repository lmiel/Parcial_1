#Explique el antipatrón "God Object". ¿Por qué es perjudicial este antipatrón y qué problemas puede causar en el desarrollo de software? Proporcione un ejemplo de un "God Object" en un contexto de ingeniería matemática y explique cómo podría refactorizarlo para evitar este antipatrón.

#El antipatron "God Object" se trata de una clase que tiene demasiadas responsabilidades, es decir, que tiene demasiados métodos y atributos. Esto es perjudicial porque hace que el código sea dificil de mantener y de entender, ya que es dificil de seguir el flujo del programa. 
#También como muchas otras clases dependen de esta clase, si se quiere cambiar algo en esta clase, se tiene que cambiar en todas las clases que dependen de ella (alto acoplamiento), esto que hace que el código sea dificil de mantener y de reutilizar debido además a su gran complejidad.
# Por último, hace que el código sea dificil de testear, ya que al tener tantas responsabilidades, es dificil de probar cada una de ellas.

#Un ejemplo de un "God Object" en un contexto de ingeniería matemática  sería una clase que tenga métodos para crear matrices, mostrar matrices, sumar matrices y resolver sistemas de ecuaciones.
class MatrixCalculator:
    def __init__(self):
        self.matrices = {}
        self.resultados = {}
    
    def crear_matriz(self, nombre, filas, columnas, valores=None):
            if valores is None:
                valores = [[0 for _ in range(columnas)] for _ in range(filas)]
            self.matrices[nombre] = valores
            print(f"Matriz '{nombre}' creada con tamaño {filas}x{columnas}.")
        
        def mostrar_matriz(self, nombre):
            matriz = self.matrices.get(nombre)
            if matriz:
                print(f"Matriz '{nombre}':")
                for fila in matriz:
                    print(fila)
            else:
                print(f"Matriz '{nombre}' no encontrada.")
        
        def sumar_matrices(self, nombre1, nombre2, resultado):
            matriz1 = self.matrices.get(nombre1)
            matriz2 = self.matrices.get(nombre2)
            if not matriz1 or not matriz2:
                print("Una o ambas matrices no existen.")
                return
            filas = len(matriz1)
            columnas = len(matriz1[0])
            suma = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)]
            self.matrices[resultado] = suma
            print(f"Matrices '{nombre1}' y '{nombre2}' sumadas en '{resultado}'.")
        
        # Métodos para resolver sistemas de ecuaciones
        def resolver_sistema_ecuaciones(self, matriz, vector, resultado):
            try:
                import numpy as np
                A = np.array(self.matrices.get(matriz))
                b = np.array(vector)
                sol = np.linalg.solve(A, b)
                self.resultados[resultado] = sol.tolist()
                print(f"Solución del sistema '{matriz}x = {vector}': {sol.tolist()}")
            except Exception as e:
                print(f"Error al resolver el sistema de ecuaciones: {e}")


#Para refactorizarlo, se podría dividir la clase en varias clases, una para crear matrices, otra para mostrar matrices, otra para sumar matrices y otra para resolver sistemas de ecuaciones. De esta forma, cada clase tendría una sola responsabilidad y sería más fácil de mantener y de entender. Además, se podría utilizar la inyección de dependencias para que las clases dependan de interfaces en lugar de clases concretas, lo que permitiría cambiar la implementación de una clase sin afectar a las demás.

class MatrixCreator:
    def __init__(self):
        self.matrices = {}
    
    def crear_matriz(self, nombre, filas, columnas, valores=None):
        if valores is None:
            valores = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.matrices[nombre] = valores
        print(f"Matriz '{nombre}' creada con tamaño {filas}x{columnas}.")
        
class MatrixViewer:
    def __init__(self, matrix_creator):
        self.matrix_creator = matrix_creator
    
    def mostrar_matriz(self, nombre):
        matriz = self.matrix_creator.matrices.get(nombre)
        if matriz:
            print(f"Matriz '{nombre}':")
            for fila in matriz:
                print(fila)
        else:
            print(f"Matriz '{nombre}' no encontrada.")
            
class MatrixAdder:
    def __init__(self, matrix_creator):
        self.matrix_creator = matrix_creator
    
    def sumar_matrices(self, nombre1, nombre2, resultado):
        matriz1 = self.matrix_creator.matrices.get(nombre1)
        matriz2 = self.matrix_creator.matrices.get(nombre2)
        if not matriz1 or not matriz2:
            print("Una o ambas matrices no existen.")
            return
        filas = len(matriz1)
        columnas = len(matriz1[0])
        suma = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)]
        self.matrix_creator.matrices[resultado] = suma
        print(f"Matrices '{nombre1}' y '{nombre2}' sumadas en '{resultado}'.")
        
class EquationSolver:
    def __init__(self, matrix_creator):
        self.matrix_creator = matrix_creator
        self.resultados = {}
    
    def resolver_sistema_ecuaciones(self, matriz, vector, resultado):
        try:
            import numpy as np
            A = np.array(self.matrix_creator.matrices.get(matriz))
            b = np.array(vector)
            sol = np.linalg.solve(A, b)
            self.resultados[resultado] = sol.tolist()
            print(f"Solución del sistema '{matriz}x = {vector}': {sol.tolist()}")
        except Exception as e:
            print(f"Error al resolver el sistema de ecuaciones: {e}")