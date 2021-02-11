Gabriel Mukobi
CS 348C HW 3

# About

I aimed to recreate one of the VFX shots from a Corridor Digital video (https://youtu.be/Gmyyvme7Fu8).
The premise is that Sam, the main character, has a Lego Midas touch where everything he touches turns into Legos, and
this causes some issues when he high-fives his friend.

# Notes

The two main parts of building this were 1) creating the Lego pieces in the shape of the default human and 2) turning
all the Lego pieces into a bullet sim.

To make the lego guy, I used the GridPoints node which is like scatter but along a grid, and I specified a min and max
iso level so that it's actually a hollow shell of legos at the edge of the person's "volume." 