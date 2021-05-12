# 1. Lecture d'un fichier CSV

Modifier la fonction proposée pour qu'elle renvoie la liste des Pokemon du `fichier` passer en argument.

# 2. Fusion de colonnes

Certains Pokemons sont de deux types :

```
{'Nom': 'Aspicot', 'Type 1': 'Insecte', 'Type 2': 'Poison', 'HP': '40', 'Attaque': '35', 'Défense': '30', 'Vitesse': '50'}
```

Écrire une fonction `fusion_col` qui transforme ce Pokemon en 

```
{'Nom': 'Aspicot', 'Type': ['Insecte', 'Poison'], 'HP': '40', 'Attaque': '35', 'Défense': '30', 'Vitesse': '50'}
```

# 3. Fusion de lignes

Écrire une fonction `fusion_lignes` qui fusionne les deux fichiers et ne renvoie qu'un seule liste de Pokemon.

# 4. Écrire un fichier CSV

En utilisant https://docs.python.org/3.7/library/csv.html#csv.DictWriter, écrire la dernière liste dans un fichier.