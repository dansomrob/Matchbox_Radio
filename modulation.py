import numpy as np
import matplotlib.pyplot as plt

# This code plots a graph of: the carrier waveform, the message waveform, and the AM waveform.

A_c = 5 #Amplitude of the carrier waveform
A_m = 2.5 #Amplitude of message waveform
omega_m = 0.01 #Angular frequency for message waveform
omega_c = 0.1 #Angular frequency for carrier waveform

inputs = np.linspace(0,1000,1000) #The inputs, over the time domain

#These for loops calculate the the carrier, message, and signal waveforms.
#For the mathematics, see the wikipedia page (https://en.wikipedia.org/wiki/Amplitude_modulation).

for carrier in inputs:
    carrier = A_c * np.cos(omega_c * inputs)

for message in inputs:
    message = A_m * np.cos(omega_m* inputs)

for signal in zip(message, carrier):
    signal = A_c*(1+(A_m/A_c)*np.cos(omega_m*inputs))*np.cos(omega_c*inputs)

#Plotting code

fig, axs = plt.subplots(3,sharex=True,sharey=True)
fig.suptitle("Amplitude Modulation")

axs[0].set_title("Carrier Wave",fontsize=10)
axs[0].plot(inputs,carrier,'b')

axs[1].set_title("Message Wave",fontsize=10)
axs[1].plot(inputs,message,'g')

axs[2].set_title("Modulated Wave",fontsize=10)
axs[2].plot(inputs,signal,'r')

plt.savefig("modulation1.png",dpi=300)
plt.show()
plt.close()

#Now we plot on a single graph, with the shape of the modulated signal controlled by the message waveform

plt.figure()

plt.plot(inputs,carrier,'b',alpha=0.4,label="Carrier")
plt.plot(inputs,message+A_c,'g--',alpha=0.4,label="Message Waveform")
plt.plot(inputs,-message-A_c,'g--',alpha=0.4)
plt.plot(inputs,signal,'r',label="Modulated Wave")

plt.legend(loc='upper right')
plt.title("Amplitude Modulation")

plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.savefig("modulation2.png",dpi=300)
plt.show()
plt.close()