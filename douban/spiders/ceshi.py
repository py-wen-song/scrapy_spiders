import scrapy,json


class MovieSpider(scrapy.Spider):
    name = 'ceshi'
    start_urls=[]
    for x in range(100):
        start_urls.append('http://wensong.xyz/ip')

    def parse(self, response):
        print(json.loads(response.body))
