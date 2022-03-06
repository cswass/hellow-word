
import scrapy
from selenium import webdriver


class PostSpider(scrapy.Spider):
    name = 'post'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = [] #存储五个列表模块

    #实例化浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='C:\\Users\\qqq\\Desktop\\chromedriver.exe')
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3, 4, 6, 7, 8]
        for index in alist:
             model_url = li_list[index].xpath('./a/@href').extract_first()
             print(model_url)
             self.models_urls.append(model_url)
        for url in self.models_urls:
            yield scrapy.Request(url, callback=self.parse_model)
    #处理每个模块url界面的请求
    def parse_model(self, new_response):
        div_list = new_response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('/div/div[1]/h3/a/text()').extract_first()
            print(title)


