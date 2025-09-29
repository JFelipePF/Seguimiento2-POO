import math




# Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

# Rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2  

    def perimetro(self):
        return 4 * self.lado

# Triángulo rectángulo
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def tipo_triangulo(self):
        lado1 = self.base
        lado2 = self.altura
        lado3 = self.hipotenusa()

        if math.isclose(lado1, lado2) and math.isclose(lado2, lado3):
            return "Equilátero"
        elif math.isclose(lado1, lado2) or math.isclose(lado2, lado3) or math.isclose(lado1, lado3):
            return "Isósceles"
        else:
            return "Escaleno"


# Clase de prueb
class POO202502_A02_E24:
    @staticmethod
    def main():
        # Crear figuras
        circulo = Circulo(1)
        rectangulo = Rectangulo(2, 4)
        cuadrado = Cuadrado(5)
        triangulo = TrianguloRectangulo(4, 4)
    
        # Mostrar resultados
        print("Círculo:")
        print(f"Área: {circulo.area():.2f} cm²")
        print(f"Perímetro: {circulo.perimetro():.2f} cm")
    
        print("\nRectángulo:")
        print(f"Área: {rectangulo.area():.2f} cm²")
        print(f"Perímetro: {rectangulo.perimetro():.2f} cm")
    
        print("\nCuadrado:")
        print(f"Área: {cuadrado.area():.2f} cm²")
        print(f"Perímetro: {cuadrado.perimetro():.2f} cm")
    
        print("\nTriángulo Rectángulo:")
        print(f"Área: {triangulo.area():.2f} cm²")
        print(f"Perímetro: {triangulo.perimetro():.2f} cm")
        print(f"Hipotenusa: {triangulo.hipotenusa():.2f} cm")
        print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")

if __name__ == "__main__":
    POO202502_A02_E24.main()
