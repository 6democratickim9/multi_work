import scrapy
from movie_scrap.items import MymovieItem
from scrapy.http import Request



# descs -> 40개의 데이터를 -> 10개의 데이터로 만든다!(공백제거)
def remove_space(descs:list) -> list:
    result = []
    # 공백 제거
    for i in range(len(descs)):
        if len(descs[i].strip()) >0:
            result.append(descs[i].strip())
 
    return result

URL= 'https://movie.naver.com/movie/point/af/list.nhn?&page=%s'
start_page =1

class MymovieBotsSpider(scrapy.Spider):
    name = 'mymovie_bots'
    allowed_domains = ['naver.com']
    start_urls = [URL%start_page]
    # /가 들어가면 파일이 아니라 디렉토리가 돼서 데이터를 못가져올수도 있음
    # /는 뺴준다

    def start_requests(self):
        for i in range(2):
            yield Request(url= URL %(i+start_page), callback=self.parse)
    

    def parse(self, response):
        # response.xpath()
        # response.css()
        # pass
        titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        stars = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        descs = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/text()').extract()
        converted_space= remove_space(descs)
        authors = response.css('.author::text').extract()
        dates = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()
        
        # 아이템 내용 다 넣어야 export된다!
        for row in zip(titles,stars,converted_space,authors,dates):
            item = MymovieItem()
            item['title'] = row[0]
            item['star'] = row[1]
            item['desc'] = row[2]
            item['author'] = row[3]
            item['date'] = row[4]

            yield item #제너레이터

        # items = []

        # for i in range(len(titles)): # titles는 (0~9)정도일거임 --> 그래서 잘못됐따!!!!!!!!!
        #     item = MymovieItem()
        #     item['title'] = titles[i]
        #     item['star'] = stars[i]
        #     item['desc'] = descs[i]
        #     item['author'] = authors[i]
        #     item['date'] = dates[i]

        #     items.append(item)

        # return items




