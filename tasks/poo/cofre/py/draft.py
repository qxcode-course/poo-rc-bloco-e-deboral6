from abc import ABC, abstractmethod

class Valuable(ABC):

    @abstractmethod
    def getLabel(self):
        pass

    @abstractmethod
    def getValue(self): 
        pass
    
    @abstractmethod
    def getVolume(self):
        pass

    def __str__(self):
        pass

class Item(Valuable):
    def __init__(self, label: str, value: float, volume: int):
        self.label = label
        self.value = value
        self.volume = volume

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getVolume(self):
        return self.volume

    def setLabel(self):
        self.setLabel = label

    def setVolume(self):
        self.volume = volume

    def __str__(self):
        return f"{self.label}, {self.value}, {self.volume}"

class Coin(Item):
    def __init__(self, label, value, volume):
        super().__init__(label, value, volume)

class Pig:
    def __init__(self, volume_max: int):
        self.volume_max = volume_max
        self.Valuables = []
        self.broken = False

    def addValuable(self, valuable):
        if self.broken:
            return False

        if self.getVolume() + valuable.getVolume() > self.volume_max:
            return False
        
        self.Valuables.apped(valuable)
        return True
    
    def break_pig(self):
        self.broken = True
        return True

    def getVolume(self):
        total = 0 
        for v in self.valuables:
            total += v.getValue()
        return total

    def calc_value(self):
        total = 0
        for v in self.valuables:
            total += v.getValue()
        return total

    def is_broken(self):
        return self.broken
    
    def getCoins(self):
        return [v for v in self.valuables if isinstance(v, Coin)]

    def get_items(self):
        return [v for v in self.valuables if isinstance(v, Item)]

    def __str__(self):
        return f"{self.getVolume()}/ {self.volume_max}, {self.calc_value()}, {self.broken}"




