class FuelTank:
    def __init__(self):
        pass


class Spacecraft:
    def __init__(self, FuelTank):
        self.FuelTank = FuelTank
        self.h = 4.25  # Height of SC
        self.d = 2.3  # Inner Diameter of SC


def main():
    tank = FuelTank()
    SAPPHIRE = Spacecraft(tank)
    pass


if __name__ == '__main__':
    main()
