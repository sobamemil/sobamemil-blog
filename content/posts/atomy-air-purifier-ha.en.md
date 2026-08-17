---
title: "Discontinued Atomy Air Purifier: Home Assistant Local Integration (Bypassing Tuya)"
date: 2026-08-13T14:14:00+09:00
draft: false
tags: ["AirPurifier", "HomeAssistant", "Atomy", "IoT", "FilterReplacement", "AAP-KR19W"]
categories: ["Smart Home DIY", "Smart Home DIY/Home IoT"]
---

The large Atomy air purifier (AAP-KR19W) that handles air quality in the house was due for a filter change. This post covers the filter replacement, plus some thoughts on eventually getting this thing onto Home Assistant.

## The two-filter-set design

The best thing about this purifier is its oversized filter system: a black deodorizing filter and a white non-woven filter stacked together. Since it's a large unit, filters go in both the top and bottom, so a full replacement means buying two of these stacked sets.

![Inside the air purifier with the filters](/images/posts/moving/IMG_2466.jpeg)
![The deodorizing filter and non-woven filter stacked together](/images/posts/moving/IMG_2467.jpeg)

Replacing the filters just means popping open the front cover, nothing more involved than that.

1. Grip the gap at the top of the front cover and pull it off.
2. Pull out the old, dust-caked filters (black + white, top and bottom) and bag them for disposal.
3. Unwrap the new filter sets and push them into place.
4. Close the cover and power it back on.

There are compatible third-party filters on the market too, but in my experience they weren't much cheaper than the genuine ones and didn't fit quite as snugly. If the price difference is small, I'd just go with the genuine filter.

After the swap, the air coming out definitely smells fresher. With thick filters top and bottom, it feels like it should handle both dust and odor well.

## Local Home Assistant integration, down the road

As covered in an earlier post, this unit's app support has been discontinued along with a few other issues, so the long-term goal is to strip out the cloud dependency entirely and run it fully local through HA.

This time around I only swapped the filters and closed it back up, but eventually I want to open up the board, get into the Wi-Fi chipset (an ESP module or similar), and flash it with something like ESPHome or Tasmota.

Once I have local control, I should be able to auto-adjust fan speed based on indoor particulate readings, turning it into a proper smart air purifier. I'll cover the hacking and integration details in a future post.
