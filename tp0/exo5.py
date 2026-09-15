"""Exercice 5"""
#question1

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(stock,modele,piece):
    """rerourne la quantité disponible de la pièce"""
    return stock[modele][piece]
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

#question2
def consommer_piece(stock,modele,piece,conso):
    """enlève la quantité consommée à la pièce"""
    stock[modele][piece]-=conso

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

def ajouter_modele(stock,modele,moteurs,capteurs,roues):
    """ajoute un modele au dictionnaire"""
    stock[modele]={"moteurs":moteurs,"capteurs":capteurs,"roues":roues}

ajouter_modele(pieces_stock, "ModeleC",moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}

def total_pieces(stock):
    """retourne un dictionnaire avec les quantités totales de chaque pièce"""
    tot_mot=0
    tot_capt=0
    tot_roues=0
    for mod in stock:
        for piece in stock[mod]:
            if piece=="moteurs":
                tot_mot+=stock[mod][piece]
            if piece=="capteurs":
                tot_capt+=stock[mod][piece]
            if piece=="roues":
                tot_roues+=stock[mod][piece]
    stock_tot={"moteurs":tot_mot,"capteurs":tot_capt,"roues":tot_roues}
    return stock_tot

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}
