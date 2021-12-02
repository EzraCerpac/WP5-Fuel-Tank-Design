from math import pi
import MaterialProperties as mp
import os


#values based on material for the backupplate (bp), SC (sc) and the fastener (b)


#decisions need to be made based on numbers not yet gotten,
#so this is just a basic set up

#values based on material choice for the attached parts (a) and the fastener (b)

def main(Dfo, Dfi, t2, t3, Lh, Lc, material_lug, material_wall, material_fastener):
    # print(f"running {os.path.basename(__file__)}")
    Ebp = mp.E_mod(material_lug)
    Esc = mp.E_mod(material_wall)
    Eb = mp.E_mod(material_fastener)

    #summing for db
    sh = Lh / ((Dfo **2 * pi)/4)
    sb = (t2 + t3) / ((Dfi **2 * pi)/4)
    sc = Lc / ((Dfo **2 * pi)/4)\

    #calculating compliances
    dbp = (4 * t2) / (Ebp * pi * (Dfo **2 - Dfi **2))
    dsc = (4 * t3) / (Esc * pi * (Dfo **2 - Dfi **2))
    db = (sh + sb + sc)/Eb

    #finding the force ratio
    phibp = dbp / (dbp + db)
    phisc = dsc / (dsc + db)

    return phibp, phisc
