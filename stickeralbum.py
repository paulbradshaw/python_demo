#!/usr/bin/env python

#this is needed to save the data in a sql database
import scraperwiki
import random

stickers = range(0,638)
#for sticker in stickers:
 #   print sticker
packet = range(1,6)
album = []
swaps = []
record = {}

def openpacket(album, swaps,index):
    swapratio = 0
    for each in packet:
        sticker = random.randint(0,638)
        print sticker
        if sticker in album:
            swaps.append(sticker)
            swapratio = swapratio+1
        else:
            album.append(sticker)
        #print album, swaps
        #print len(album), len(swaps)
        #print swapratio
    record['packet'] = index
    record['ratio'] = swapratio
    record['album'] = len(album)
    record['swaps'] = len(swaps)
    print record
    scraperwiki.sqlite.save(['packet'],record)
    return album, swaps

for i in range(1,1000):
    index = i
    openpacket(album,swaps,index)

# Saving data:
# unique_keys = [ 'id' ]
# data = { 'id':12, 'name':'violet', 'age':7 }
# scraperwiki.sql.save(unique_keys, data)
