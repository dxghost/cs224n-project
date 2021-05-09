import scrapy

class TalkSportsFootballSpider(scrapy.Spider):
    name = 'talksports.football'
    start_urls = [
        'https://talksport.com/football/page/{}/'.format(i) for i in range(1, 4565)
    ]

    def parse(self, response):
        post_links = response.css('div.sun-row div.col div.teaser-item a.teaser-anchor::attr(href)').getall()
        yield from response.follow_all(post_links, self.parse_post)

    def parse_post(self, response):

        yield {
            'title': response.css("h1.article__headline::text").get(),
            'content': " ".join(response.css("div.article__content p::text").getall()),
            'tags':  response.xpath('//*[@id="thesun-head-js-extra"]/text()').re('var thesun_googletag = ({.*});'),
            'author': response.css("span.article__author-name::text").get().strip(),
            'publish_date': " ".join(response.css("div.article__published span::text").getall())
        }

# TODO ftfy.fix_text
# TODO cawled until 1885

'''{'downloader/request_bytes': 24596783,
 'downloader/request_count': 54194,
 'downloader/request_method_count/GET': 54194,
 'downloader/response_bytes': 1106046240,
 'downloader/response_count': 54194,
 'downloader/response_status_count/200': 54193,
 'downloader/response_status_count/301': 1,
 'elapsed_time_seconds': 4797.921979,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'shutdown',
 'finish_time': datetime.datetime(2021, 5, 8, 3, 43, 4, 532903),
 'httpcompression/response_bytes': 4213626328,
 'httpcompression/response_count': 54193,
 'item_scraped_count': 52305,
 'log_count/DEBUG': 106499,
 'log_count/INFO': 91,
 'memusage/max': 112046080,
 'memusage/startup': 56274944,
 'request_depth_max': 1,
 'response_received_count': 54193,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 54193,
 'scheduler/dequeued/memory': 54193,
 'scheduler/enqueued': 54720,
 'scheduler/enqueued/memory': 54720,
 'start_time': datetime.datetime(2021, 5, 8, 2, 23, 6, 610924)}
'''