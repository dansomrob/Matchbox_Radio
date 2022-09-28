import numpy as np
import matplotlib.pyplot as plt

# This code plots a graph of: the carrier waveform, the message waveform, and the AM waveform.

A_c = 3 #Amplitude of the carrier waveform
A_m = 1 #Amplitude of message waveform
omega_m = 1 #Angular frequency for message waveform
omega_c = 5 #Angular frequency for carrier waveform

inputs = np.linspace(0,50,1000) #The inputs, over the time domain

#These for loops calculate the the carrier, message, and signal waveforms.
#For the mathematics, see the wikipedia page (https://en.wikipedia.org/wiki/Amplitude_modulation).

for carrier in inputs:
    carrier = A_c * np.sin(omega_c * inputs)

for message in inputs:
    message = A_m * np.cos(omega_m* inputs) + 1

for signal in zip(message, carrier):
    signal = carrier * (1 + message/A_c)

#Plotting code

plt.figure()

plt.yticks(color='w') #Turn off the numbers for the y axis
plt.ylabel("Relative amplitude")
plt.xlabel("Time")

plt.plot(inputs,carrier,'b',label="Carrier Wave")
plt.plot(inputs,message,'r',label="Message Wave")
plt.plot(inputs,-1*message,'r')
plt.plot(inputs,signal,'g',label="Modulated Signal")

plt.legend(loc='upper right')

plt.show()
#plt.savefig("modulation.png")