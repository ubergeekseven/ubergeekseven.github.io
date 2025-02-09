---
date: 2025-02-09
header:
  teaser: "/img/RyujinxDual.png"
  overlay_image: "/img/RyujinxDual.png"
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
---

# Ryujinx, VR Desktop, 3d Depth Setup

I have been playing TOTk on the quest 3 using VR Desktop and Ryujinx for a few weeks. I was playing around with the setup using reshade and a custom LUT setup. Just to make it look darker than the general yellow tint that exists by default. Also some mods to increase the resolution and FPS. 
I saw something called superdepth3d as an option within reshade during installation. This shader setup will create a side by side display of the game and you can control the settings to modify the depth it shows as well as many other things I have not touched. 

I should play with more of the settings to get some things figured out but as of now, the default works well enough for a legit sense of depth added to the game while using a VR headset. 

There are methods of using another application to render to the headset, the 3D setup. Vorpx can do this but I accidentally found out that VR Desktop supports this by default. While connected to your computer, you can set the 3D settings in the main menu bar of VR Desktop to side by side half screen and it will render the view perfectly. Super simple to set up.

install reshade and choose ryujinx as the application to modify. I use the Vulkan choice when doing this setup since ryujinx is using the Vulkan setup as well. Make sure to choose the superdepth3d entry in the reshade installer so that the shader is installed as an option.

When you launch your game in Ryujinx, you can get the VR Desktop keyboard to pop up so that you can hit the Home key. This will show the reshade menu. 

Within that menu, select superdepth3d to turn it on. you will get a split screen. It looks terrible. Then hit home on the keyboard to close the menu. 
![ryujinxSuperDepth.gif](/img/ryujinxSuperDepth.gif)
In the VR Desktop menu bar, choose side by side half. When the game is full screen, it will render as one image with much greater depth. 

Some overlays look odd in the game. This could be due to settings I have not yet touched. Otherwise, when playing, the effect is much more immersive than the standard 2d renderings. 

