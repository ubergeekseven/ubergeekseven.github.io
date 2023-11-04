---
date: 2016-08-04
header:
  teaser: /img/imgplaceholder
  overlay_image: /img/imgplaceholder
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
I have been having many problems with the hue lighting system. About 10-15
lights regularly loose connectivity and show as not communicating. Most of
them will still respond to group controls, but not to individual controls.
Then, the switches themselves will have problems turning on groups of lights
even though the app and the API will trigger them to turn on. It makes no
sense as to why this happens with the group communications.

However, I moved my hub to my basement and now it sits 30 feet away from all
of my networking gear upstairs. This has fixed most of the communication
issues I was having. But, I guess that the setup previously corrupted the
communications with the lamps and now I have to re-add all of the problematic
lights. This is a big hassle and will involve several hours of work to get
back to normal. This could be fixed by the hue bridge recording the address of
the lamps so that it places them back in the original numbering positions. Or
at least allow the end user with the API to rename the number to one that the
user wants. Then I have to reprogram my openhab setup to take control of all
of the new lamps instead of just addressing the numbers I originally set up.
Philips will not implement this, they seem lazy. Their app is terrible and the
API is somewhat limited. Although 3rd party creations have done a much better
job at using the API than Philips themselves. Someone at Philips should be
ashamed of their work.

If you have an issue with you remotes, you can reboot them. I recently
discovered this trick in the developers forum. Philips does not state this in
the app or in the faq. Hold all 4 buttons in until the lights flash. Boom- now
it works better again. Crazy that I spent hours attempting to disconnect and
reconnect the switches. It would randomly connect to the system and usually
hours after I reset and attempted to connect again.

Hopefully philips can get their act together, since somehow people who do not
even get paid to do the work can figure out better ways of interacting with
that system than the creators themselves. The only saving grace is the price
of their lamps. $15 is a great deal, but maybe not if you have to spend 6
hours a month fixing the problems.

