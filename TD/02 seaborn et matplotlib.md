# 02 seaborn et matplotlib

## Livrables attendus
Réalisez et livrez un Notebook que vous partagerez à simon.ouellet@univ-poitiers.fr (Simon OUELLET).

Votre Notebook devra être nommé : 01pandas_\<Prenom\>-\<Nom\>.ypynb  

Utilisez les cellules textes en format Markdown directement dans le notebook pour :    
Décrire avant chaque cellule de code :  
- l'action/résultat attendus ;  
- vos analyses/stratégie ;  
- vos limitations ;  
- vos résultats.

## Les données

Les données sont disponibles dans le dépôt de code Github de SimonOuellet saradsm2 branche Master et répertoire data : https://github.com/SimonOuellet/saradsm2/tree/master/data 

## Objectifs

### Exercice 1 palette de couleurs - évolution des vols  

Utiliser le jeu de données **flight_details.csv** pour produire un graphique de type heatmap.  
Créer votre propre palette de couleur et faites en sorte que les valeurs minimales soient d'une couleur vive et que les valeurs maximales soient sombre.  
  
Le résultat devrait ressembler à cela : 

![heatmap](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781800568846/files/image/B15779_04_27.jpg)


### Exercice 2 graphique à barres - comparaisons de films

Dans cet exercice, il faudra comparer les scores provenant de deux sources différentes pour 5 films. La source tomatometer indique de critique ayant été positives et la source "Audience Score" correspond au pourcentage d'utilisateur ayant donnés une note de plus de 3.5 ou plus sur 5.  

Pour ce faire, vous devrez utiliser la source de données **movie_scores.csv**. Transformer les données pour qu'ils soient utilisable par la fonction seaborn **barplot**.  
 
Le résultat devrait ressembler à cela :   

![Comparaison](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781800568846/files/image/B15779_04_29.jpg)


### Exercice 3 Comparaison des résultats de QI de différent groupe en utilisant des graphiques en violon.  

En utilisant le jeu de données **iq_scores.csv** il faut récupérer les données de chaque groupe, les convertir en liste, les assigner aux bonnes variables.  
Il faudra créer un DataFrame contenant toutes ces données.  Créer un graphique pour les résultats de QI en utilisant la fonction **violonplot()**. Utiliser le style **whitegrid**, le contexte **talk**, supprimer toutes les bordures sauf celle du bas et ajouter un titre.  
  
Le résultat devrait ressembler à cela :   

![violon](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781800568846/files/image/B15779_04_36.jpg)

### Exercice 4 Visualiser le top 30 des Music Youtube Channels.  

Il faudra générer un graphique de type FacetGrid pour comparer le nombre total d'inscrit et le nombre total de vues pour un top 30 YouTube Channels (janvier 2020) dans la catégorie music.  

Il faudra utiliser Pandas pour charger les données du fichier YouTube.csv et créer ensuite un FacetGrid avec deux colonnes pour afficher les résultats.  

Le résultat devrait ressembler à cela :   

![youtube](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781800568846/files/image/B15779_04_38.jpg)

### Exercice 5 Analyse d'existence de relation entre le poids et la longévité chez les animaux en utilisant une régression linéaire.

Vous disposez d'un ensemble de données concernant divers animaux, comprenant leur masse corporelle et leur longévité maximale.  

Vous devrez générer un diagramme de régression pour découvrir s'il existe une relation linéaire entre ces deux variables.  

Vous devrez charger les données depuis **anage_data.csv** dans un dataframe. 
Vous devrez filtrer les données pour ne gardez que les variables de poids et de longévité maximale.  
Ne gardez que les données concernant la classe **Mammalia** et les animaux d'un poids de moins de 200 000g.   
Créer une graphique de régression linéaire pour observer la relation entre ces deux variables.  

Le résultat devrait ressembler à cela:  

![animals](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781800568846/files/image/B15779_04_40.jpg)
