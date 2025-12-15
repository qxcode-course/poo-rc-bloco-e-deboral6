from abc import ABC, abstractmethod
 
class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = 0

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
        tempo = horaSaida - self.horaEntrada
        return tempo / 20


class Carro(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida):
        tempo = horaSaida - self.horaEntrada
        valor = tempo / 10
        return valor if valor >= 5 else 5.0


class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.horaAtual = 0

    def procurarVeiculo(self, id: str):
        for i, v in enumerate(self.veiculos):
            if v.getId() == id:
                return i
        return -1

    def estacionar(self, veiculo: Veiculo):
        veiculo.setEntrada(self.horaAtual)
        self.veiculos.append(veiculo)

    def pagar(self, id: str):
        pos = self.procurarVeiculo(id)
        if pos != -1:
            veiculo = self.veiculos[pos]
            valor = veiculo.calcularValor(self.horaAtual)
            print(
                f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} "
                f"saiu {self.horaAtual}. Pagar R$ {valor:.2f}"
            )
        else:
            print("Veículo não encontrado")

    def passarTempo(self, tempo: int):
        self.horaAtual += tempo

    def __str__(self):
        texto = ""
        for v in self.veiculos:
            texto += str(v) + "\n"
        return texto

def main():
    est = Estacionamento()

    while True:
        try:
            linha = input()
            print(f"${linha}")

        except EOFError:
            break

        if not linha:
            continue

        partes = linha.split()
        comando = partes[0]

        if comando == "end":
            break

        elif comando == "tempo":
            est.passarTempo(int(partes[1]))

        elif comando == "estacionar":
            tipo = partes[1]
            vid = partes[2]

            if tipo == "bike":
                v = Bike(vid)
            elif tipo == "moto":
                v = Moto(vid)
            elif tipo == "carro":
                v = Carro(vid)
            else:
                continue

            est.estacionar(v)

        elif comando == "show":
            if est.veiculos:
                print(est, end="")
            print(f"Hora atual: {est.horaAtual}")

        elif comando == "pagar":
            est.pagar(partes[1])
main()