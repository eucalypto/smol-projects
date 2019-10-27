# Training repetition logger

This logger waits for you to input the number of repetitions you just did.
It then logs them for you with the current timestamp.

## Why?

I wrote this logger because I like to spread out my sets over a long time.
But then I want to log not only the number of reps but also the timestamp 
of the set. And this is the perfect job for a computer! ^-^

## Extensions

Here are some extension ideas:


### Amend last entry

Sometimes I mistype the number and want to amend the last entry.


### Class structure

Right now, it is one script. But if I want to make further extensions, I should split up the logic from the display (current: command line). This would allow me to set up a gui later without much hustle.

### Gui

Having a gui would be nice. I could offer a number-pad that allows me to insert the rep-number with mouse.

I also could offer the last used rep-numbers for quick selection.

### File logging

Right now, the program just displays the log in the command line. For now, this is enough for me. But later, I maybe want to let it save to a file as well.

### Starting repetitions

Sometimes you start the logger after you started the workout. You should be able to give the reps you already did as a starting point.

### Multiple exercises

Right now, the program assumes you do only one kind of exercise. You have to start this script multiple times to log more than one exercise.

### Done

#### Graceful input validation

Right now, the program tries to cast the input to int. When this fails it raises a ValueError, terminating the whole program.

I want it to ask me again for input if this fails.

#### Assume last number as input

Often I do the same amount of reps. The program should assume the last given amount as input if you hit "enter" without giving a number (input).
