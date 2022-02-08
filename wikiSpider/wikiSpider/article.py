import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_request(self):
        urls = [
            "https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%84%A0",
            "https://ko.wikipedia.org/wiki/%EC%8A%A4%EC%9C%84%ED%94%84%ED%8A%B8_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4)",
            "https://ko.wikipedia.org/wiki/%ED%95%A8%EC%88%98%ED%98%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D",
            "https://ko.wikipedia.org/wiki/%EB%AA%AC%ED%8B%B0_%ED%8C%8C%EC%9D%B4%ED%8A%BC"
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print("URL is %s" % url)
        print("title is %s" % title)
