def F_bry(material: str):
    F_bry = {"steel-4130": 827,  # MPa
             "steel-4340": 2151,  # MPa
             "S 96": 973,  # MPa
             "S 99": 1667,  # MPa
             "S 510": 448,  # MPa
             "S 514": 945,  # MPa
             "T 45": 849,  # MPa
             "Al-2014": 490,
             "Al-2024": 248,
             "Al-6061": 152,
             "Al-7075": 469,
             "other": 500
             }  # from http://www.lightaircraftassociation.co.uk/engineering/TechnicalLeaflets/Building,%20Buying%20or%20Importing/TL%201.16%20Material%20Allowable%20Strength%20Data.pdf
    return F_bry[material]


def E_mod(material: str):
    E_mod = {"steel-4130": 205,  # Gpa
             "steel-4340": 200,
             "S 96": 200,
             "S 99": 200,
             "S 510": 200,
             "S 514": 200,
             "T 45": 200,
             "Al-2014": 73,
             "Al-2024": 73.1,
             "Al-6061": 68,
             "Ti-6AL": 104,
             "Composite": 110,
             "Al-7075": 71.7
             }
    return E_mod[material]


def Expansion_cof(material: str):
    Expansion_cof = {"steel-4130": 12,  # m/k  10^-6
                     "steel-4340": 12.3,
                     "S 96": 12,
                     "S 99": 12,
                     "S 510": 12,
                     "S 514": 12,
                     "T 45": 12,
                     "Al-2014": 23,
                     "Al-2024": 22.8,
                     "Al-6061": 23.4,
                     "Al-7075": 23.2
                     }
    return Expansion_cof[material]


def Yield_stress(material: str):
    Yield_stress = {"steel-4130": 483,
                    "steel-4340": 1496,
                    "S 96": 680,
                    "S 99": 1080,
                    "S 510": 255,
                    "S 514": 630,
                    "T 45": 620,
                    "Al-2014": 324,
                    "Al-2024": 200,
                    "Al-6061": 83,
                    "Ti-6AL": 880,
                    "Composite": 825,
                    "Al-7075": 303
                    }  # MPa
    return Yield_stress[material]


def density(material: str):
    density = {"steel-4130": 7830,
               "steel-4340": 7830,
               "S 96": 7860,
               "S 99": 7860,
               "S 510": 7920,
               "S 514": 7890,
               "T 45": 7890,
               "Al-2014": 2800,
               "Al-2024": 2770,
               "Al-6061": 2710,
               "Ti-6AL": 4429,
               "Composite": 1550,
               "Al-7075": 2800
               }  # kg/m^3

    return density[material]


def Poisson_ratio(material: str):
    ratio = {"steel-4130": 0.3,
             "steel-4340": 0.3,
             "S 96": 0.3,
             "S 99": 0.3,
             "S 510": 0.3,
             "S 514": 0.3,
             "T 45": 0.34,
             "Al-2014": 0.33,
             "Al-2024": 0.33,
             "Al-6061": 0.33,
             "Al-7075": 0.33
             }  # kg/m^3

    return ratio[material]
