from enum import Enum

class tipoPlaneta(Enum):
    "Clase tipoPlaneta que corresponde a una enumeracion"
    GASEOSO = 'G'
    TERRESTRE = 'T'
    ENANO = 'E'

class Planeta:
    """
    Clase Planeta
    """

    def __init__(
            self, tipoPlaneta: tipoPlaneta,
            nombre = None,
            cantidadSatelites = 0,
            masa = 0,
            volumen = 0,
            diametro = 0,
            distanciaSol = 0,
            esObservable = False,
            periodOrbital = 0,
            periodRotacional = 0
    ):
        """
        Constructor de la clase Planeta

        :param nombre Parametro que define el nombre del planeta
        :param cantidadSatelites Parametro que define la cantidad de  
            satelites del planeta
        :param masa Parametro que define la masa del planeta (en  
            kilogramos)
        :param volumen Parametro que define el volumen del planeta  
            (en kilometros cubicos)
        :param diametro Parametro que define el diametro del planeta  
            (en kilometros)
        :param distanciaSol Parametro que define la distancia media del  
            planeta al sol (en kilometros)
        :param tipo Parametro que define el tipo de planeta (puede ser  
            GASEOSO, TERRESTRE o ENANO)
        :param esObservable Parametro que define si el planeta es  
            observable o no
        :param periodOrbital Parametro que define el periodo orbital (en
            anos)
        :param periodRotacional Parametro que define el periodo
            rotacional (en dias) 
        """
        self.tipoPlaneta = tipoPlaneta
        self.nombre = nombre
        self.cantidadSatelites = cantidadSatelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distanciaSol = distanciaSol
        self.esObservable = esObservable
        self.periodOrbital = periodOrbital
        self.periodRotacional = periodRotacional


    def imprimir(self):
        """Metodo que imprime en pantalla los datos de un planeta"""
        print("Nombre del planeta: ", self.nombre)
        print("Cantidad de satelites: ", self.cantidadSatelites)
        print("Masa del planeta: ", self.masa)
        print("Volumen del planeta: ", self.volumen)
        print("Diametro del planeta: ", self.diametro)
        print("Distancia al sol: ", self.distanciaSol)
        print("Tipo de planeta: ", self.tipoPlaneta.value)
        print("Periodo orbital: ", self.periodOrbital, " anos")
        print("Periodo de rotacion: ", self.periodRotacional, " dias")
        print()


    def clacular_densidad(self):
        """Metodo que calcula y devuelve la densidad d eun planeta."""
        return self.masa / self.volumen    


    def es_planeta_exterior(self):
        """Metodo que determina y devuelve si un planeta es exterior o no."""
        limite = 149597870 * 3.4
        if self.distanciaSol > limite:
            return True
        else:
            return False

class POO202502_A02_E22:
    @staticmethod
    def main():
        p1 = Planeta(tipoPlaneta.TERRESTRE, "Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, True, 3, 321) 
        p1.imprimir()
        print(f"Densidad del planeta: {p1.clacular_densidad()}")
        print(f"Es planeta exterior: {p1.es_planeta_exterior()}")
        print()
        p2 = Planeta(tipoPlaneta.GASEOSO, "Jupiter", 79, 1.899E27, 1.4313E15, 139820, 750000000, True, 7, 125)
        p2.imprimir()
        print(f"Densidad del planeta: {p2.clacular_densidad()}")
        print(f"Es planeta exterior: {p2.es_planeta_exterior()}")


if __name__ == "__main__":
    POO202502_A02_E22.main()

