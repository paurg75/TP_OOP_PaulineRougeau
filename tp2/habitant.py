#Question 1
class Habitant():
    def __init__(self, nom, age, adresse, animaux=None):
        self.nom=nom
        self.age=age
        self.adresse=adresse
        self.animaux=animaux

    def affichage_adresse(self):
        print(self.nom+" habite à "+self.adresse)

    def compte_animal(self, animal):
        for anim in self.animaux:
            if anim==animal:
                return self.animaux[anim]
            else:
                return 0


h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"