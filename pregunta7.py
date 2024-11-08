#Se le pide que implemente este escenario utilizando el patrón de diseño estrategia. Debe proporcionar una estructura que permita cambiar fácilmente el método de #integración. Incluya al menos dos métodos específicos (por ejemplo, Trapecio y Simpson) y demuestre cómo se podrían cambiar estos métodos en tiempo de ejecución.

class EstrategiaIntegracion():
    def integrar(self, f, a, b, n):
        pass

class EstrategiaTrapecio(EstrategiaIntegracion):
    def integrar(self, f, a, b, n):
        h = (b - a) / n
        suma = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            suma += f(a + i * h)
        return h * suma

class EstrategiaSimpson(EstrategiaIntegracion):
    def integrar(self, f, a, b, n):
        h = (b - a) / n
        suma = f(a) + f(b)
        for i in range(1, n, 2):
            suma += 4 * f(a + i * h)
        for i in range(2, n-1, 2):
            suma += 2 * f(a + i * h)
        return (h / 3) * suma

class Integrador:
    def __init__(self, estrategia: EstrategiaIntegracion):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaIntegracion):
        self.estrategia = estrategia

    def calcular_integral(self, f, a, b, n):
        return self.estrategia.integrar(f, a, b, n)

def funcion_ejemplo(x):
    return x**2

if __name__ == "__main__":
    integrador = Integrador(EstrategiaTrapecio())
    
    resultado_t = integrador.calcular_integral(funcion_ejemplo, 0, 1, 1000)
    print(f"Resultado con estrategia trapecio: {resultado_t}")
    
    integrador.set_estrategia(EstrategiaSimpson())
    
    resultado_s = integrador.calcular_integral(funcion_ejemplo, 0, 1, 1000)
    print(f"Resultado con estrategia simpson: {resultado_s}")```
