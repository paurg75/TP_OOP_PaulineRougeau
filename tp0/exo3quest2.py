"""question2 de l'exo 3"""
releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]
def recalibrer(docreleve,nom,val):
    """permet de changer la valeur d'un des composants"""
    newreleve=[]
    for releve in docreleve:
        if releve[0]==nom:
            newreleve.append((releve[0],val,releve[2]))
        else:
            newreleve.append(releve)
    return newreleve
nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
