from scrapy.crawler import CrawlerProcess
from ScrapyPackage.linkedin import LinkedinSpider


class Scraper:
    def __init__(self, companies_links):
        # scrapy_settings = {"ITEM_PIPELINES": {'pipelines.MongoDBPipeline': 1, 'pipelines.JsonWriterPipeline': 2}}
        # process = CrawlerProcess(scrapy_settings)

        process = CrawlerProcess()
        process.crawl(LinkedinSpider, companies_links)
        process.start()  # the script will block here until the crawling is finished
