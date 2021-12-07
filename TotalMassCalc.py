from math import pi
from MaterialProperties import density


def tankMass(material: str, R, L, t1, t2):
    # end caps
    volume_caps = 4 * pi * R ** 2 * t2

    # mid section
    length = L - 2 * R
    volume_mid = 2 * pi * R * length * t1

    # total tank
    volume_total = volume_caps + volume_mid
    mass_tank = volume_total * density(material)
    return mass_tank


def TankFuelMass(mass_tank, mass_fuel):
    return mass_tank + mass_fuel


def totalMass(material: str, R, L, t1, t2, attachments_mass, mass_fuel, mass_sc):
    mass_tank = tankMass(material, R, L, t1, t2)
    mass_fueled_tank = TankFuelMass(mass_tank, mass_fuel)
    total_mass = mass_fueled_tank + attachments_mass + mass_sc
    return total_mass
