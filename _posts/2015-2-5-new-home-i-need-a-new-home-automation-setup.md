---
date: 2015-02-05
header:
  teaser: /img/imgplaceholder
  overlay_image: /img/imgplaceholder
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
![upload.png](/img/upload.png)

5-6 year's ago, I attempted to create an all in one home automation system. I
was capable of cobbling together several different half working setups. But
quickly I realized it wasn't as capable as my mind wanted it to be. I spent
months programming a custom website with custom code to send to the different
systems to try to make them work together.

using event ghost on a Windows computer a touch screen computer on another
Windows setup and IP cameras and X10 home automation switches and outlets as
well as a barcode scanner. A usb uart ir transmitter/receiver also. I even
attempted voice control using a Bluetooth speakerphone as a remote control.
And even an android app with touch controls.

All i can say is that i wasted lots of time, I did learn several things about
project planning and interacting between several protocols. But the technology
at the time tried to lock you in to a single manufacturer. And they all pretty
much sucked even when using their setups. X10 in a old house with questionable
wiring schemes is flaky at best. And I eventually stopped using them all
together. This was before tasker became so well improved and at the start of
the IOT discussions.

The barcode scanner was too far away from the fridge and the database was
limited. The Bluetooth voice control was attempted using a combination of
Windows voice service and event ghost. That never worked. And updating code on
a website to add buttons was tedious.

Two years ago i attended ces and saw at least 50 booths of automation devices.
Most using zigbee or zwave and most claiming compatibility with other products
in that sphere. I couldn't wait until those devices came out, and today, they
are here.

![upload.jpeg](/img/upload.jpeg)

This is not to say that they are perfect. But, i now can use several systems
depending on what hardware they offer, together. The bad thing this time
around is the need for a cloud infrastructure to use the protocols. This must
be a way to mine data for consumer behavior, because there is not a need for
the cloud to run these systems. It may be easier for the end user to set up,
but useless when the internet goes down.

This is where [openhab](http://openhab.org) comes in and delivers more than I
have time to do. Openhab, as the name implies, is open source and compatible
with everything out there today and possibly everything out there tomorrow. It
is built on java and can be run almost anywhere. Currently, it's successor is
being developed, and it looks good. Right now, 1.6.2 is out and stable.

I looked in to getting a smart things hub and several others before i saw the
hackaday post on hacking the GE Wink hub. This hack allows local control over
any of the devices connected to the hub, without the wink app or an internet
connection.

I then found the instructable on the uber home automation controller, and his
addition of the wink in to it. This brought me to openhab and raspberry pi
with the wink.the next day i ordered a hub and two dimmable link lights from
home depot for $54 shipped. Way less than any other device and has a great
offering of radios available for future use.

I then found a deal on rfm69hw 918mhz modules and bought 10 of those. I have a
large number of atmel 328p chips and all of the components to build arduinos
when needed. Just had to order the 8mhz crystal and the TI switching regulator
package for 3.3v because my current build uses a 5v version of the package.
Just have to design the board with an array of connectors for sensors and
output options to make an all in one device for each room. Not sure what I'm
adding yet, but I like data.

This board I'm making will first be for through hole components, because i
don't have to purchase them. And 20 boards will cost less than 50$, I can
always design it with surface mount at the same time and order them for future
use. And at this point, the calculations work out to around $20 per node.

I've already set up the wink and successfully created tasker events to trigger
curl over ssh using voice commands. It has lag, but I think using openhab as
an in between might trigger things faster. Not sure yet though.

So far I've thought about several sensors to use.

Temperature and humidity

Light

occupancy

Window and door switches

i would also like to trigger notifications to either be played outloud or
signified by flashing lights or color.

Since some commands and devices are 1 way, with lights, i can use a light
sensor to detect if the light is on. Then send an update to notify me of the
status.

A refrigerator door sensor, oven sensor, laundry sensors through an
accelerometer or maybe a more simplistic method. I could even make a switch of
some sort wherever the laundry baskets sit to notify me of a full basket. This
could be in every bedroom as well, then instead of telling my kids to bring it
to the laundry, they could just get notifications on there devices or out loud
when detected in their room.

A camera system for outside is already a given. And integrating all of this in
one package to offset eventual incompatibilities with manufactured devices is
going to allow me to adapt my setup as new and interesting devices come in to
existence.

As i troubleshoot and learn these systems, i will try and keep a list of links
I used to set this up. I've had several problems already with spread out
answers on forums that i have already gained from. There is not one single
place to go yet to find all of this. Hopefully the notes I keep will allow
someone to eventually set up a similar system with an easy reference to
access.

