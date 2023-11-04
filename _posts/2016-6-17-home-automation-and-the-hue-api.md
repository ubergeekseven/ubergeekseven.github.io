\--- layout: post title: Home Automation and the Hue API and Problem with the
Dimmer Remotes categories: [] tags: \- HUE \- HUE API \- Home Automation \-
REST status: publish type: post published: true meta: _thumbnail_id: '33' \---

I have been using Openhab for over two years now and most of the time I have
used the Hue bridge and lights to connect Zigbee devices to my network. I only
used the apps, which are terrible, to add lights and bring them in to groups.
I recently started to look in to the API after getting a [Hue Dimmer
Switch](http://www2.meethue.com/en-us/productdetail/philips-hue-dimmer-switch)
and being underwhelmed with the capabilities that the default setup allows.

The best thing about the Hue setup is that you get access to a good API. One
that the programmers working for Philips have not taken advantage of in the
apps fully. For one thing, in the app, you cannot add more than two groups to
the switch. So if you have 3 or more groupings of lights within a room, you
have to combine those in to 2 groups. Even Then you can only turn them on, dim
turn off or set the groups to previously set up scenes. At first I thought I
could trick the app in to simulating turning the groups on and off in
different orders based on clicks by choosing a picture with black as the only
color. No good, it dims to the lowest setting only.

If you use the API though, you can do almost any combination of things that
you can think of. As of now, I do not have everything figured out, but I can
trigger several groups in predetermined orders by using click counts and long
and short clicks. I am still trying to fully understand the API, it uses a
REST interface so JSON is the format that you will use to set up, read and
communicate between devices in the network.

This opens up many options that Philips left out of their app. It also allows
you to create virtual sensors or "Clip sensors" that can exist in the network.
This means that you can create a virtual sensor that can hold counts, trigger
actions based on counts, or be end nodes that connect to the Hue bridge via
Ethernet. This could be an arduino, esp8266, Raspberry pi or any other network
device that you can send and receive data through CURL or REST whatever exists
that can send the JSON formatted information to the bridge.

One thing to note about the remotes, they seem to be touchy with connectivity.
Not once they are on the network, but trying to connect them can be a hassle
and if you send a command to program the switch using a rule that replaces an
already existing rule without dealing with the variables that the default
rules use, you may erase all of the rules currently stored and the remotes
will do random things. I recently sent a command to the rules section without
stating the actual rule that I wanted to update and two of my remotes stopped
working. They would not even report to the hub any longer. The only way to get
them back on the network was to do a time wasting reset and reprogramming.
Here is how I did that:

Hue Dimmer Switch reset if you cannot connect them,

1) Make sure you have the 2nd gen version of the app

2)Delete the remote from the app. This will remove any rules you have set up
before. You can use the api to get the setup before deleting to make setup a
little faster later on.

3) Reset the switch by flipping the remote over and pressing the reset switch
for around 10 seconds. The light will flash green, let go of the button and
the light will flash between green red and orange and then will flash orange.
Your remote is "ready" to connect again.

4) Open the app and go to Setting-->Switch Setup-->(+) to add a remote. Then,
since your remote has been reset, you can add it as a remote that has never
been used before. Even if the remote came with a lamp, it is now no longer
paired with that lamp. As long as the light is still flashing orange, click
the orange light is flashing button.

5) Your remote will most likely flash the green light within a few seconds.
The app will most likely not report that it is communicating with the remote.
backing out to the switch configuration section will not show the remote. This
is annoying, but, just let the app sit in the background for several minutes.
It says up to 3 minutes, but I have had to wait upwards of 20 minutes before
it actually showed in the app. It has worked several times doing this exact
method.

I read on a forum that someone had the same issue and they recommended a
similar approach, except they said to press the reset button until fully
reset, then wait until the orange light stopped flashing and then push the
reset button for 1 second to start the pairing process again. This did not
work for me. But if the above does not work for you, maybe this will. But I
think that the bridge may be adding all of the default rules and updating the
remote in the background without notifying the user of the connection status.
terrible design, but at least they can improve it in the future.

Once I finish programming my remotes to do what I want, I will post the steps
I went through to get the actions I have working.

