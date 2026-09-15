"""Exercice 6"""
#problèmes de qualité pylint :
#- pas de docstring sur la fonction
#- pas de nom explicite pour les variables d t
# - paramètre inutilisé (d)
def cout_deplacement_propre(terrain,x1, y1, x2, y2):
    """calcule le coût énergétique d'un déplacement selon le terrain"""
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if terrain == 'R':
        c = dist * 1.0
    elif terrain == 'andH':
        c = dist * 1.5
    elif terrain == 'S':
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
    return c
