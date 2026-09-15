releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def recalibrer(releves,nom,val):
    newreleve=[]
    for releve in releves:
        if releve[0]==nom:
            newreleve.append((releve[0],val,releve[2]));
        else:
            newreleve.append(releve);
    return newreleve



nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3