---
title: "Perfecting Wired Mesh Home Network with ISP Router in Hub Mode"
date: 2026-08-13T14:13:00+09:00
draft: false
tags: ["HomeNetwork", "Mesh", "WiredMesh", "Router", "Network", "HubMode"]
categories: ["Smart Home DIY", "Smart Home DIY/Network"]
---

When building a smart home and using various IoT devices, the one thing you feel most acutely is **'network stability'**. 
In my previous home, a single main router couldn't cover the entire space, so I configured and used a **Wireless Mesh (Wireless Backhaul)** network. However, because it was wireless, there was a drop in speed, and there was the stress of the connection occasionally becoming unstable.

Moving into a newly built apartment this time, I decided to utilize the terminal box to build a perfect and pleasant **Wired Mesh (Wired Backhaul)** environment.

## 1. Failure to Evict ISP Router and the Hub Mode Compromise

My very first goal was to remove the underperforming default router provided by the ISP (Internet Service Provider) and cleanly use only the modem in the terminal box and my personal main router.

I opened the communication terminal box near the front door, removed the ISP router, and tried indiscriminately plugging the wall LAN cables directly into the patch panel inside the terminal box. But no matter how I connected them, the signal wouldn't go to each room. It turned out that the patch panel was not a **'switch hub'** that distributes signals internally, but merely a **simple connection block**.

Ultimately, a switch hub was needed inside the terminal box, and unfortunately, I didn't have one on hand. I had to change the **ISP router (which I was going to remove) to 'Hub (Bridge) Mode'** and stick it back into the terminal box to use as a substitute for a switch hub. (The structure is: Modem ➡ Living room main router ➡ Wall port ➡ back to terminal box ISP router (Hub Mode) ➡ distributed to each room.)

## 2. Diving in Without a LAN Tester (The Ups and Downs)

The biggest obstacle was finding the LAN cable heading to each room.
To make matters worse, I didn't even have a **LAN tester** that beeps to let you know if a line is properly connected. All I had was my two legs and a single laptop.

The method was primitive.
1. Plug the laptop into the LAN port on the living room wall.
2. Walk (run) to the front door terminal box and try plugging in one cable.
3. Come back to the living room and check if the `ping` on the laptop terminal goes through.
4. If it doesn't work, go back to the front door and switch to another cable.

I repeated this process infinitely until I found every LAN port in the house. In the middle of summer, I went back and forth between the living room and the front door dozens of times, sweating profusely.

### 💡 The Betrayal of Living Room 2
Fortunately, in modern new apartments, the terminal box has labels like 'Living Room 1' and 'Living Room 2'.
After safely finding Living Room 1, I plugged in **'Living Room 2 (Gray/Blue wire)'** at the terminal box to revive the LAN port under the dining table. Then I ran under the dining table to do a ping test, but no matter how much I swapped the gray and blue wires, it wouldn't connect.

It turned out that the LAN port under the dining table, which I firmly believed to be 'Living Room 2', was actually the line going into **'Kitchen 1, 2'**. The real 'Living Room 2' port was on the opposite wall where the sofa is placed. Only when I found the wire labeled 'Kitchen' in the terminal box and plugged it into the hub did the internet miraculously work under the dining table.

## 3. Installing Mesh Nodes (Sub Routers) in Each Room

After dozens of round trips and trial and error, I correctly found all the cables going to each room, and to ensure there were no dead zones, I hardwired sub routers (Mesh nodes) in the rooms.

## Results and Review

After completing the Wired Mesh configuration, I walked all around the house holding my smartphone.
Even as I move from room to room, the Wi-Fi smoothly switches (roams) to the nearest router on its own, and there are absolutely no disconnections or speed drops. All the smart home devices are also stably connected without ever dropping offline. It was definitely worth the physical effort without a LAN tester. If you have active LAN ports in your home, I highly recommend building a **Wired Mesh** rather than wireless!
