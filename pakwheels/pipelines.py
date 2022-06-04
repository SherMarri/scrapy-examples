# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from typing import List
import uuid
from itemadapter import ItemAdapter
import json
from pakwheels.items import PakwheelsItem, PakwheelsList
from scrapy.exceptions import DropItem


class PakwheelsPipeline:
    def process_item(self, item_list: PakwheelsList, spider):
        # print("Title: ", item.get("name"))
        # print("City: ", item.get("city"))
        file_name = uuid.uuid1()
        items: List[PakwheelsItem] = item_list.get("items")
        if len(items) == 0:
            raise DropItem()

        # item_dicts = [{k: v for k, v in item.items()} for item in items]
        # directory = "data/unprocessed"
        # os.makedirs(directory, exist_ok=True)
        # with open(f"{directory}/{file_name}.json", "w") as file:
        #     json.dump(item_dicts, file)
        return item_list
