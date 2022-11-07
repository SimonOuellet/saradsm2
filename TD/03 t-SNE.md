# 03 t-SNE

## Livrables attendus

Réalisez et livrez un Notebook que vous partagerez à so@gleeph.net (Simon OUELLET).

Votre Notebook devra être nommé : 02tsne_\<Prenom\>-\<Nom\>.ypynb  

Utilisez les cellules textes en format Markdown directement dans le notebook pour :    
Décrire avant chaque cellule de code :  
- l'action/résultat attendus ;  
- vos analyses/stratégie ;  
- vos limitations ;  
- vos résultats.

## Les données

Les données sont disponibles dans le dépôt de code Github de SimonOuellet saradsm2 branche Master et répertoire data : [salary.csv](https://github.com/SimonOuellet/saradsm2/blob/master/data/salary.csv)

## Objectifs

### Exercice 1 Chercher par essais et erreurs

Inspirez-vous du notebook [TSNE](https://github.com/SimonOuellet/saradsm2/blob/master/Notebooks/TSNE.ipynb) pour réaliser une première analyse de la base de données exemple [salary.csv](https://github.com/SimonOuellet/saradsm2/blob/master/data/salary.csv). 

1.1 Essayer de trouver les bons paramètres pour obtenir une forme globulaire comprenant plusieurs sous ensembles eux même de formes plus ou moins globulaires.  
Il faut itérer en modifiant au "feeling" les paramètres en fonction des résultats précédemment obtenus.

Exemple:
voir ![image TSNE](https://github.com/SimonOuellet/saradsm2/raw/master/TD/reponses/tsne-salary-gender.png)


1.2 Une fois que vous aurez une distribution satisfaisante, modifiez le code de la visualisation pour obtenir une coloration des points en fonction d'une variable (ex.: genre).   

1.3 Faites le pour chaque variables et sauvegardez le résultat dans une image.  

1.4 Analysez et qualifiez l'impacte de chaque variables par rapport au résultat obtenu.  

### Exercice 2 Réaliser un t-SNE sur votre propre jeu de données. (ex projet stat)

