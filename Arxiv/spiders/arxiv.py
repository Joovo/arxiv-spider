# -*- coding: utf-8 -*-
import scrapy
from Arxiv.items import *
import re


class ArxivSpider(scrapy.Spider):
    name = 'arxiv'
    allowed_domains = ['arxiv.org']
    start_urls = ['https://arxiv.org/list/cs.CV/1801?show=1000']

    def parse(self, response):
        self.logger.info('A response from %s just arrived' % response.url)
        # get num line
        num = response.xpath('//*[@id="dlpage"]/small[1]/text()[1]').extract()[0]
        # get max_index
        max_index = int(re.search(r'\d+', num).group(0))
        for index in range(1, max_index + 1):
            item = ArxivItem()
            # get title and clean data
            title = response.xpath('//*[@id="dlpage"]/dl/dd[' + str(index) + ']/div/div[1]/text()').extract()
            # remove blank char
            title = [i.strip() for i in title]
            # remove blank str
            title = [i for i in title if i is not '']
            # insert title
            item['title'] = title[0]

            authors = ''
            # authors list
            xpath_a = '//*[@id="dlpage"]/dl/dd[' + str(index) + ']/div/div[2]//a/text'
            author_list=reponse.xpath(xpath_a).getall()
            authors = str.join('',author_list)
          
            item['authors'] = authors

            item['subjects']=response.xpath('string(//*[@id="dlpage"]/dl/dd['+str(5)+']/div/div[5]/span[2])').extract_first()


            yield item

        yield scrapy.Request('https://arxiv.org/list/cs.CV/1802?show=1000', callback=self.parse)
