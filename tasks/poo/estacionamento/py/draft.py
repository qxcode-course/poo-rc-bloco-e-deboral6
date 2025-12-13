from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, entrada: int, tipo: str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo

    def setEntrada(self, horaEntrada: int):

    def getEntrada() -> int:

    @abstractmethod
    def calcularValor():
        pass