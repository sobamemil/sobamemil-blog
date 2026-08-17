---
title: "Commax Wallpad Home Assistant Integration and Elfin EW11 Setup Guide"
date: 2026-08-13T14:12:00+09:00
draft: false
tags: ["HomeAssistant", "Commax", "Wallpad", "IoT", "EW11"]
categories: ["Smart Home DIY", "Smart Home DIY/Home IoT"]
---

The wallpad that comes standard in most Korean apartments is wired into the lighting, heating, ventilation, gas valve, and even the elevator call button, which makes it both an appealing target and something you eventually have to deal with if you're serious about a smart home.

The new apartment I moved into has a Commax wallpad installed. This post covers the first step toward Home Assistant integration: analyzing the hardware and locating the communication lines.

## Removing the wallpad and checking inside the junction box

The wallpad on the living room wall came off easily, just loosen the top screw and lift the unit up.

Opening the junction box near the shoe cabinet, I found it wasn't just a network patch panel, it also housed the wallpad's main control board, a Commax CAP-1400YX.

![The Commax CAP-1400YX main board nameplate inside the junction box](/images/posts/moving/IMG_2483.jpeg)

The lines running out to each room were plugged into connectors labeled things like room phone, kitchen phone, and entrance.

![Connectors labeled for the room phone, kitchen phone, entrance, and more](/images/posts/moving/IMG_2473.jpeg)

## Looking for the RS-485 line

Most apartment wallpad systems run on RS-485 serial communication. There were stickers and silkscreen printing next to the connectors on the board with a pinmap, so I used that to roughly locate the gas valve, lighting, boiler, and door lock lines. That said, this isn't fully verified yet, I'll need to hook up the EW11 and actually read the signal to know for sure which lines are 485+/485-.

![Communication lines labeled for gas, phone, and more](/images/posts/moving/IMG_2477.jpeg)

> Be careful of static and shorts whenever you're working inside the junction box. If you damage the main board, the repair bill can add up fast.

## Next up: bringing in an Elfin EW11

To get the RS-485 signal onto Wi-Fi as TCP/IP, I ordered an Elfin EW11, a module that's popular among smart home users, from AliExpress.

It hasn't arrived yet, so I haven't made the physical connection. Once it does, I'll wire it into the RS-485 terminal in the junction box, pull packets over MQTT, and start working through the Commax protocol piece by piece. I'll pick this up in the next post.
