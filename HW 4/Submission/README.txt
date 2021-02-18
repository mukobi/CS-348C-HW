I tried to imitate one of the character effects from the 2016 AICP Sponsor Reel - Dir Cut (https://vimeo.com/169599296),
specifically the cable person at 0:33. I'm not super sure how they did it, but I think I took a pretty different
approach to setting up my geometry and sim, and I ended up with something looking more like a bunch of rubber bands.

One notable part was that I tried to give each generated cable a random color out of 3 choices and a random multiplier
on top of its normal rest length to use as a new rest length. This scaled up rest length let some of the cables droop
more than others. I also turn off my pin constraints at the end to make all the cables fall down, and I couldn't find
any way to get that to work through animating or wrangling attributes on the SOP level, so I had to dive into the
Vellum Solver SOP's forces DOP network and add a Vellum Constraint Property DOP to 0 the breaking threshold and bend
constraint force after a certain frame.

For the character, I used the "Breakdance Ending 3" animation with the "Olivia" character from Mixamo.

For the color scheme, I was inspired by https://www.reddit.com/r/cableporn/comments/foq1nm/rainbow_effect/ and used https://coolors.co/f16704-1588e0-14cc00-565656-f4fec1