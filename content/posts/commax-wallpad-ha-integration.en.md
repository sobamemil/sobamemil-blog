---
title: "Commax Wallpad Home Assistant Integration and Elfin EW11 Installation Guide"
date: 2026-08-13T14:12:00+09:00
draft: false
tags: ["HomeAssistant", "Commax", "Wallpad", "IoT", "EW11"]
categories: ["Smart Home DIY", "Smart Home DIY/Home IoT"]
---

For those seriously building a smart home, the **Wallpad**, a default option in many apartments, is an incredibly attractive toy and a mountain that must be conquered. This is because numerous devices, such as the home's lighting, heating, ventilation system, gas valve, and elevator call, are connected to the wallpad.

The new apartment I moved into came with a **Commax** wallpad. In this post, we will cover the first step to integrate this wallpad into Home Assistant (HA): **analyzing the hardware and securing the communication lines**.

## Step 1: Removing the Wallpad and Analyzing the Terminal Box

The basics of smart home integration involve figuring out how the device communicates. Detaching the wallpad from the living room wall was simpler than I thought. I unscrewed the top screws and slightly lifted the main body upwards, and it easily came off.

Afterwards, I opened the communication terminal box located near the shoe cabinet. When I took apart the bulky equipment in the center of the terminal box, I found that it wasn't a simple network patch panel, but a **Commax CAP-1400YX** board, which acts as the core control board for the wallpad.

![Terminal Box Analysis](/images/posts/moving/IMG_2475.jpeg)
*(The Commax main board inside the terminal box. Numerous communication lines extend to each room.)*

## Step 2: Finding the RS-485 Communication Line

Most apartment wallpad systems use the highly stable **RS-485** serial communication method.
Looking closely at the board, fortunately, a pinmap was kindly printed on stickers and silkscreen next to each connector.

- Gas valve control line
- Lighting control line for each room
- Boiler heating thermostat line
- Front door lock line

Through the wiring diagram, I confirmed that each device was communicating with the main board via the 485+ (TRX+) and 485- (TRX-) lines. What we need to do is plant a 'spy' in the middle of these communication lines to intercept the incoming and outgoing signals (packets) and, conversely, shoot the commands we want.

> ⚠️ **Caution**: When handling the board inside the terminal box, always be careful of static electricity and be careful not to cause a short circuit. If you mess up and the wallpad main board breaks, you could be billed hundreds of dollars in repair costs.

## Step 3: Next Target, Deploying the Elfin-EW11

Now that we have identified the RS-485 communication line, we need equipment that will convert this serial data into a TCP/IP network via Wi-Fi.
Today, I just ordered the **Elfin-EW11**, the most widely used cost-effective module among smart home users, from AliExpress.

The parts haven't arrived yet, so I haven't been able to make the physical connection. When the EW11 module arrives, I plan to bite it onto the RS-485 terminal in the terminal box and set it up to shoot packets to the MQTT server. After that, the process of analyzing and reverse-engineering the Commax protocol (command rules) using a packet capture tool awaits.

Will I be able to successfully display the lighting and heating on the HA dashboard? I'll be back with Part 2: Protocol Analysis and HA Integration as soon as the parts arrive!
