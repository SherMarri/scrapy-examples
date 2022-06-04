from typing import List, Optional
import scrapy
from scrapy.spiders import Spider
from scrapy.http.response.text import TextResponse
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup, PageElement
from pakwheels.items import PakwheelsItem, PakwheelsList


class LatestAdsSpider(Spider):
    name = "latest_ads"
    allowed_domains = ["www.pakwheels.com"]
    start_urls = [
        "https://www.pakwheels.com/used-cars/search/-/",
        "https://www.pakwheels.com/used-cars/search/-/?page=1",
        "https://www.pakwheels.com/used-cars/search/-/?page=2",
        "https://www.pakwheels.com/used-cars/search/-/?page=3",
        "https://www.pakwheels.com/used-cars/search/-/?page=4",
        "https://www.pakwheels.com/used-cars/search/-/?page=5",
        "https://www.pakwheels.com/used-cars/search/-/?page=6",
        "https://www.pakwheels.com/used-cars/search/-/?page=7",
        "https://www.pakwheels.com/used-cars/search/-/?page=8",
        "https://www.pakwheels.com/used-cars/search/-/?page=9",
        "https://www.pakwheels.com/used-cars/search/-/?page=10",
    ]

    def parse(self, response: TextResponse):
        soup = BeautifulSoup(response.body, "html.parser")
        # print(response.body)
        ad_divs: List[BeautifulSoup] = soup.find_all(
            "ul",
            class_="list-unstyled search-results search-results-mid next-prev car-search-results",
        )
        ads: List[PakwheelsItem] = []
        for div in ad_divs:
            ad_elems: List[BeautifulSoup] = div.find_all(
                "li", class_="classified-listing"
            )
            for elem in ad_elems:
                listing_id = elem.get("data-listing-id").strip()
                title = (
                    elem.find("a", class_="car-name ad-detail-path")
                    .get("title")
                    .strip()
                )
                city = (
                    elem.find("ul", class_="list-unstyled search-vehicle-info fs13")
                    .find("li")
                    .text.strip()
                )
                other_elems = elem.find(
                    "ul", class_="list-unstyled search-vehicle-info-2 fs13"
                )
                other_facts = other_elems.find_all("li")
                year = other_facts[0].text.strip()
                mileage = other_facts[1].text.strip()
                fuel_type = other_facts[2].text.strip()
                cc = other_facts[3].text.strip()
                transmission = other_facts[4].text.strip()
                price = elem.find("div", class_="price-details").text.strip()
                ads.append(
                    PakwheelsItem(
                        listing_id=listing_id,
                        name=title,
                        city=city,
                        year=year,
                        mileage=mileage,
                        fuel_type=fuel_type,
                        cc=cc,
                        transmission=transmission,
                        price=price,
                    )
                )

        yield PakwheelsList(items=ads)

        self.logger.info("Total ad divs: %s", len(ad_divs))
