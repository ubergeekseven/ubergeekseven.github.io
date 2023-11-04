---
date: 2015-01-11
header:
  teaser: /img/imgplaceholder
  overlay_image: /img/imgplaceholder
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
While listening to embedded, a podcast on embedded development, the
interviewee described how he was capable of sensing the pulses emitted from
the common water meter. He did a project for the recent hackaday space prize,
and got to the top 50 contestants.

The water meter uses a magnetic coupling between the flow blades and the
geared counter within the meter. To avoid making any changes to the meter, he
had to find a way to measure the magnetic field. This is where the idea
becomes interesting, using a magnetometer . Since a magnetometer is capable of
sensing magnetic north, it should be capable of sensing other magnetic fields.
Sitting the magnetometer near the housing picks up the spinning magnetic field
and translates in to a pulse. Although he said he had to hack it a bit to get
the results and that a different setup would give better results, the proof
was there.

This have me an idea for a measurement device. While researching optical
encoders to find a way to measure small distances accurately, I was
disheartened to see that the smallest collection slit available is .5mm and
costs more than it is worth. I didn't spend too much time looking, so they
could produce smaller ones. But I'm looking for a micrometer level measurement
device.

I don't have time to do this now, but i will eventually get to this one.
Attach a magnet or magnets to a shaft, spaced equally, and then use gearing to
spin the shaft several times per mm. Then use the magnetometer to sense the
field. I'm not sure, but if it is sensitive enough, a on off touch doesn't
need to be the measurement. Potentially, if the magnets are calibrated to the
same magnetic output, you may be able to achieve smaller increments by sensing
the edges as well as the apex of the field.

Add this to the end of a digital caliper to roll along distances and then
output as a keyboard. Possibly adding multiple buttons to label measurements
and submit the text. Or use it as an accumulative measurement device. Roll,
press save, roll press save, roll press save and send as output.

I had to put this thought out there, as a reminder to myself on the future.

