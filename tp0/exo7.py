import unittest
from exo3quest2 import *
from exo4 import *

class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""
    def test_recalibrer_capteur_existant(self):
        releve1 = ("laser_avant", 2.35, "m")
        releve2 = ("laser_arriere", 1.10, "m")
        releve3 = ("gyroscope", 87.5, "deg")
        releves = [releve1, releve2, releve3]
        resultat= recalibrer(releves, "laser_avant", 2.40)
        attendu=[("laser_avant", 2.40, "m"),releve2,releve3]
        self.assertEqual(resultat, attendu)

    def test_recalibrer_capteur_absent(self):
        """Cas limite : le capteur demande n’existe pas."""
        releve1 = ("laser_avant", 2.35, "m")
        releve2 = ("laser_arriere", 1.10, "m")
        releve3 = ("gyroscope", 87.5, "deg")
        releves = [releve1, releve2, releve3]
        resultat= recalibrer(releves, "capteur", 2.40)
        attendu=releves
        self.assertEqual(resultat, attendu)

class TestFlotteRobots(unittest.TestCase): 
    def test_robots_double_mission(self):
        robots_exploration = {"R2", "R5", "R7"}
        robots_transport = {"R5", "R9", "R7", "R3"}
        resultat1= robots_double_mission(robots_exploration, robots_transport)
        attendu1= {"R5", "R7"}
        self.assertEqual(resultat1, attendu1)
        resultat2 = robots_toutes_missions(robots_exploration, robots_transport)
        attendu2 ={"R2", "R3", "R5", "R7", "R9"}
        self.assertEqual(resultat2, attendu2)
        resultat3 = robots_exploration_seulement(robots_exploration, robots_transport)
        attendu3 ={"R2"}
        self.assertEqual(resultat3, attendu3)

if __name__ == "__main__":
    unittest.main(verbosity=2)