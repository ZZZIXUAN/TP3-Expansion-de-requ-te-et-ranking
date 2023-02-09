# TP3 Expansion de requête et ranking
# Description du projet
Nous voulons construire un système basé sur l'index fourni par le fichier `index.json`, la liste d'url et le titre originaux fournis par `documents.json`. 

Les requêtes personnalisées entrées par l'utilisateur sont tokenisées et transformées, le token est obtenu et la liste de toutes les urls contenant le token est filtrée dans le fichier `index.json` correspondant et les résultats classés sont donnés.

Par exemple, si l'utilisateur saisit `wikipédia et google`, tous les liens url et titres pertinents sont stockés dans le fichier `result.json`. Les métadonnées sont stockées dans le fichier `metadata.json`, où
* Total Index : le nombre de token convertis à partir des demandes des utilisateurs.
* Filtered Index : le nombre de correspondances entre le token de requête de l'utilisateur et `l'index.json`. Dans ce cas, 'wikipédia', 'and' et 'google' apparaissent tous dans `index.json`, donc Total Index=Filtered Index=3.
* Total Records : le nombre d'entrées retournées dans le fichier `result.json`.

## Etapes de la mise en place
* Connectez ce github `git clone https://github.com/ZZZIXUAN/TP3-Expansion-de-requ-te-et-ranking.git`
* Changez de répertoire `cd TP3-Expansion-de-requ-te-et-ranking`
* Exécutez le programme en utilisant `python3 main.py` (Exécutez avec les valeurs par défaut)
* Exécutez les tests en utilisant `python3 -m unittest discover`

### Contributeur

Zixuan WANG