import pandas as pd

#Charge du fichier JSON dans un DataFrame pandas
richpwr = pd.read_json('rich-pwr-simon.json', lines=True)

#Transforme la colonne _source contenant les données structurées en JSON et on écrase le dataframe d'origine
richpwr = richpwr._source.apply(pd.Series)

#Affiche les informations sur le dataframe principal
richpwr.infos()
richpwr.shape

#Applatie les colonnes clilFirst contenant des données structurées en JSON en créant un nouveau dataframe
richpwrClilFirst = richpwr.clilFirst.apply(pd.Series)
richpwrClilSecond = richpwr.clilSecond.apply(pd.Series)
richpwrClilFirst.infos()

#Renomme les colonnes des dataFrames clil
richpwrClilFirst = richpwrClilFirst.rename(columns={"id": "clilFirstId", "libelle": "clilFirstLibelle", "color": "clilFirstColor"}) 
richpwrClilSecond = richpwrClilSecond.rename(columns={"id": "clilSecondId", "libelle": "clilSecondLibelle", "color": "clilSecondColor"})

#Supprime les colonnes clil du dataframe principal
richpwr.drop(columns=['clilFirst', 'clilSecond'], inplace=True)

#Concatene les 3 dataframes
final_richpwr = pd.concat([richpwr, richpwrClilFirst, richpwrClilSecond], axis=1)
final_richpwr.infos()
final_richpwr.shape

#Sauvegarde le resultat en CSV
final_richpwr.to_csv('richpwr.csv', index=False)
