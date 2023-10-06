# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Deal with Sulfuras
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            # Deal with Aged Brie
            elif item.name == "Aged Brie":
                item.quality = min(50, item.quality + 1)
            # Deal with Backstage passes
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in > 10:
                    item.quality += 1
                elif 6 <= item.sell_in <= 10:
                    item.quality += 2
                elif 1 <= item.sell_in <= 5:
                    item.quality += 3
                # The item has expired
                else:
                    item.quality = 0
                # Set the maximum quality to 50
                if item.quality > 50:
                    item.quality = 50
            # Deal with normal items with the exception of Conjured items
            else:
                degrade = 1
                # Conjured items degrade twice as fast as normal items
                if "Conjured" in item.name:
                    degrade *= 2
                # The item has expired
                if item.sell_in <= 0:

                    degrade *= 2
                # The minimum quality is 0
                item.quality = max(0, item.quality - degrade)
            item.sell_in -= 1