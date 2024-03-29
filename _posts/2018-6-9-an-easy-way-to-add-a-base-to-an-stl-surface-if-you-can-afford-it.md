---
date: 2018-06-09
header:
  teaser: /img/imgplaceholder
  overlay_image: /img/imgplaceholder
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
TLDR; import STL surface into Vectric Aspire, export as STL and import to the
program you want.

I purchased some assets from Etsy for cnc carving without having to produce
them myself. Turns out that most of these files are just the surface and then
require a decent amount of work to get imported correctly into other software
to machine.

I spent too long attempting to create a base for some of these files. The
biggest problem was the size of the mesh itself. One was over 10 million
triangles. So every change and update took too long to deal with. Then,
selecting the edges to actually join the surface to a base was impossible. I
tried all kinds of tricks to get this fixed without any good output.

The first thing I tried was to import to Aspire and then scale the file to the
size I actually wanted. The way that Aspire handles 3D objects is a little
weird. I would compare it to Minecraft. It seems that the topology is turned
into what they call pixels. These pixels look fine at the original size, but
when scaling the file down to a smaller size, the pixels do not scale with it.
Instead, you get a chunky looking Minecraft version of your file. The thing
that I noticed was that when imported, it automatically adds volume to the
surface. Something that I have not seen on any other software yet. Everything
else tends to take an hour of work and then you may get a file that works for
you.

Import to Aspire and then export to STL. Then, import that file into 3D
builder in windows 10. Most liekly your file will not be manifold, or will
have errors that no other software tells you except it will fail to do any
sort of reduction when you attempt to reduce surface faces. After it repairs
within 3D Builder, you can scale or change anything you want inside of the
software before exporting again to a new OBJ or STL. Then import into your CAD
package, I use Fusion 360, in Fusion I import a new mesh. Next I create a base
feature and then convert it to a solid. Then I had the file that could be used
anywhere for anything easily. All you need is a $2000 program to do this. I
bet that if Vectric published this tool, and this tool alone for $25, they
would sell a ton of licenses to all the people attempting to do a similar
thing. It is very fast and simple.

