# Projet Python : Data Engineer Tools - Scraper Tennis <a href="https://www.esiee.fr/"> <img align="right" width="8%" height="8%" src="rapport/Logo_ESIEE_Paris.png"> </a>

Projet ESIEE Paris dont l'objectif est de créer une application Web en utilisant plusieurs outils d'ingénieur data (Data Engineer Tools).

## Table des matières

 - [Présentation](#presentation)
 - [User Guide](#user-guide)
 - [Developer Guide](#developer-guide)
 - [Rapport d'analyse](#rapport-danalyse)
 - [Données](#dataset)

## 1 - Presentation <a name="user-guide" />

#### Technologies utilisées

Cette application web est codée en Python, basée sur le package <a href="https://flask.palletsprojects.com/en/1.1.x/">**Flask**</a>.<br>
L'application permet de récupérer des données sur le web en les <a href="https://scrapy.org/">**scrapant**</a>.<br>
Ces données sont ensuite stockées dans une base de données <a href="https://en.wikipedia.org/wiki/Redis">**Redis**</a>.<br>
Enfin, ces données sont affichées à travers un Dashboard interactif réalisé avec le framework <a href="http://dash.plotly.com/">**Dash**</a>.<br>

L'ensemble de l'application est déployée grâce à la technologie <a href="https://www.docker.com/">**Docker**</a>.

#### Thème choisi

Les données utilisées par cette application sont les classements des joueurs de tennis mondiaux en tournois simples (*singles*) et en tournois doubles (*doubles*). Ces données sont issues du site officiel https://www.atptour.com/ et sont scrapées directement depuis les adresses suivantes :

- https://www.atptour.com/en/rankings/singles
- https://www.atptour.com/en/rankings/doubles

Les divers éléments tirés de ces classements sont revisités à travers le dashboard pour faire apparaître de nouvelles informations qui n'étaient pas visibles explicitement sur le site d'origine.

## 2 - User Guide <a name="user-guide" />

### **Installation**

*Installer python au préalable sur la machine utilisée (version 3+).*

##### Télécharger le Projet

Si vous avez l'habitude d'utiliser <a href="https://git-scm.com/">Git</a>, utilisez la commande suivante :

`git clone https://github.com/Martin-Moritz/Scraper-Tennis.git`

Sinon, téléchargez simplement le dossier du projet en format .zip depuis cette page avec **Code -> Download ZIP**

##### Docker

Cette application doit être déployée en utilisant la technologie Docker. Docker est un outil de virtualisation qui permet de lancer toutes les ressources nécessaire du projet sans demander de nombreuses manipulations.

Pour l'installation de **Docker**, suivez les informations suivantes selon votre système d'exploitation :

- **Windows :** https://docs.docker.com/docker-for-windows/install/
- **Linux :** https://docs.docker.com/engine/install/ubuntu/ puis installez **Docker Compose** : https://docs.docker.com/compose/install/
- **MacOs :** https://docs.docker.com/docker-for-mac/install/

Vous pouvez suivre la page complète de commencement de Docker sur la <a href="https://www.docker.com/get-started">page d'installation de Docker</a>.

##### Ouvrir l'invite de commande

> *Windows* et *Linux* : chercher en tapant '*terminal*' dans la barre de recherche.

##### Se placer dans le dossier du projet

> Utiliser la commande `cd <chemin du répertoire>`<br>
> par exemple : 'cd Desktop/scraper-tennis'

### **Utilisation**

*Après avoir téléchargé le dossier du projet et installé Docker (voir ci-dessus) :*

**Lancez l'application en suivant les étapes suivantes :**

- Ouvrez l'invite de commande

- Placez-vous dans le dossier du projet

- Installez les ressources nécéssaires en exécutant la commande `docker-compose build` pour démarrer l'application

Si tout se passe bien :

```
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 193-380-289
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

redis is connected :  True
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
web_1    | 2021-02-07 19:35:39 [werkzeug] INFO:  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

- Exécutez la commande `docker-compose build` pour démarrer l'application

- Attendez quelques instants le chargement de l'application

- Ouvrez votre navigateur internet et affichez le dashboard en *localhost* (entrez l'adresse suivante dans votre navigateur : http://127.0.0.1:5000/)

- Appuyez CTLR+C dans le terminal pour quitter l'application

## 3 - Developer Guide <a name="developer-guide" />

#### Architecture du projet

Le projet est constitué de :

- 4 dossiers :

  - **pycache** : contient une version compressée des modules python afin d'accélérer leur chargement.
  - **app** : contient l'ensemble du code de l'application.
  - **data** : contient les fichiers .csv des données utilisées pour ce projet.
  - **rapport** : contient les images utilisées dans le rapport d'analyse.

* 3 fichiers :

  * **main.py** : fichier python permettant de lancer l'application.
  * **requirements.txt** : liste des modules/packages utilisés dans cette application.
  * **README.md**

#### Architecture du dossier **app**

Le dossier app est constitué d'un dossier *pycache* et de 7 fichiers python :

- **init.py** : permet de créer l'application *flask*.
- **callbacks.py** : contient les fonctions qui permettent d'obtenir des graphiques interactifs.
- **dash.py** : permet de convertir l'application *flask* en une application *Dash*, permettant ainsi la création du dashboard.
- **data.py** : contient le code permettant de trier les jeux de données contenus dans le dossier .data
- **figures.py** : contient les fonctions qui créent les différentes figures et graphiques du dashboard.
- **layout.py** : contient le code permettant de disposer les différents composants et figures sur la page, déterminant ainsi l'aspect du dashboard.
- **navbar.py** : contient le code déterminant l'aspect de la barre de navigation située en haut de la page.

#### Fonctions des différents fichiers

- **callbacks.py** :
  - *update_carte(selected_countries, selected_salarial)*
  > Met à jour la carte choroplèthe en fonction des pays choisis dans le menu déroulant, ainsi qu'en fonction du type d'emploiement sélectionné.

  - *update_histogramme(selected_countries, selected_salarial, selected_year)*
  > Met à jour l'histogramme en fonction des pays et du type d'emploiement choisis, ainsi que de l'année sélectionnée sur le slider situé en dessous.

  - *update_diagramme(selected_countries, selected_salarial, selected_year)*
  > Met à jour le diagramme en barres en fonction des pays et du type d'emploiement choisis, ainsi que de l'année sélectionnée sur le slider situé en dessous.

  - *update_slider(selected_countries, selected_salarial)*
  > Met à jour le slider en fonction des pays et du type d'emploiement choisis pour pouvoir sélectionner des années où des données sont présentes.

  - *update_dropdown(selected_salarial)*
  > Permet d'activer ou désactiver le menu déroulant en fonction du type d'emploiement sélectionné.

  - *update_graphe(selected_countries, selected_salarial)*
  > Met à jour le premier graphique en fonction des pays choisis dans le menu déroulant, ainsi qu'en fonction du type d'emploiement sélectionné.

- **figures.py** :
  - *create_carte(df,focus='world')*
  > Crée la carte choroplèthe avec le dataframe et le focus donnés en paramètres.

  - *create_histogramme(df, year)*
  > Crée l'histogramme avec le dataframe et l'année donnés en paramètres.

  - *create_diagramme(df, year)*
  > Crée le diagramme en barres avec le dataframe et l'année donnés en paramètres.

  - *create_graphe(df)*
  > Crée le premier graphique avec le dataframe donné en paramètre.

## 4 - Rapport d'analyse <a name="rapport-danalyse" />

#### Définition de l'écart salarial femmes-hommes :

L’écart salarial entre les femmes et les hommes est défini comme la différence entre le salaire médian des hommes et des femmes rapportée au salaire médian des hommes. Les données se rapportent d’une part aux salariés à plein temps et de l’autre aux non-salariés.


#### Analyse :

###### **Introduction**

La différence de salaires entre les hommes et les femmes est un fait flagrant concernant l'égalité hommes-femmes en France mais aussi partout dans le monde. La question que nous pouvons nous poser est : l'écart de salaire femmes-hommes se réduit-il au fil des années ?

###### **Le cas de la France**

En France, l'écart salarial en 1995 est de 14,6% pour des personnes salariées.

![FRANCE1](rapport/France1.PNG)

Cet écart est évalué à 13,7% en 2016. On observe une légère baisse, mais l'évolution reste très faible et semble stagner en 20 ans.

![FRANCE2](rapport/France2.PNG)

###### **Dans le reste du monde**

Mais qu'en est-il dans le reste du monde ?

En 1995, l'écart salarial en Europe varie entre 10 et 28% selon les pays. Aux USA, l'écart est évalué à 24,6%. En Australie,  14,5%. Et enfin en Asie de l'Est, l'écart salarial femmes-hommes est de 37% au Japon et de 44% en Corée du Sud !

![MONDE1](rapport/Monde1.PNG)

On remarque une grande diversité de l'inégalité hommes-femmes au niveau des salaires selon les régions du monde.<br>
Heureusement, cet écart salarial semble diminuer dans l'entièreté du globe au fil des ans pour atteindre des valeurs en 2016 de 7 à 17% en Europe, 17% en Amérique du Nord, 11,5% en Australie, 24,6% au Japon et 36,7% en Corée du Sud.

![MONDE2](rapport/Monde2.PNG)

###### **Le cas des auto-entrepreneurs**

Le cas des personnes non-salariées est plus délicat. En effet, beaucoup moins de personnes sont auto-entrepreneurs dans le monde et il sera plus difficile d'évaluer la pertinence des écarts de salaire observés dans le monde.

En 2006, l'écart salarial varie de 12 à 60% selon les pays,les plus grosses inégalités étant observées en Amérique du Nord.

![MONDE3](rapport/Monde3.PNG)

Nénmoins, on observe de manière globale une baisse de cet écart salarial dans le monde au fil des années. En 2016, les valeurs varient entre 8 et 56%.

![MONDE4](rapport/Monde4.PNG)

###### **Conclusion**

Le cas de la France laisse penser que l'écart de salaire entre les hommes et les femmes reste sensiblement le même depuis plus 20 ans.<br>
Cependant, en comparant l'écart salarial en France au reste du monde, on remarque finalement que la France fait partie des pays les plus égalitaires en terme de salaire dans le monde !<br>
Les plus grosses inégalités sont observés en Amérique du Nord, et surtout en Asie. On peut supposer que cela est dû à une grande différence culturelle et de société.

Malgré cela, on remarque une diminution incontestable de l'écart salarial femmes-hommes, et ce, dans l'ensemble des pays du monde. Ainsi, même si de nombreux pays sont encore loin d'être proche d'une égalité totale en terme de salaire entre les hommes et les femmes, tout le monde se dirige à son rythme dans la bonne voie.

#### Aller plus loin...

Notre analyse porte sur la différence de salaires entre les hommes et les femmes de manière gobale.<br>
Cependant, il pourra être pertinent de s'intéresser à l'écart salarial femmes-hommes au sein d'un même secteur d'activité (Agriculture, Industrie, Services...), voire au sein d'un métier précis.

## Dataset <a name="dataset" />

Data utilisée pour l'analyse : https://data.oecd.org/fr/earnwage/ecart-salarial-femmes-hommes.htm

Data secondaire (utilisée pour avoir les noms des pays et des continents en français) :

  - https://sql.sh/ressources/sql-pays/sql-pays.csv
  - https://pkgstore.datahub.io/JohnSnowLabs/country-and-continent-codes-list/country-and-continent-codes-list-csv_csv/data/b7876b7f496677669644f3d1069d3121/country-and-continent-codes-list-csv_csv.csv
