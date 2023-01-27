from motorbike_int import IMotorbike


class NewMoto(IMotorbike):
    def __init__(self, nome) -> None:
        self.__nome = nome

    def start(self) -> None:
        print("Traveling at 200 km/h")
    
    def stop(self) -> None:
        print("No break!!!")
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        self.__nome = valor


class OldMoto(IMotorbike):
    def __init__(self, nome) -> None:
        self.__nome = nome

    def start(self) -> None:
        print("Traveling at 150 km/h")
    
    def stop(self) -> None:
        print("Stopping")
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        self.__nome = valor


if __name__ == "__main__":
    nwm = NewMoto("Moto 2024")

    print(nwm.nome)
    nwm.nome
    nwm.start()
    nwm.stop()

    print()

    old = OldMoto("Moto 1975")

    print(old.nome)
    old.start()
    old.stop()
