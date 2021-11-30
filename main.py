import LaunchLoads3a, LaunchLoads3b

class FuelTank:
    def __init__(self):
        # Random Values
        self.material = "Al-2014"
        self.R = 2
        self.L = 5
        self.t1 = 3e-3
        self.t2 = 4e-3


    def p3a(self):
        self.column_buckling_stress, fail = LaunchLoads3a.main(self.material, self.R, self.L, self.t1)
        if fail:
            print("fail!")


def main():
    pass


if __name__ == '__main__':
    main()

