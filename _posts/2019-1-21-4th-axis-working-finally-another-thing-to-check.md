\--- layout: post title: 4th Axis Working... Finally! Another thing to check
categories: [] tags: \- CNCRouterparts \- 4th \- 4th axis \- mach 3 \- mach 3
rotary \- mach 3 rotary very slow \- slow rotary \- a axis rotates slow \-
vectric \- fusion status: publish type: post published: true meta:
_thumbnail_id: '67' \---

I have been messing with the 4th axis for half of the day today. I finally got
the nerve to test it doing a simple toolpath to create a dowel of a certain
diameter. When I ran it, the axis moved incredibly slow. Looking into this
more in old mach 3 forums, I finally found a post that pointed to the right
answer.

When exporting your toolpath, mach will see the feedrate as inches per minute.
even though you set up the motor tuning and axis in the config, there is 1
more setting to get mach to output in degrees per correctly. Then, another
setting to use in the .62 version that should be used with CNCROUTERPARTS
machines. They recommend it, at least.

Open Config - - Toolpath

Make sure that “A-Rotations Enabled” and “Use Radius for Feedrate” are both
checked.

In the settings dialog, enter 0.0001 as the rotation radius. Or enter your
actual stock radius. Not sure if the bug was fixed, for this in the version I
use. I have not checked if the actual radius produces the same result.

![RotarySettings.PNG](/img/RotarySettings.PNG)

Now you should be able to run your rotary axis at an actual working pace. Such
a clunky bit of software and the forums are getting dated and hard to search.
Maybe this post will show and help someone in the same boat.

