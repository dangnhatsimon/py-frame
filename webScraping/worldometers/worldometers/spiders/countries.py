import logging
import scrapy
# from scrapy.shell import inspect_response # for debugging
# from scrapy.utils.response import open_in_browser # for debugging

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country/"]
    country_name = ''
    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            self.country_name = name
            link = country.xpath(".//@href").get()
            
            # absolute_url = f"https://www.worldometer.info{link}"
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url = absolute_url)
            
            yield response.follow(url = link, callback = self.parse_country, meta = {"country_name": name})
        # yield response.follow(url = 'https://www.worldometers.info/world-population/china-population/', callback = self.parse_country, meta = {"country_name": 'China'}) # for debugging
            
    def parse_country(self, response):
        # inspect_response(response, self)
        # open_in_browser(response) # for debugging
        # logging.info(response.url) # for debugging
        # logging.info(response.status) # for debugging
        # logging.warning(response.status) # for debugging
        name = response.request.meta["country_name"]
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield {
                'country_name': self.country_name,
                'year': year,
                'population': population
            }