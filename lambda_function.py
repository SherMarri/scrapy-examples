from typing import Any, Text
from pakwheels.spiders.latest_ads import LatestAdsSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


def lambda_handler(event: Any, context: Any) -> Text:
    process = CrawlerProcess(get_project_settings())

    # 'followall' is the name of one of the spiders of the project.
    process.crawl(LatestAdsSpider)
    process.start()  # the script will block here until the crawling is finished
    return "Crawling done."
