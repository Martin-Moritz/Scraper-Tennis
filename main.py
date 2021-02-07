from app import app
from app.data import *
from data.redis import *
from newscrawler.run_spider import *
import os

# Pour lancer l'app avec Python directement
if __name__ == '__main__':

    # Si des données ont déjà été scrapées précédemment
    if os.path.exists("data/singles.json"):
        os.remove("data/singles.json")
    else:
        print("data/singles.json n'existe pas")

    if os.path.exists("data/doubles.json"):
        os.remove("data/doubles.json")
    else:
        print("data/doubles.json n'existe pas")

    # Scraping des données et stockage temporaire dans des fichiers json
    web_scraping()

    # Stockage des données dans une base de données redis
    redis_init()

    # lancement de l'application flask
    app.run(host='0.0.0.0',debug=True)
