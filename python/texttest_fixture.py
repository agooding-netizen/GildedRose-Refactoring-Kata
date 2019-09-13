# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=6, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 12
    import sys
    with open("Test_Result.txt", 'w+') as file:
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            print("-------- day %s --------" % day, file=file)
            print("name, sellIn, quality", file=file)
            for item in items:
                print(item, file=file)
            print("", file=file)
            GildedRose(items).update_quality()

    with open('GOLDEN_MASTER.txt') as f1, open('Test_Result.txt') as f2, open('difference_to_master.txt', 'w') as outfile:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print(line2, end='', file=outfile)

