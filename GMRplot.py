import sys
import numpy as np
import matplotlib.pyplot as plt
import os

# load csv file
PATH = "./data/Sample_F5_21_2_1mA_trial3"
# DATA = "./data/Sample_F5_21_2_1mA_trial2";
field, resistance = np.loadtxt(PATH, skiprows=0 , unpack=True, delimiter='	');

# color stuff
color = []
array = []
i = 0

while (i < len(field) - 1):
    if (float(field[i]) >= float(field[i+1])):
        color = 'blue'
    else:
        color = 'red'
    # array[i] = field[i], resistance[i], color[i]
    # print(math.fabs(float(i)/10000.00))
    fig = plt.plot(field[i], resistance[i], '.', color = color)
    i = i+1


# plot temperature vs. pressure + error bars
plt.ylabel("Resistance (Ohms)");
plt.xlabel("Magnetic Field Strength (Tesla)");
plt.title("Magnetoresistance in F5 Nanopillar");
plt.show();

plt.show();
