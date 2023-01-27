from motorbike import Motorbike

class Yamaha(Motorbike):
    def new_engine(self):
        print("New engine with more power and torque.")

if __name__ == "__main__":
    mt_09 = Yamaha("MT09",2023, 823)
    mt_09.new_engine()