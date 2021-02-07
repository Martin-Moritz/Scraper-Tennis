from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from newscrawler.newscrawler.spiders.singles import SinglesSpider
from newscrawler.newscrawler.spiders.doubles import DoublesSpider

process = CrawlerProcess(get_project_settings())

def web_scraping():
    """ Fonction pour scraper en temps réel les données du site atptour.com """
    process.crawl(SinglesSpider)
    process.crawl(DoublesSpider)
    process.start()
