---
title: "[Smart Home / DIY] Installing a New PMS9003M Laser Dust Sensor in Atomy Air Purifier"
date: 2026-08-09T13:20:00+09:00
draft: false
categories: ["🏠 Smart Home & DIY", "🛠️ Home Assistant & IoT"]
tags: ["ESP8266", "Home Assistant", "IoT", "Smart Home", "Atomy Air Purifier", "PMS9003M", "Dust Sensor"]
description: "A quick DIY guide on replacing/installing a Plantower PMS9003M particulate matter sensor into an Atomy Air Purifier (AAP-KR19W) to restore PM1.0, PM2.5, and PM10 readings in Home Assistant."
---

# Breathing New Life into the Atomy Air Purifier: PMS9003M Sensor Installation

In my previous post, I documented the complete local integration of an abandoned Atomy Air Purifier (AAP-KR19W) into Home Assistant without relying on the dead official cloud servers.

While the integration was a huge success, there was one minor issue: the physical laser dust sensor module inside the device was either broken or missing. As a result, the particulate matter (PM) readings on my Home Assistant dashboard were stuck at `0`.

To restore its full functionality, I looked for compatible replacement sensors and discovered that the **Plantower PMS9003M** laser dust sensor—commonly used in Xiaomi air purifiers and various smart home DIY projects—is perfectly compatible with this unit!

---

## 1. Buying the PMS9003M Sensor from Naver Shopping

I quickly ordered a replacement PMS9003M sensor from Naver Shopping. It was very affordable, costing around 10,000 to 20,000 KRW including shipping. The sensor arrived quickly in just a few days.

---

## 2. Installing the Sensor into the Air Purifier

I opened the sensor cover on the side of the air purifier to reveal the empty slot and installed the newly purchased PMS9003M.

Here is a photo of the completed installation. As you can see, the form factor is an exact match—no modifications, drilling, or cutting required.

![PMS9003M Sensor Installed](/IMG_2256.jpg)

It secures perfectly with just two screws, and the wiring harness clips right in. The whole physical installation took less than a minute.

---

## 3. Verifying the Sensor in Home Assistant

After plugging the sensor in, I turned the air purifier back on and opened my Home Assistant dashboard.

As I analyzed in the previous post, the Tuya board inside this device already has the built-in logic to handle three separate particle sizes: **PM1.0 (DP 11), PM2.5 (DP 10), and PM10 (DP 9)**.

The result? A massive success! Without any additional software configuration or coding, Home Assistant instantly started receiving live, highly accurate measurements for PM1.0, PM2.5, and PM10. 

*I even stirred up some dust near the sensor to test it, and the values spiked immediately, proving its excellent sensitivity.*

---

## Conclusion

If the PM sensor on your air purifier is reading strange values, stuck at zero, or completely broken, you don't need to throw away the whole machine! I highly recommend ordering a standalone `PMS9003M` sensor from online stores like Naver Shopping and swapping it out yourself.

It feels incredibly rewarding to not only resurrect an abandoned smart device via Home Assistant but also physically repair its hardware to make it 100% functional again! 👍
