import sys
import numpy as np
import matplotlib.pyplot as plt

# load csv file
DATA = "data/17,0_trial1";
field, resistance = np.loadtxt(DATA, skiprows=0 , unpack=True, delimiter='	');

# plot temperature vs. pressure + error bars
plt.ylabel("Resistance (Ohms)");
plt.xlabel("Magnetic Field Strength (Tesla)");
plt.title("Magnetoresistance in F5 Nanopillar");
plt.plot(field, resistance, 'o', color = 'purple')

plt.show();
