# -*- coding: utf-8 -*-

import re

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @staticmethod
    def upgrade(item, rate):
        if item.quality < 50-rate:
            item.quality += rate
        else:
            item.quality = 50

    @staticmethod
    def downgrade(item, rate):
        if item.quality > 0+rate:
            item.quality -= rate
        else:
            item.quality = 0

    @staticmethod
    def sulfuras(item):
        item.quality = 80

    def standard(self, item):
        if item.sell_in > 0:
            self.downgrade(item, 1)
        elif item.sell_in <= 0:
            self.downgrade(item, 2)
        item.sell_in -= 1

    def brie(self, item):
        if item.sell_in > 0:
            self.upgrade(item, 1)
        elif item.sell_in <= 0:
            self.upgrade(item, 2)
        item.sell_in -= 1

    def concert(self, item):
        if item.sell_in > 10:
            self.upgrade(item, 1)
        elif item.sell_in > 5:
            self.upgrade(item, 2)
        elif item.sell_in > 0:
            self.upgrade(item, 3)
        elif item.sell_in <= 0:
            item.quality = 0
        item.sell_in -= 1

    def conjured(self, item):
        if item.sell_in > 0:
            self.downgrade(item, 2)
        if item.sell_in <= 0:
            self.downgrade(item, 4)
        item.sell_in -= 1

    def name_switch(self, item_name, item):
        {
            "Aged Brie": self.brie,
            "Backstage passes to a TAFKAL80ETC concert": self.concert,
            "Sulfuras, Hand of Ragnaros": self.sulfuras,
            "Conjured": self.conjured,
            "Elixir of the Mongoose": self.standard,
            "+5 Dexterity Vest": self.standard
        }[item_name](item)

    @staticmethod
    def conjure_check(item):
        conjured = re.findall(r'[Cc]onjured', item.name)
        if conjured:
            item_name = {"name": "Conjured"}
        else:
            item_name = {"name": item.name}
        return item_name["name"]

    def update_quality(self):
        for item in self.items:
            item_name = self.conjure_check(item)
            self.name_switch(item_name, item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
