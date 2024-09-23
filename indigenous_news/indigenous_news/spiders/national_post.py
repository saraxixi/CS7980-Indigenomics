import time
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from threading import Lock


class national_post(scrapy.Spider):
    name = 'nationalpost'
    allowed_domains = ['nationalpost.com']
    start_urls = ['https://nationalpost.com/search/?search_text=indigenous&date_range=-365d&sort=score']
    count = 0
    max_count = 10

    def __init__(self, *args, **kwargs):
        super(national_post, self).__init__(*args, **kwargs)
        # Initialize Selenium WebDriver
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.lock = Lock()

    def parse(self, response):
        articles = response.xpath("//div[contains(@class, 'article-card__details')]")
        
        for article in articles:
            if self.count >= self.max_count:
                return
            item = {}
            href = article.xpath("./a/@href").get()
            item["title"] = article.xpath("./a/h3/@title").get()
            item["brief"] = article.xpath("./a/p/text()").get()
            item['url'] = response.urljoin(href)

            self.count += 1
            
            yield scrapy.Request(
                url=item['url'],
                callback=self.parse_detail,
                meta={"item": item},
                dont_filter=True
            )

        # self.count += 20
        if self.count <= self.max_count:
            next_page_url = f"https://nationalpost.com/search/?search_text=indigenous&date_range=-365d&sort=score&from={self.count}"
            yield scrapy.Request(
                url=next_page_url,
                callback=self.parse,
                dont_filter=True
            )

    def parse_detail(self, response):
        item = response.meta['item']
        item["content"] = " ".join(response.xpath("//article//p/text()").getall())
        item["publish_date"] = response.xpath("//time[@class='date__text']/text()").get()
        yield item

    def closed(self, reason):
        # Clean up the driver when the spider is closed
        self.driver.quit()
