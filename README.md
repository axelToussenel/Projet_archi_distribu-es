# Projet_archi_distribuées

Ce github contient notre projet d'*Architecture Distribuée* encadré par M. Lima. Nous avons décidé de travailler sur une corrélation entre la **concentration de velib** et le **taux de pollution** par zone géographique dans la capitale.

Dans ce Readme sera expliqué le cheminement à travers différents outils comme "[**Kafka**](https://kafka.apache.org/)", "[**Spark**](https://spark.apache.org/)" et "[**Zookeper**](https://zookeeper.apache.org/))" pour arriver au produit final : un **Dashboard** disposant les données ainsi traitées de manière visuelle.

Une fois sur l'invite de commandes *Kafka*, vous pouvez lancer :

  - Un **Producer**, qui écrit les données. Il les envoie à un **Topic** ou « catégorie » dans lequel les messages sont stockés et publiés.
 
      *kafka-console-consumer.sh --topic quickstart-events --bootstrap-server localhost:9092*
  
  - Un **Consumer**, celui qui s’occupe de lire les données.
 
      *kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092*

