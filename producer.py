import requests
from kafka import KafkaProducer
import json # Configuration du Kafka Producer
import time

kafka_broker = "localhost:9092"
kafka_topic = "github-data"

producer = KafkaProducer(bootstrap_servers=kafka_broker,
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))

i = 0
while True:
    i =+1

    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=1&sort=duedate&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&facet=duedate&refine.nom_arrondissement_communes=Paris&refine.is_installed=OUI&timezone=Europe%2FParis"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Envoi des données à Kafka
        producer.send('quickstart-events', data)
        time.sleep(5)
    else:
        print("Erreur lors de la requête : {}".format(response.status_code))
