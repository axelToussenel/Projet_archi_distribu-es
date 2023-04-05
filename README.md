# Projet_archi_distribuées

Ce github contient notre projet d'*Architecture Distribuée* encadré par M. Lima. Nous avons décidé de travailler sur une corrélation entre la **concentration de vélib** et le **taux de pollution** par zone géographique dans la capitale.

Dans ce Readme sera expliqué le cheminement à travers différents outils comme "[**Kafka**](https://kafka.apache.org/)", "[**Spark**](https://spark.apache.org/)" et "[**Zookeper**](https://zookeeper.apache.org/))" pour arriver au produit final : un **Dashboard** disposant les données ainsi traitées de manière visuelle.

Il vous faudra dans un premier temps vous devrez créer un container **Kafka**, **Zookeeper**, **Spark Master** et **Spark Worker** dans votre plateforme Docker.



Une fois sur l'invite de commandes *Kafka*, vous pouvez lancer :

  - Un **Producer**, qui écrit les données. Il les envoie à un **Topic** ou "catégorie" dans lequel les messages sont stockés et publiés.
 
      *kafka-console-consumer.sh --topic quickstart-events --bootstrap-server localhost:9092*
  
  - Un **Consumer**, celui qui s’occupe de lire les données.
 
      *kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092*



Nous n'avons malheureusement pas pu terminer ce projet pour différentes raisons, nous allons tout de même détailler le Dashboard comme nous l'aurions conçu.

Pour une bonne visualisation, nous avons imaginé des "camemberts" de ce type :

![Dessin sans titre](https://user-images.githubusercontent.com/91553182/230185101-a231e69e-0336-400f-99ed-6eb6c62a803d.png)

Ou même aller plus loin en créant une carte intéractive !
