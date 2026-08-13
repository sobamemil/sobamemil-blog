---
title: "Discontinued Atomy Air Purifier Home Assistant Local Integration (Tuya Bypass)"
date: 2026-08-13T14:14:00+09:00
draft: false
tags: ["AirPurifier", "HomeAssistant", "Atomy", "IoT", "FilterReplacement", "AAP-KR19W"]
categories: ["Smart Home DIY", "Smart Home DIY/Home IoT"]
---

The time has come to replace the filters for the large **Atomy Air Purifier (AAP-KR19W)**, which reliably takes care of the indoor air quality in my home.
Today, I'll share a brief review of the simple filter replacement process and outline a basic concept for how I might integrate this device into Home Assistant (HA) in the future to run it smartly.

## 1. Dual Filter Setup, Satisfying Performance

The biggest advantage of the Atomy large air purifier is, undoubtedly, its overwhelmingly large filter system.
The filter for this product uses a method of layering two filters: a black **deodorizing filter** and a white **non-woven fabric-like filter**. Because the device itself is a large model, filters go into the top and bottom respectively, so for a full replacement, you need to purchase a total of 2 sets of these layered filters.

![Inside the Air Purifier and Filters](/images/posts/moving/IMG_2466.jpeg)

**The filter replacement process is almost anti-climactically simple.**
There is no need to grab a screwdriver to take apart the internal board; you just open the outer filter cover.

1. Grab the gap at the top of the front cover and pull to remove it.
2. Take out the dust-contaminated existing filters (2 sets of black + white) from the upper and lower spaces and put them in a garbage bag.
3. Smoothly slide the new filter sets, with the plastic wrapping removed, right into place, matching the shape.
4. Close the cover back up, turn on the power, and you're done!

After turning it on post-replacement, the air coming out definitely smells fresher. Having thick filters in both the top and bottom gives a reassuring feeling that it will effectively capture not only fine dust but also odors.

## 2. Future HA Local Integration Concept

As I've covered in other posts before, this product has several issues, such as the discontinuation of its dedicated app support. Ultimately, my goal is to completely revamp it locally and attach it to HA, bypassing external clouds altogether.

Today I simply replaced the filters and closed it up, but later, I plan to disassemble the board and either hack or replace the internal Wi-Fi communication chipset (like the ESP module) to flash a custom firmware (like ESPHome, Tasmota, etc.).

Once I gain local control authority, it could be reborn as a perfect smart air purifier, automatically adjusting the fan speed based on indoor fine dust levels (sensor values). I'll cover the detailed hacking(?) and integration process in my next post!
