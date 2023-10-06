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
            if item.name == 'Aged Brie':
                Brie(item).update_item()
            elif item.name == 'Sulfuras, Hand of Ragnaros':
                Sulfuras().update_item()
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                BackstagePasses(item).update_item()
            elif item.name == 'Conjured Mana Cake':
                Conjured(item).update_item()
            else:
                NormalItem(item).update_item()


class Brie(object):
    def __init__(self, item: Item):
        self.item = item

    def update_item(self):
        self.item.sell_in -= 1
        self.item.quality += 1
        self.item.quality = min(50, self.item.quality)


class Sulfuras(object):
    def update_item(self):
        pass


class BackstagePasses(object):
    def __init__(self, item: Item):
        self.item = item

    def update_item(self):
        self.item.sell_in -= 1

        if self.item.sell_in > 10:
            self.item.quality += 1
        elif 6 <= self.item.sell_in <= 10:
            self.item.quality += 2
        elif 1 <= self.item.sell_in <= 5:
            self.item.quality += 3
        else:
            # the item has expired
            self.item.quality = 0

        # Set the maximum quality to 50
        self.item.quality = min(50, self.item.quality)


class NormalItem(object):
    def __init__(self, item: Item):
        self.item = item
        self.degrade = 1

    def update_item(self):
        self.item.sell_in -= 1

        if self.item.sell_in >= 0:
            self.item.quality -= self.degrade
        else:
            self.item.quality -= self.degrade * 2

        self.item.quality = max(0, self.item.quality)


class Conjured(object):
    def __init__(self, item: Item):
        self.item = item
        # Conjured items degrade twice as fast as normal items
        self.degrade = 1 * 2

    def update_item(self):
        self.item.sell_in -= 1
        if self.item.sell_in >= 0:
            self.item.quality -= self.degrade
        else:
            # The item has expired
            self.item.quality -= self.degrade * 2
        # The minimum quality is 0
        self.item.quality = max(0, self.item.quality)
