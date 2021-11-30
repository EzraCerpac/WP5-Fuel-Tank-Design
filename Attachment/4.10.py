from math import pi


#values based on material for the backupplate (bp), SC (sc) and the fastener (b)
Ebp = 205 * 10**9
Esc = 68 * 10**9
Eb = 71.1 * 10**9

def main(Dfo, Dfi, t2, t3):

    Dfo = Dfo / 1000
    Dfi = Dfi / 1000
    t2 = t2 / 1000
    t3 = t3 /1000

    #summing for db
    sh = (0.5 * Dfi) / ((Dfo **2 * pi)/4)
    sb = (t2 + t3) / ((Dfi **2 * pi)/4)
    sc = (0.4 * Dfi) / ((Dfo **2 * pi)/4)\

    #calculating compliances
    dbp = (4 * t2) / (Ebp * pi * (Dfo **2 - Dfi **2))
    dsc = (4 * t3) / (Esc * pi * (Dfo **2 - Dfi **2))
    db = (sh + sb + sc)/Eb

    #finding the force ratio
    phibp = dbp / (dbp + db)
    phisc = dsc / (dsc + db)

    return phibp, phisc


    


