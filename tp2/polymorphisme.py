from abc import ABC, abstractmethod
class Habitant(ABC):
    def __init__(self, nom, prenom, age,adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse=adresse
    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        pass
    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.age} ans, habite à {self.adresse}"
    

class Adulte(Habitant):
    def __init__(self, nom, prenom, age, adresse):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")
        super().__init__(nom, prenom, age,adresse)
    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Déjà à la retraite"
        else:
            return age_retraite - self.age

class Enfant(Habitant):
    def __init__(self, nom, prenom, age, adresse):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
        super().__init__(nom, prenom, age,adresse)
    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: Un enfant ne peut pas calculer sa retraite"


def affichage(h: Habitant):
    print(str(h))
    

adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant=Enfant("Martin", "Lucas", 12, "Rue B")
print(adulte)
affichage(adulte)
affichage(enfant)