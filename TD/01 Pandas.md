# Travaux dirigés Pandas
Préparés par Simon OUELLET 2022  


## Contexte
Dans le cadre du projet statistique, dans la mesure du possible et dès que c'est pertinent de le faire, les données de Calixys doivent être utilisées.  

## Objectifs
1. Charger des données dans un DataFrame Pandas, les données en provenance d'un fichier CSV et :  
	2. Afficher le type de chaque colonnes ;  
	3. Afficher un échantillon du DataFrame ;  
	4. Afficher le nombre de colonnes et de lignes que contient le DataFrame ;  
	5. Afficher la quantité de mémoire qu'utilise votre DataFrame ;  
	6. Afficher les données statistiques d'une colonne de votre choix ;  
	7. Afficher le nombre de valeur nulles pour une colonne ;   
	8. Supprimer une colonne ;  
9. Charger un fichier JSON et l'aplatir. (voir https://github.com/SimonOuellet/saradsm2/tree/master/Python/demojson)  
	10. Charger le fichier parkings-publics-nantes-disponibilites_12102022-15_58_07.json et aplatir les données pour obtenir les champs suivant dans votre dataframe : grp_horadatage, grp_disponible, grp_nom, grp_statut, grp_complet, grp_location : longitude et latitude.  
	11. Afficher les parkings et les champs :   
	nom    
	nombre de place disponible(grp_complet),   
			avec un tri inversé (z-a) sur le nom.  
	12. Afficher le taux de remplissage de chaque parking. Nom et taux de remplissage (grp_complet / grp_disponible)  
13. Associer plusieurs DataFrames  
	14. créer un datadrame à l'aide des trois fichiers suivant :  carei_sen_seniors_v3_211203.csv, care_i_revenus_quetelet.csv et suivimortalite2021_carei.csv.  
		15. Utiliser deux méthodes différentes pour associer deux dataframes : merge et join, et identifier la méthode la plus rapide.  
16. Transformer et encoder en valeur numérique les colonnes catégorielles ayant des valeurs non numérique. (Encodage de valeur) (Ex. : colonne axelarge1 )  
17. Remplacer les valeurs nulles par des 0.  
18. Normaliser les valeurs de votre dataframe.   
19. Créer un nouveau dataframe avec que des variables catégorielles.  
	20. Modifier le types des colonnes de ce dataframe en "category".  

## Livrables attendus
Réalisez et livrez un Notebook que vous partagerez à so@gleeph.net (Simon OUELLET).

Votre Notebook devra être nommé : 01pandas_\<Prenom\>-\<Nom\>.ypynb  

Utilisez les cellules textes en format Markdown directement dans le notebook pour :    
Décrire avant chaque cellule de code :  
- l'action/résultat attendus ;  
- vos analyses/stratégie ;  
- vos limitations ;  
- vos résultats.  

==Les données devront être livrées avec le notebook ou du moins spécifier dans le notebook l'endroit où ils peuvent être récupérer et la procédure pour le faire en fonction de la complexité.==

## Communications
@ Simon Ouellet -> Lorsque vous avez terminé, partagez lui votre Notebook. Merci! :)

## Données à utiliser 

Données Calixys  
carei_sen_seniors_v3_211203.csv  
care_i_revenus_quetelet.csv   
suivimortalite2021_carei.csv    

https://github.com/SimonOuellet/saradsm2/blob/ebb9dab5efe1068390ab877982e92e78240f80aa/Python/demojson/parkings-publics-nantes-disponibilites_12102022-15_58_07.json

## Cheat Sheet

https://github.com/SimonOuellet/saradsm2/tree/master/Python/demojson

Magic pour calculer le temps d'exécution d'une cellule:  
%time  

Pandas : afficher le type de vos colonnes :   
```
df.dtypes
```

Pandas : afficher les 5 premières lignes et 5 dernières:  
```
df.head(5)  
df.tail(5)  
```

Import de json  
```
import json
with open('parkings-publics-nantes-disponibilites_1210202215.json') as json_file:
    json_data = json.load(json_file)
j = pd.DataFrame(json_data['records'])
```
