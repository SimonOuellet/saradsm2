# Automatisation ML GCP
Simon OUELLET 2022  

## Macro planning

- Présentation Prophet
	- Théorie
	- Cas Gleeph
	- Cas Parking
- Automatisation GCP
	- Architecture
		- Rédaction d'un cahier des charges fonctionnel
		- Dessin Draw.io
	- TD Automatisation
		- Objectif
		- Postman
		- Librairie Python
		- Cloud Function
		- Google Cloud Storage
		- Cloud scheduler
		- Big Query
			- SQL
			- ML
		- Looker
		- Prophet / colab
		- Analyse
		- Présentation

## Automatisation GCP
Pédagogie par l'exemple.  

Modèle de prévision du nombre de places libres dans un parking.    

Objectif : Réaliser un service de prévision des places de parking.  

Macro planning:  

1. Organisation  
2. Captation de données  
3. Réalisation d'un modèle
4. Analyse
5. Mise en oeuvre d'un service API

### Organisation & Architecture
#### Rédaction d'un cahier des charges
##### Gabarit
Contexte  
Objectifs  
Livrables attendus  
Communications  
Références et informations techniques  
##### Atlassian
[Confluence](https://www.atlassian.com/wac/software/confluence)   
[Jira](https://www.atlassian.com/software/jira)  
##### Schéma d'architecture
[Draw.io](https://app.diagrams.net)  
Le bon niveau d'information.
### Captation de la données  
[Postman](https://www.postman.com)   
[Opendata Parking La Rochelle](https://opendata.agglo-larochelle.fr/visualisation/information/?id=59ef869b-e326-42d6-b6ce-bba226db5266)  
#### GCP
##### Création d'un projet
- Compte gmail  
- Activation du crédit 300$  
- IAM gestion des droits  
##### GCS Google Cloud Storage
##### GCS Cloud Function  
##### GCS Cloud scheduler  
##### GCS Big Query  
#### Cloud Function de collecte récurrente de la donnée de parking
Python  
- Fichier requirements.txt  
- Création d'une class/librairie Python  
- Externalisation de la configuration avec configparser  

Création d'une Cloud Function getparkingdata.  

Collecte automatique des données grace à l'ordonnancement de l'appel à la Cloud Function via Cloud Scheduler.  

#### Accéder aux données via BigQuery
Création d'une table de données externes.  

#### Utiliser les données de BigQuery avec Colab et réaliser un modèle FB Prophet.  

#### Utiliser Big Query ML pour mettre en oeuvre un modèle ARIMA+
[ARIMA+](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-time-series)

### Réaliser une analyse de performance entre le modèle FB Prophet et ARIMA+  

### Mettre en oeuvre un service API de prédiction

À l'aide d'une Cloud Function, mettre en oeuvre un service de prédiction du nombre de places de parking disponible à venir dans les 3 prochaines heures à l'aide d'un service API.




