import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class PostScraper(scrapy.Spider):
    name = 'posts'
    start_urls = [
        'https://old.reddit.com/r/cscareerquestions/',
        'https://old.reddit.com/r/programming/',
        'https://old.reddit.com/r/dataengineering/',
        'https://old.reddit.com/r/csmajors/',
        'https://old.reddit.com/r/machinelearning/',
        'https://old.reddit.com/r/datascience/',
    ]

    count = 0

    def parse(self, response):
        siteTable = response.xpath('//*[@id="siteTable"]')
        posts = siteTable.css('div.link')
        for post in posts:
            yield post.attrib

        next_link = response.css('span.next-button').css('a').attrib['href']
        self.count += 1
        if next_link is not None and self.count < 4:
            yield response.follow(next_link, self.parse)
        else:
            self.count = 0

process = CrawlerProcess(settings={
    'FEEDS': {
        'posts.jl': {'format': 'jsonlines'}
    },
})

process.crawl(PostScraper)
process.start()