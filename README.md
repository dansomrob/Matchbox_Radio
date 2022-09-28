# Matchbox Radio

After stupidy running the 'sudo apt purge python3' command, my rpi broke and had to be factory reset. Unfortunately all rescources on this project were not saved to GitHub. So I'm having to restart this project from scratch.

## Transistors

To first understand how an radio works, we need to understand how a transistor (BJT)  acts as an amplifier.

Specifically we look at common emitter transistors, as well as biasing transistors.

We also explore some important transistor circuits, such as current mirrors and darlington pairs.

## Operational  Amplifiers 

The file 'opamps.md' contains some notes on operational amplifiers, and some basic experiments.

## Loop-Stick Antenna

For the reciever I am going to use a loop-stick antenna. This consists of a ferrite rod with copper wire wrappped around it. This is then connected to a variable capacitor.

The inductor picks up any changes in the electric field and induced a voltage, according to Faraday's law. The combined LC circuit can be tuned by the capacitor to determine the oscillating frequency.

## AM Modulation

The radio signal we'll recieve will be amplitude modulated. For simplicity we'll ignore frequency modulation (FM).

## Signal Regeneration

After detection, we must process our signal to return the orginal signal waveform. 

## External Rescources

Berkeley has a course, EE105, which contains brilliant lab scripts 

The website [https://petervis.com/Radios/ta7642/7642.html](https://petervis.com/Radios/ta7642/ta7642.ytml) (working link as of 27/09/22) has a brilliant write upof making a simple AM radio with the TA7642 IC chip.
