#question 1

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releve):
    val=str(releve[1]);
    return "Capteur "+releve[0]+" : "+val+" "+releve[2]

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

#question 2
def recalibrer(releve,nom,val):
    for i in range(0,2):
        newreleve[i][0]=releve[i][0]
        newreleve[i][2]=releve[i][2]
        if releve[i][1]==nom:
            newreleve[i]



nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3