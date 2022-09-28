# Modulation

For this project we're only going to look at AM (amplitude modulation). Therefore the frequency of our incoming signal will be constant. This makes the circuit simplier. 

## AM Modulation

AM modulation works by taking a carrier wave, oscillating at a constant known frequency, and thenmodulating it with a message wave.

If we assume our carrier wave has the form $c(t)=A_C\cos{\omega_Ct}$ and that our message wave has the form $m(t)=A_M\cos{\phi_Mt+\phi}$.

We can use the theory of fourier decomposition to show that a message wave of any form could be written as a sum of cosines (but with a phase I've chosen to ignore).

The modulated wave would have the form

$$y(t)= (1+\frac{m(t)}{A_C})c(t)$$.

We can plot this (code in [modulation.py](./modulation.py)) which gives

![modulation1.png](./modulation1.png)

If we plot these on the same graph, we can see that the modulated wave has the same frequency as the carrier wave but that its amplitude varies based on the shape of the message wave.

![modulation2.png](./modulation2.png)

### Double Sideband

The original form of AM is called *double-sideband amplitude modulation*.

We note that $\cos{\theta}\cos{\phi}=\frac{1}{2}\bigl(\cos{(\theta-\thi)}+cos{(\theta+\phi)}\bigl)$, which gives

$$y(t)=A_C\cos{(\omega_Ct)}+\frac{1}{2}A_M\bigl(\cos{(\theta-\thi)}+cos{(\theta+\phi)}\bigl)$$

## De-Modulation

### Envelope Detection

If we take our electric signal, and run it through a diode, we can select for only the positive voltages.
