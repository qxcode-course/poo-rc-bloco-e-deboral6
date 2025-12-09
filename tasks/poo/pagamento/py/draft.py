from abc import ABC, abstractmethod

class Metodo(ABC):
    @abstractmethod
    def realizar_pagamento(self, descricao, 1valor: float):
        pass

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError(f"O valor deve ser maior que zero")
    
    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descricao}")

    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero, nome_titular, limite_disponivel):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        if self.valor > self.limite_disponivel:
            raise Exception(f"Erro: Limite isuficiente no cartão {self.numero}")
        else:
            self.limite_disponivel -= self.valor
            print(f"Pagamento no cartao, no valor de {self.valor}")

class Pix(Pagamento):
    def __init__(self, valor, descriçao, chave, banco):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"Pagando pix produto {self.descricao} para {self.chave} do banco {self.banco} no valor de {self.valor}")

class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras: int, vencimento):
        super().__init__(valor, descriçao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):

        




