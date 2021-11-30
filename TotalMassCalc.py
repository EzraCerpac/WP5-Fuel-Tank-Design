from math import pi
from MaterialProperties import density


def main(material: str, R, L, t1, t2, attachments_mass):
    # end caps
    volume_caps = 4 * pi * R**2 * t2

    # mid section
    length = L - 2 * R
    volume_mid = 2 * pi * R * length * t1

    # total tank
    volume_total = volume_caps + volume_mid
    mass_tank = volume_total * density(material)

    total_mass = mass_tank + attachments_mass
    return total_mass