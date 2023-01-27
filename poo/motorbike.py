class Motorbike:
    def __init__(self, model: str, year: int, power: int) -> None:
        self.model = model
        self.__year = year
        self.power = power

    def start(self) -> None:
        if self._verifyGasoline:
            print("Starting the Motorbike!")
        print("No gasoline")

    def stop(self) -> None:
        print("Stopping the Motorbike")

    def _verifyGasoline(self) -> bool:
        return False
    
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, valor: int) -> None:
        self.__year = valor


if __name__ == "__main__":
    p = Motorbike("MT07", 2023, 700)
    p.start()
    print(p.model, p.power)
