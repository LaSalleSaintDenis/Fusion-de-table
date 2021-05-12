import csv

def csv2list(fichier):
    list1 = []
    with open('pokedex1.csv','r') as fp:
        lecteur = csv.DictReader(fp, delimiter=';')
        for ligne in lecteur:
            list1.append(dict(ligne))
        return None


def fusion_col(pokemon):
    return pokemon


def fusion_lignes(fichier1,fichier2):
    return list