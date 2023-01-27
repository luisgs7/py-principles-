from abc import ABC, abstractmethod


class IMotorbike(ABC):

    @abstractmethod
    def start(self) -> None:
        raise NotImplemented
    
    @abstractmethod
    def stop(self) -> None:
        raise NotImplemented


class Honda(IMotorbike):
    def __init__(self, nome) -> None:
        self.nome = nome

    def start(self) -> None:
        print(f"Ligou a moto {self.nome}")
    
    def stop(self) -> None:
         print(f"Desligou a moto {self.nome}")
    

if __name__ == "__main__":
    h = Honda("01")
    h.start()
    h.stop()