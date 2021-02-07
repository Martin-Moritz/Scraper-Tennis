import redis
import json

# local ?
LOCAL = False

# Connection de la base redis
redis_client = redis.StrictRedis(host='localhost' if LOCAL else 'redis', charset='utf-8', decode_responses=True)

def redis_init():
    """
    Permet de stocker les données scrapées dans une base de données redis.
    Les données dans la base sont sous la forme clés/valeurs, où les valeurs sont
    ici des dictionnaires tirés de fichiers json.
    """

    # Redis est bien connecté ?
    redis_connected = redis_client.ping()
    print("redis is connected : ", redis_connected)

    # Lecture des données présentes dans les fichiers json
    with open('data/singles.json') as singles_data :
        singles_dict_list = json.load(singles_data)

    with open('data/doubles.json') as doubles_data :
        doubles_dict_list = json.load(doubles_data)

    # Stockage des données dans la base de données Redis
    for i in range(len(singles_dict_list)):
        redis_client.hmset('single ' + str(i+1), singles_dict_list[i])
        redis_client.hmset('double ' + str(i+1), doubles_dict_list[i])
