# Monty Hall Problem Simulator

This simple program aims to simulate the so-called 'Monty Hall Problem'.  The problem statement is below:

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; 
> behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, 
> opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" 
> Is it to your advantage to switch your choice?

This program makes a random choice from three doors, and, based on whether or not it matches with the 'prize door', 
labels it either a 'staying win' or a 'switching win' if the prize would be won by staying or switching, respectively.

To run this program, first install Python 3 (please don't install Python 2).  Make sure you add Python to your
system's environment variables in the installer (on Windows).

Then, simply open a terminal and type `python .\monty_hall.py {###}` where {###} is the number of times you want to 
run the simulation.
