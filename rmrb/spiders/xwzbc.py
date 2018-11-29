# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy_splash import SplashRequest

# 打开搜狗微信公众号搜索引擎(Request)
# 查询“人民日报”微信公众号(FormRequest)
# 打开“人民日报”微信公众号(SplashRequest)
# 打开“新闻早班车”(Request)

class XwzbcSpider(scrapy.Spider):
    name = 'xwzbc'     # 人民日报新闻早班车
    allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    start_urls = ['http://weixin.sogou.com/']

    def parse(self, response):
        import time
        today = time.strftime('%Y-%m-%d', time.localtime())
        f = open('xwzbc_' + today + '.html', 'w')
        f.write(response.text)
        f.close()
        yield {'text': response.text}

    search_url = 'https://weixin.sogou.com/'

    # 打开搜狗微信公众号搜索引擎
    def start_requests(self):
        yield Request(self.search_url, callback=self.search)
        # yield SplashRequest(url, args={'images': 0, 'timeout': 3})

    # 搜索“人民日报”微信公众号
    def search(self, response):
        fd = {'type': '1', 'query': '人民日报'}    # 类型1表示“搜公众号”
        yield FormRequest.from_response(response, formdata=fd, callback=self.parse_rmrbwx)

    # 获得“人民日报”微信公众号的URL地址
    def parse_rmrbwx(self, response):
        if 'rmrbwx' in response.text:
            rmrbwx_url = response.xpath('//label[contains(text(), "rmrbwx")]/../../p/a/@href').extract_first()
            yield SplashRequest(rmrbwx_url, callback=self.parse_xwzbc)

    def parse_xwzbc(self, response):
        hrefs = response.xpath('//h4[contains(text(), "新闻早班车")]/@hrefs') .extract_first()
        xwzbc_url = response.urljoin(hrefs)
        #yield {'url': xwzbc_url}
        yield SplashRequest(xwzbc_url, callback=self.parse)
