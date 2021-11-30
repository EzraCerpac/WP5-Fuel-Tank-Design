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


def main(material: str, R, L, t1, t2, attachments_mass):
    mass_tank = tankMass(material, R, L, t1, t2)
    total_mass = mass_tank + attachments_mass
    return total_mass
