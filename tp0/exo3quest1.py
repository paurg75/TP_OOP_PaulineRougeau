"""question1 de l'exo 3"""
releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releve):
    """affiche les caracteristiques des composants"""
    val=str(releve[1])
    return "Capteur "+releve[0]+" : "+val+" "+releve[2]

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"
