import scrapy
import json

class NBABasketballSpider(scrapy.Spider):
    name = 'nba.basketball'
    start_urls = [
        'https://content-api-prod.nba.com/public/1/content?page={}&count=100&types=post'.format(i) for i in range(1, 101)
    ]

    def parse(self, response):
        results = json.loads(response.text).get("results").get("items")
        for post in results:
            url = post["permalink"]
            metadata = {
                "title": post.get("title"),
                "publish_date": post.get("date"),
                "excerpt": post.get("excerpt"),
                "author": post.get("author").get("name"),
                "category": post.get("category")
            }
            yield scrapy.Request(url=url, callback=self.parse_post, meta=metadata)

    def parse_post(self, response):

        yield {
            'title': response.meta.get("title"),
            'publish_date': response.meta.get("publish_date"),
            'excerpt': response.meta.get("excerpt"),
            'author': response.meta.get("category"),
            'content': json.loads(response.xpath('//*[@id="__next"]/script[1]/text()').get()).get("articleBody").strip()
        }