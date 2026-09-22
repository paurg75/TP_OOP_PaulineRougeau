from habitant2 import*

class Village():
    def __init__(self, nom):
        self.nom=nom
        self.habitant=[]

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        habitant=Habitant(nom,age,adresse,animaux)
        self.habitant.append(habitant)

    def ajouter_habitant_agregation(self, habitant):
        self.habitant.append(habitant)

    def get_habitants(self):
        return self.habitant

    def afficher_habitants(self):
        for hab in self.habitant:
            print(" "+hab.get_nom())

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()
pytown.afficher_habitants()


#ajouter_habitant_composition est une composition car si le village est détruit, l'habitant disparaît avec lui.
#ajouter_habitant_agregation est une agrégation car elle utilise un objet habitant déjà existant donc l'habitant survit indépendamment du village dans le reste du programme.  