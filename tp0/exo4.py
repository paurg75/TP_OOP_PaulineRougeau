#question1

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}
def robots_double_mission(rob_exp,rob_trans):
    return rob_exp&rob_trans

def robots_toutes_missions(rob_exp,rob_trans):
    return rob_exp|rob_trans    

def robots_exploration_seulement(rob_exp,rob_trans):
    return rob_exp-rob_trans 


double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

#question 2
def ajouter_robot_mission(listrob,nom):
    newlist=[]
    newlist.append(listrob)
    newlist.append(nom)
    for i in newlist:
        print(i)
    return newlist

def retirer_robot_mission(listrob,nom):
    newlist=[]
    for list in listrob:
        if list!=nom:
            newlist.append(list)        
    return newlist
    
ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}
