# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 11:58:59 2025

@author: 65681
"""

#Ejercicio 2.3
from enum import Enum

# Enumeraciones
class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"

class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"

class Automovil:
    def __init__(self, marca: str, modelo: int, motor: int,
                 tipoCombustible: TipoCom, tipoAutomovil: TipoA,
                 numeroPuertas: int, cantidadAsientos: int,
                 velocidadMaxima: int, color: TipoColor, automatico: bool):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAutomovil = tipoAutomovil
        self.numeroPuertas = numeroPuertas
        self.cantidadAsientos = cantidadAsientos
        self.velocidadMaxima = velocidadMaxima
        self.color = color
        self.velocidadActual = 0
        self.automatico = automatico
        self.cantidadMultas = 0
        self.valorMulta = 100000

    # Getters (en Python se suele acceder directo, pero se pueden hacer metodos)
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getMotor(self):
        return self.motor

    def getTipoCombustible(self):
        return self.tipoCombustible

    def getTipoAutomovil(self):
        return self.tipoAutomovil

    def getNumeroPuertas(self):
        return self.numeroPuertas

    def getCantidadAsientos(self):
        return self.cantidadAsientos

    def getVelocidadMaxima(self):
        return self.velocidadMaxima

    def getColor(self):
        return self.color

    def getVelocidadActual(self):
        return self.velocidadActual

    def getAutomatico(self):
        return self.automatico

    # Setters
    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setMotor(self, motor):
        self.motor = motor

    def setTipoCombustible(self, tipoCombustible: TipoCom):
        self.tipoCombustible = tipoCombustible

    def setTipoAutomovil(self, tipoAutomovil: TipoA):
        self.tipoAutomovil = tipoAutomovil

    def setNumeroPuertas(self, numeroPuertas):
        self.numeroPuertas = numeroPuertas

    def setCantidadAsientos(self, cantidadAsientos):
        self.cantidadAsientos = cantidadAsientos

    def setVelocidadMaxima(self, velocidadMaxima):
        self.velocidadMaxima = velocidadMaxima

    def setColor(self, color: TipoColor):
        self.color = color

    def setVelocidadActual(self, velocidadActual):
        self.velocidadActual = velocidadActual

    def setAutomatico(self, automatico: bool):
        self.automatico = automatico

    # Metodos funcionales
    def acelerar(self, incrementoVelocidad: int):
        if self.velocidadActual + incrementoVelocidad < self.velocidadMaxima:
            self.velocidadActual += incrementoVelocidad
        else:
            self.cantidadMultas += 1
            print("No se puede incrementar a una velocidad superior a la maxima del automovil.")
            print(f"Multa # {self.cantidadMultas} generada.")

    def desacelerar(self, decrementoVelocidad: int):
        if (self.velocidadActual - decrementoVelocidad) > 0:
            self.velocidadActual -= decrementoVelocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidadActual = 0

    def calcularTiempoLlegada(self, distancia: int) -> float:
        if self.velocidadActual == 0:
            return float('inf')  # evitar division por cero
        return distancia / self.velocidadActual

    def tieneMultas(self) -> bool:
        return self.cantidadMultas > 0

    def valorTotalMultas(self) -> float:
        return self.cantidadMultas * self.valorMulta

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipoCombustible.name}")
        print(f"Tipo de automovil = {self.tipoAutomovil.name}")
        print(f"Numero de puertas = {self.numeroPuertas}")
        print(f"Cantidad de asientos = {self.cantidadAsientos}")
        print(f"Velocidad maxima = {self.velocidadMaxima}")
        print(f"Color = {self.color.name}")

class POO202502_A02_E23:
    @staticmethod
    def main():
        auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO, 5, 6, 250, TipoColor.NEGRO, True)
        auto1.imprimir()
        auto1.setVelocidadActual(240)
        print("Velocidad actual =", auto1.velocidadActual)
        auto1.acelerar(20)
        print("Valor total en multas =", auto1.valorTotalMultas())
        print("Velocidad actual =", auto1.velocidadActual)
        auto1.desacelerar(50)
        print("Velocidad actual =", auto1.velocidadActual)
        auto1.frenar()
        print("Velocidad actual =", auto1.velocidadActual)
        auto1.desacelerar(20)

# Ejemplo de uso
if __name__ == "__main__":
    POO202502_A02_E23.main()