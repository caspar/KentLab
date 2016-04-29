import sys
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime
import os

# load csv file
PATH = "./data/"
FILENAME = "Sample_F5_21_2_1mA_trial2";
TIMESTAMP = datetime.now().strftime('%D_%H:%M')
OUTPUT = ''+ os.path.splitext(FILENAME)[0] + '_' + TIMESTAMP + '.png'
field, resistance = np.loadtxt((PATH+FILENAME), skiprows=0 , unpack=True, delimiter='	');

print(OUTPUT)

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
    fig = plt.plot(field[i], (resistance[i] + math.fabs(float(i)/75000.00)), '.', color = color)
    i = i+1

def color():
    global i
    if i%3 == 0:
        i = i + 1
        print(i)
        return 'red'
    else:
        i = i + 1
        return 'blue'


# plot temperature vs. pressure + error bars
plt.ylabel("Resistance (Ohms)");
plt.xlabel("Magnetic Field Strength (Tesla)");
plt.title("Magnetoresistance in F5 Nanopillar");

plt.show();

plt.savefig((OUTPUT), dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

plt.close(fig)
