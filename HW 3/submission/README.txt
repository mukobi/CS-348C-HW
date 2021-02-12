Gabriel Mukobi
CS 348C HW 3

# About

I aimed to recreate one of the VFX shots from a Corridor Digital video (https://youtu.be/Gmyyvme7Fu8).
The premise is that Sam, the main character, has a Lego Midas touch where everything he touches turns into Legos, and
this causes some issues when he high-fives his friend.

# Notes

The two main parts of building this were 1) creating the Lego pieces in the shape of the default human and 2) turning
all the Lego pieces into a Bullet sim.

To make the lego guy, I used the GridPoints node which is like scatter but along a grid, and I specified a min and max
iso level so that it's actually a hollow shell of legos at the edge of the person's "volume." The bricks are just boxes
scaled to the correct dimensions of Legos. I tried having proxy boxes and adding nubs to make hi-poly bricks that looked
more like Legos, but it kept messing up my bullet sim for some reason (the nubs were popping of the bricks and the thing
was exploding), so I gave up on trying to do my own custom render and proxy geo.

I also procedurally made my own constraint geometry out of the Lego guy. I used Connect Adjacent Pieces to create polylines
representing the connections from each brick to some of its neighbors, I randomly deleted some of these to it would break
easier, and I also used the Cluster node and some wrangling to define clusters of bricks so I could have a scalar attribute
to make the rbd glue stronger within each cluster and really weak at the borders of each cluster.

To do the sim, the big challenge was figuring out how to set up my own SOP Bullet Solver but with my own custom pieces.
Most all the tutorials or examples of the new SOP RBD tools show the Bullet Solver in conjunction with RBD Material Fracture
which takes care of splitting your geo, making constraints, and setting all the correct attributes, but I didn't want
voronoi fractures, I wanted to use the bricks that I had already set up as fracture pieces. I ended up jumping into
the RBD Material Fracture HDA a few times to see what it was actually doing so that I could set the same things on my own
constraints and pieces.

In terms of art directing the destruction, there were two big hurdles. First was making the guy fall over (like the source
video), as he's actually quite stable with decently glued constraints. I first tried guided geometry, but I must have
guided it too strongly as I didn't like the unnatural looking motion. Then, I tried wind, but I had to have way too much
wind to get him to fall and all the pieces blew away after. So I settled on adding in a hidden pusher cube as collision
geometry that nudges him from behind the chest. The second hurdle was getting good chunking with my custom Lego pieces.
It was easy to either get him to shatter into all the individual pieces or stay together, but I was only able to get
decent chunks to form by doing the aformentioned deleting, clustering, and wrangling on the constraints to give them
some low-frequency variance in glue strength.