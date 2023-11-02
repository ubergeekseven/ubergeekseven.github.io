\--- layout: post title: Possible mobile vr positioning system... for any
device? categories: \- vr tags: \- tracking \- vr status: publish type: post
published: true meta: _thumbnail_id: '8' \---

I have recently stated to work with the vuforia sdk for unity. It is for ar,
but it's possible to remove the camera feed used as the background to them use
the markers for loading scene content.

I am able to remove the background, but i think that the processing is still
being done and then just not rendered. So if i can figure out how to force it
to only load the content when the marker is seen, i may be able to reduce the
overhead. Maybe not, but I'm going to try.

Qualcomm also has a beta program for ar headsets, which has a camera for vr. I
have applied for the sdk, and hopefully they accept my application. There is
still the issue of warping when using the vuforia sdk, and I'm working on
using a combination of the cardboard sdk for warping alone and the vuforia sdk
for marker recognition. I have been able to do them individually, but i think
that the cardboard sdk overrides whatever vuforia is doing on the background.
There has to be a way to combine them.

Maybe the new ar sdk will have warping built in, but it's built for pass
through use and may not have it at all.

