# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_concert_under_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(33, items[0].quality)

    def test_concert_under_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(32, items[0].quality)

    def test_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(31, items[0].quality)

    def test_concert_expired(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_concert_max_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_concert_max_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_concert_max(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 13, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_vest(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].quality)

    def test_vest_expired(self):
        items = [Item("+5 Dexterity Vest", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)

    def test__vest_min(self):
        items = [Item("+5 Dexterity Vest", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_mongoose(self):
        items = [Item("Elixir of the Mongoose", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].quality)

    def test_mongoose_expired(self):
        items = [Item("Elixir of the Mongoose", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)

    def test_mongoose_min(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_sulfuras_expired(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_brie(self):
        items = [Item("Aged Brie", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_brie_expired(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)

    def test_brie_max(self):
        items = [Item("Aged Brie", 12, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)

    def test_conjured_expired(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(16, items[0].quality)

    def test_conjured_min(self):
        items = [Item("Conjured Mana Cake", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_concert_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_vest_sell_in(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_mongoose_sell_in(self):
        items = [Item("Elixir of the Mongoose", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)

    def test_brie_sell_in(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_conjured_sell_in(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
