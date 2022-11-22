from datetime import datetime
import requests
import logging
import configparser
import json
from google.cloud import pubsub_v1
from google.cloud import storage

class Harvester:
    """
    Gathering data from open data API
    """
    def __init__(self, env='dev'):
        if env=='dev':
            logging.basicConfig(level=logging.DEBUG)
        self.env = env
        configFilename = "./harvester.conf"
        config = configparser.ConfigParser()
        config.read(configFilename)
        self.project = config[self.env]["projet_id"]
        self.client_storage = storage.Client(project=self.project)
        self.bucket_name = config[self.env]["data_bucket_name"]
        self.bucket = self.client_storage.get_bucket(self.bucket_name)

        self.data_topic_name = config[env]["data_parkinglr_topic_name"] 
        self.publisher = pubsub_v1.PublisherClient()
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subtimeout = 10

    def put_pubsub_data(self, topic, data):
        """Publish a News on a pubsub topic
        :param topic: Topic name to publish the News object.
        :type topic: String
        :param data: The News serialized object.
        :type data: JSON
        :rtype: publisher.future
        :return: future object with the publish's result infos."""
        topic_path = self.publisher.topic_path(self.project, topic)
        logging.debug('pub_data: project=%s', self.project+' topic='+topic)
        logging.debug('pub_data: data: %s ', json.dumps(data))
        future = self.publisher.publish(topic_path, data=json.dumps(data).encode("utf-8"))
        logging.debug('publish result: %s', future.result())
        return future

    def put_gcs_data(self, data_json, ts_fieldname):
        """save in json format a Data object on GCS.
        :param news_json: JSON data object to store on GCS.
        :type data_json: JSON
        """
        blob_name = 'income/' + data_json['parameters']['dataset'] + '_' + ts_fieldname + '.json'
        blob = self.bucket.blob(blob_name)
        blob.upload_from_string(
            data=json.dumps(data_json),
            content_type='application/json'
            )

    def get_and_save_parking_lr(self):
        url = "https://api.agglo-larochelle.fr/production/opendata/api/records/1.0/search/dataset=parking___places_disponibles_en_temps_reel&facet=id&facet=nom&facet=date_comptage&facet=nb_places&facet=nb_places_disponibles&facet=ylat&facet=xlong&facet=coord_x&facet=coord_y&facet=nb_pr&facet=nb_pr_dispo&facet=nb_pmr&facet=nb_pmr_dispo&facet=nb_voitures_electriques&facet=nb_voitures_electriques_dispo&facet=nb_velo&facet=nb_velo_dispo&facet=nb_2r_el&facet=nb_2r_el_dispo&facet=nb_autopartage&facet=nb_autopartage_dispo&facet=nb_2_rm&facet=nb_2_rm_dispo"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
        self.put_pubsub_data(topic=self.data_topic_name, data=response.json())
        self.put_gcs_data(data_json=response.json(), ts_fieldname=response.json()['records'][0]['fields']['date_comptage'].replace(' ','_'))
         

    def get_and_save_parking_nantes(self):
        url = "https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=244400404_parkings-publics-nantes-disponibilites&q=&facet=grp_nom&facet=grp_statut&facet=grp_identifiant&facet=grp_disponible&facet=grp_exploitation&facet=grp_complet&facet=grp_horodatage&facet=idobj&facet=location&facet=disponibilite"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
        self.put_pubsub_data(topic=self.data_topic_name, data=response.json())
        self.put_gcs_data(data_json=response.json(), ts_fieldname=str(datetime.now().strftime("%d%m%Y%H:%M:%S")))

    def get_and_save_parking_yelolr(self):
        url = "https://api.agglo-larochelle.fr/production/opendata/api/records/1.0/search/dataset=yelo___disponibilite_des_velos_en_libre_service&facet=station_nom&facet=velos_disponibles&facet=accroches_libres&facet=nombre_emplacements&facet=station_latitude&facet=station_longitude&facet=geo_point_2d&facet=geojson"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
        self.put_pubsub_data(topic=self.data_topic_name, data=response.json())
        self.put_gcs_data(data_json=response.json(), ts_fieldname=str(datetime.now().strftime("%d%m%Y%H:%M:%S")))
