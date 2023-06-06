import scrapy


class WhiskeySpider(scrapy.Spider):
    name = "whisky"
    start_urls = ["https://www.whiskyshop.com/scatch-whisky&item_availability=In+Stock"]

    def parse(self, response):
        for products in response.css("div.product-item-info"):
            yield {
                "name": products.css("a.product-item-link::text").get(),
                "price": products.css("span.price::text").get().replace("£", ""),
                "link": products.css("a.product-item-link").attrib["href"],
            }
