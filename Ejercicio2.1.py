

class Persona:

    def __init__(self, nombre, apellidos, numero_documento_identidad,
                 pais_nacimiento, genero, anio_nacimiento):
        """
        Constructor de la clase Persona

        :param nombre: Nombre de la persona
        :param apellidos: Apellidos de la persona
        :param numero_documento_identidad: Numero de documento de identidad
        :param pais_nacimiento: Pais de nacimiento
        :param genero: Genero de la persona ('H' o 'M')
        :param anio_nacimiento: Ano de nacimiento
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self):
        """Metodo que imprime en pantalla los datos de una persona"""
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Numero de documento de identidad =", self.numero_documento_identidad)
        print("Pais de nacimiento =", self.pais_nacimiento)
        print("Genero =", self.genero)
        print("Ano de nacimiento =", self.anio_nacimiento)
        print()


class POO202502_A02_E21:
    @staticmethod
    def main():
        p1 = Persona("Pedro", "Perez", "1053121010", "Colombia", "H", 1998)
        p2 = Persona("Luis", "Leon", "1053223344", "Argentina", "H", 2001)

        p1.imprimir()
        p2.imprimir()


if __name__ == "__main__":
    POO202502_A02_E21.main()
