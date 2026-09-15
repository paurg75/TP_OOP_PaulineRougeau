#question1
"""Exercice 4"""
robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}
def robots_double_mission(rob_exp,rob_trans):
    """renvoie les robots qui font les 2 missions"""
    return rob_exp&rob_trans

def robots_toutes_missions(rob_exp,rob_trans):
    """renvoie tous les robots qui font au moins une mission"""
    return rob_exp|rob_trans

def robots_exploration_seulement(rob_exp,rob_trans):
    """renvoie les robots qui ne font que la mission d'exploration"""
    return rob_exp-rob_trans


double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

#question 2
def ajouter_robot_mission(ensrob,nom):
    """ajoute un robot à une mission"""
    newens=ensrob.copy()
    newens.add(nom)
    return newens

def retirer_robot_mission(ensrob,nom):
    """retire un robot à une mission"""
    newens=ensrob.copy()
    newens.remove(nom)
    return newens

ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
print(robots_transport)
assert robots_transport == {"R5", "R9", "R7", "R3"}
