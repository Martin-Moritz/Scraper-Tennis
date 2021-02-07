import scrapy
import json

## Scraping plus précis, exemple d'adresse : https://www.atptour.com/en/rankings/singles?rankDate=2021-02-01&rankRange=0-100&countryCode=FRA

class SinglesSpider(scrapy.Spider):
    name = 'singles'
    allowed_domains = ['www.atptour.com/en/rankings/singles']
    start_urls = ['https://www.atptour.com/en/rankings/singles/']
    user_agent = ""
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI':'data/singles.json'
    }

    def parse(self, response):

        # rank-cell
        list_ranks =  response.css('td.rank-cell::text').getall()
        for i in range(len(list_ranks)):
            list_ranks[i] = list_ranks[i].replace('\r',"")
            list_ranks[i] = list_ranks[i].replace('\n',"")
            list_ranks[i] = list_ranks[i].replace('\t',"")

        # country-item
        list_countries =  response.css('div.country-item').getall()
        for i in range(len(list_countries)):
            list_countries[i] = list_countries[i].replace('\r',"")
            list_countries[i] = list_countries[i].replace('\n',"")
            list_countries[i] = list_countries[i].replace('\t',"")
            list_countries[i] = list_countries[i].replace(' onerror="this.remove()"></div>',"")
            list_countries[i] = list_countries[i][-4:-1]

        # player-cell
        list_players = response.css('td.player-cell').css('a::text').getall()
        for i in range(len(list_players)):
            list_players[i] = list_players[i].replace('\r',"")
            list_players[i] = list_players[i].replace('\n',"")
            list_players[i] = list_players[i].strip()

        # age-cell
        list_ages = response.css('td.age-cell::text').getall()
        for i in range(len(list_ages)):
            list_ages[i] = list_ages[i].replace('\r',"")
            list_ages[i] = list_ages[i].replace('\n',"")
            list_ages[i] = list_ages[i].replace('\t',"")

        # points-cell
        list_points = response.css('td.points-cell').css('a::text').getall()

        #tourn-cell
        list_tourns = response.css('td.tourn-cell').css('a::text').getall()

        for i in range(len(list_ranks)):
            data = {'rang' : list_ranks[i],
                   'pays' : list_countries[i],
                   'joueur' : list_players[i],
                   'age' : list_ages[i],
                   'points' : list_points[i],
                   'nb_tournois' : list_tourns[i]
                   }

            yield data
