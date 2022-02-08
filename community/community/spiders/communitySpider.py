import scrapy


class CommunitySpider(scrapy.Spider):
    # 이름 정의
    name = "communityCrawler"
    # 크롤링할 사이트 주소
    start_url = []

    def start_requests(self):
        for i in range(1, 5, 1):
            yield scrapy.Request("https://www.clien.net/service/board/park?&od=T31&category=0&po=%d" % i, self.parse_clien)

    def parse_clien(self, response):
        # response를 통해서 웹에 접근
        for sel in response.xpath('//div/div[@class="list_item symph_row'):
            item = CommunityItem()

            item['source'] = "클리앙"
            item['category'] = "free"
            item['title'] = sel.xpath(
                'div[@class = "list_title"]/a/span/text()').extract()[0]
            item['url'] = 'https://www.clien.net/service/board/park?&od=T31&category=0&po=0' + \
                sel.xpath(
                    'div[@class = "list_title"]/a/@href').extract()[0][2:]
