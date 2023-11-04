\--- layout: post title: My Christmas Present categories: \- 3dPrinting tags:
\- 3dPrinting status: publish type: post published: true meta: _thumbnail_id:
'6' \---

![upload.jpeg](/img/upload.jpeg)

I have had a 3d printer for over two years now. I started with the MBot cube
which at the time most printers were constructed using laser cut plywood, and
still cost $1000+ to get. I spent a couple months upgrading and configuring
the printer, eventually understanding the simplicity of the device. All in
all, I spent $1500 dollars to get it working consistently.

About a month or so ago, i started having extrusion issues, so i took
everything apart and started to replace the extruder mechanism. I printed an
upgraded spring tension extruder and had a few good prints and then issues
started to occur again. I then commissioned a machine class at my work to
machine aluminum versions of my printed version. After a while of waiting,
which I'm glad that's all it cost, i saw the davinci 1.0 on sale at micro
center. $400 and the build quality out of the box was way better than my
original printer. Someone returned one to the store, so I ended up getting it
for $350. Less than the miter saw I just bought and less than the upgrades to
my previous printer.

I still plan on getting my other printer up again after the parts are ready,
but i thought that at this price i could test it and have time to return it if
i had issues. This original davinci has one extruder, which is totally fine
since 90% of what i do is single color and i try to design with printing in
mind.

The worst part of the davinci, the filament cartridges are stupid expensive.
Good idea, but too much. The board running the printer, like most out there,
is essentially an arduino. And since this is a mass produced printer that has
a low barrier of entry, there is a healthy community working on replacement
firmware.

My printer has the jumpers on the board to reset the ROM to a factory
condition. So I jumped them and flashed [lucs repetier
firmware](https://github.com/luc-github/Repetier-Firmware-0.92). A couple
hours later after dialing in the settings, I now have a $350 printer that runs
on any 3rd party filament.

I then installed a raspberry pi running [octoprint](http://octoprint.org) and
a wireless connection. I now have a wireless printer that can go on any closet
with power. Next step i am going to install a camera for a live feed, i used
the ps2 camera with no luck. So now I'm going to try some other cameras.

I have printed several times with very good results, the auto leveling feature
is really just a measurement of the distance in z that the plates on the
corners register. The firmware does not compensate for the differences, it
just tells you in mm what it is. Pair that with a measurement device, then
just raise and lower the bed so that all are equal and you're ready to go.

If you want to get in to 3d printing, but the cost and reviews of other
printers out there are why you haven't. Find a early generation davinci 1 and
hack it. You'll be happy with what it can do, especially for the cost.

