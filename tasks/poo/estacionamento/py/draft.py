from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, horaEntrada: int, tipo: str):
        self.id = id
        self.horaEntrada = 0
        self.tipo = tipo

    def setEntrada(self, horaEntrada: int):
        self.horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self.horaEntrada

    def getTipo(self) -> str:
        return self.tipo

    def getId(self) -> str:
        return self.id

    @abstractmethod
    def calcularValor(self, horaSaida: int):
        pass

    def __str__(self):
        return f"{self.tipo:_>10} : {self.id:_>10} : {self.horaEntrada}"
class Bike(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Bike")

    def calcularValor(self, horaSaida):
        return 3.0
    
class Moto(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida):
        temp = horaSaida - self.horaEntrada
        return temp / 20

class Carro(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida):
        temp = horaSaida - self.horaEntrada
        valor = temp / 10
        return valor if valor >= 5 else 5.0 

class Estacionameto:
    def __init__(self, veiculos: Veiculo, horaAtual: int):
        self.veiculos = []
        self.horaAtual = 0

        def procurarVeiculo(self, id: str):
            for i, v in enumerate(self.veiculos):
                if v.getId() == self.id:
                    return 1
            return -1

        def estacionar(self, veiculo: Veiculo):
            veiculo.setEntrada(self, horaAtual)
            self.veiculos.apped(veiculo)
            print("Veiculo estacionado, veiculo")

        def pagar(self, id: str):
            pos = self.procurarVeiculo(id)
            if pos != -1:
                veiculo = self.veiculos.pop(pos)
                valor = calcularValor(self.horaAtual)
                print(f"valor a pagar ({veiculo.getTipo()}): R$ {valor:.2f}")
            else:
                print("Veículo não encontrado")
           
        def sair(self, id: str):
            pos = self.procurarVeiculo(id)
            if pos != -1:
                veiculo = self.veiculos.pop[pos]
                valor = calcularValor(self.horaAtual)
                print(f"Veículo {veiculo.getId()} saiu")
                print(f"Total pago: R$ {valor:.2f}")
            else:
                print("Veículo não encontrado")

        def passarTempo(self, tempo: int):
            horaAtual += tempo

        def __str__(self):
            texto = "Veículos no estacionamento:\n"
            for v in self.veiculos:
                texto += str(v) + "\n"
            return texto