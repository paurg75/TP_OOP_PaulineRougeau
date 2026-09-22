import unittest
from habitant2 import*

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""
    def test_age_setter_valide(self):
        self.h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        self.h1.age=26
        resultat= self.h1.age
        attendu=26
        self.assertEqual(resultat, attendu)

    def test_age_setter_invalide(self):
        self.h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        with self.assertRaises(ValueError):
            self.h1.age = -5

    def test_compte_animal_possede(self):
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        resultat=h1.compte_animal("vaches")
        attendu=3
        self.assertEqual(resultat, attendu)



if __name__ == "__main__":
    unittest.main(verbosity=2)