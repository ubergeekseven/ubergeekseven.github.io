---
date: 2014-12-20
header:
  teaser: /img/imgplaceholder
  overlay_image: /img/imgplaceholder
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
Yesterday I rewrote the HID descriptors to allow for only buttons. the bits
used are 0x01-0x20 and windows loads the driver fine. But for some reason the
buttons do not respond at all, and I cant figure that out at all. It must be
something with the bit shifting in the program. But then again, maybe not.

As a work around so that I can actually move forward on my projects, I am
using a Moga bluetooth controller that I tore apart and soldered the
connections to. This is not what I want to do because of the multitude of
controller ideas I have. I want to make a golf controller using the WII camera
and some IR LEDs for positional tracking, which then leads to the idea that I
can use the same setup for mobile positioning. This would work around the need
for a more accurate IMU in the phone and can give you the ability to move
within a limited field. Then again if you could attach the LEDs in some way
that one is always centered, then you could lean forward and side to side with
the same result.

But if I want this to work, I will have to figure out the descriptor problems
and get this working in mobile. The WII remote can sense 4 IR blobs in x,y,z
and it gives serial data for the position of x,y and then a size for the z.
Therefore z would give distance relative to the blob.

I am going to keep at it, but for now, I need to get at least one game
completed.

