# Projet_archi_distribuées

Une fois sur l'invite de commandes **Kafka**, vous pouvez lancer :
  - Un **Producer**, qui écrit les données. Il les envoie à un **Topic** ou « catégorie » dans lequel les messages sont stockés et publiés.
 
  kafka-console-consumer.sh --topic quickstart-events --bootstrap-server localhost:9092
  - Un **Consumer**, celui qui s’occupe de lire les données.
 
  kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092

