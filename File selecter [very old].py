import sys
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime
import os
    #naming conventions
title = "Magnetoresistance in F5 Nanopillar Trial "
print("enter: 1 for single graph, 2 for two comparative trial graphs, 3 for range of trials ")
print("4 for separated single graph, 5 for Quad Split")
compare = int(raw_input("Which option listed above? ")) #compare is the variable used to determine the process for the data
Location = "C:\Users\Graham\OneDrive\KentLab-master\KentLab\data"
DyeX = raw_input("X coordinate of sample ")
DyeY = raw_input("Y coordinate of sample ")
Current = raw_input("Current through sample (mA) ")
title = "Magnetoresistance in F5 Nanopillar Trial "
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #option 1: Single Graph Print
if compare == 1:
        #Data Grab
    j = raw_input("trial # ")
    field, resistance = np.loadtxt((Location+"\Sample_F5_"+DyeX+"_"+DyeY+"_"+Current+"mA_trial"+j+".txt"), skiprows=0 , unpack=True, delimiter='	')
        #separator and plotter (written by Caspar)
    color = []
    array = []
    i = 0
    while (i < len(field) - 1):
        if (float(field[i]) >= float(field[i+1])):
            color = 'blue'
        else:
            color = 'red'
    
        fig = plt.plot(field[i], (resistance[i] + math.fabs(float(i)/75000.00)), '.', color = color)
        i = i+1
        #plot title
    plt.ylabel("Resistance (Ohms)");
    plt.xlabel("Magnetic Field Strength (Tesla)");
    plt.title((title+str(j)))
    plt.show ()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #option 2: Comparative Graph Print For 2 Trials    
elif compare == 2 :
            #data grab
    j = int(raw_input("first trial # "))
    a = int(raw_input("second trial # "))
    field, resistance = np.loadtxt((Location+"\Sample_F5_"+DyeX+"_"+DyeY+"_"+Current+"mA_trial"+str(j)+".txt"), skiprows=0 , unpack=True, delimiter='	')
    plt.subplot(2,1,1)
        #separator and plotter for 1st trial (written by Caspar)
    color = []
    array = []
    i = 0

    while (i < len(field) - 1):
        if (float(field[i]) >= float(field[i+1])):
            color = 'blue'
        else:
            color = 'red'
        fig = plt.plot(field[i], (resistance[i] + math.fabs(float(i)/75000.00)), '.', color = color)
        i = i+1
        #Plot titles
    plt.ylabel("Resistance (Ohms)");
    plt.xlabel("Magnetic Field Strength (Tesla)");
    plt.title((title+str(j)))
    
    field, resistance = np.loadtxt((Location+"\Sample_F5_"+DyeX+"_"+DyeY+"_"+Current+"mA_trial"+str(a)+".txt"), skiprows=0 , unpack=True, delimiter='	')
    plt.subplot(2,1,2)
        #Separator and plotter for 2nd trial (written by Caspar)
    color = []
    array = []
    i = 0

    while (i < len(field) - 1):
        if (float(field[i]) >= float(field[i+1])):
            color = 'blue'
        else:
            color = 'red'
        fig = plt.plot(field[i], (resistance[i] + math.fabs(float(i)/75000.00)), '.', color = color)
        i = i+1
        #Plot titles
    plt.ylabel("Resistance (Ohms)");
    plt.xlabel("Magnetic Field Strength (Tesla)");
    plt.title((title+str(a)))
    plt.show ()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #option 3: Print Range of Trials (from _ to _)
elif compare == 3:
    j = int(raw_input("starting trial #"))
    first = j
    last = int(raw_input("Last Trial #"))

    while j <= last:

        # Data grab
        FileName = "C:\Users\Graham\OneDrive\KentLab-master\KentLab\data\Sample_F5_21_2_1mA_trial"
        Trial = str(j);
        field, resistance = np.loadtxt((FileName+Trial+".txt"), skiprows=0 , unpack=True, delimiter='	');
        PlotNum = 2*(j-first)+1
        PlotH = 2*(last-first)+1
        plt.subplot(PlotH,1,PlotNum)
            #Separator and plotter (writen by Caspar)
        color = []
        array = []
        i = 0

        while (i < len(field) - 1):
            if (float(field[i]) >= float(field[i+1])):
                color = 'blue'
            else:
                color = 'red'
            fig = plt.plot(field[i], (resistance[i] + math.fabs(float(i)/75000.00)), '.', color = color)
            i = i+1

            #Plot titles
        plt.ylabel("Resistance (Ohms)");
        plt.xlabel("Magnetic Field Strength (Tesla)");
        plt.title((title+str(j)));
        j = j+1

    plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #option 4: Separate Plot into Increasinf Field and Decreasing Field
elif compare == 4 or 5:
        #Data Grab
    j = raw_input("trial # ")
    field, resistance = np.loadtxt((Location+"\Sample_F5_"+DyeX+"_"+DyeY+"_"+Current+"mA_trial"+j+".txt"), skiprows=0 , unpack=True, delimiter='	')
    i = 0
    UpField = []
    DownField = []
    UpRes = []
    DownRes = []
        #Seperator (written by Graham)
    while (field[i] < field[i+1] ): # While the magnetic field is increasing the prog will place the values in the separate arrays
        UpField.extend([field[i]])
        UpRes.extend([resistance[i]])
        i = i + 1
    while (i < len(field)-1): #Will place all remaining data points (the decreasing mag field side) in a separate array
        DownField.extend([field[i]]) 
        DownRes.extend([resistance[i]])
        i = i +1
            #Plots and plot titles
    if compare == 4:
        plt.subplot(2,1,1)
        plt.plot(UpField, UpRes, '.', color='red')
        plt.ylabel("Resistance (Ohms)");
        plt.xlabel("Magnetic Field Strength (Tesla)");
        plt.title((title+str(j)+' increasing field'));
        plt.subplot(2,1,2)
        plt.plot(DownField, DownRes, '.', color='blue')
        plt.ylabel("Resistance (Ohms)");
        plt.xlabel("Magnetic Field Strength (Tesla)");
        plt.title((title+str(j)+' decreasing field'));
        plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Option 5: Splits data into 4 quadrants as listed below
    elif compare == 5:
        s = max(UpRes)
        s = UpRes.index(s)
        Quad1 = [] #increasing field part 1
        Res1 = []
        Quad2 = [] #increasing field part 2
        Res2 = []
        Quad3 = [] #decreasing field part 1
        Res3 = []
        Quad4 = [] #decreasing field part 2
        Res4 = []
        #divides the increasing magnetic field plot into increasing resistance and decreasing resistance
        i = 0
        while (i < s ): 
            Quad1.extend([UpField[i]])
            Res1.extend([UpRes[i]])
            i = i + 1
        while (i < len(UpRes)-1): 
            Quad2.extend([UpField[i]])
            Res2.extend([UpRes[i]])
            i = i +1
        g = max(DownRes)
        g = DownRes.index(g)
        #divides decreasing magnetic field into increasing resistance and decreasing resistance
        i = 0
        while (i < g ): 
            Quad3.extend([DownField[i]])
            Res3.extend([DownRes[i]])
            i = i + 1
        while (i < len(DownRes)-1): 
            Quad4.extend([DownField[i]])
            Res4.extend([DownRes[i]])
            i = i +1
        plt.subplot(2,2,1)    
        plt.plot(Quad1,Res1, '.', color = 'red')
        plt.ylabel("Resistance (Ohms)");
        plt.xlabel("Magnetic Field Strength (Tesla)");
        plt.title((title+str(j)+' increasing field increasing resistance'));
        plt.subplot(2,2,2)
        plt.plot(Quad2,Res2, '.', color = 'purple')
        plt.ylabel("Resistance (Ohms)");
        plt.xlabel("Magnetic Field Strength (Tesla)");
        plt.title((title+str(j)+' increasing field decreasing resistance'));
        plt.subplot(2,2,3)
        plt.plot(Quad4,Res4, '.', color = 'blue')
        plt.ylabel("Resistance (Ohms)");
        plt.xlabel("Magnetic Field Strength (Tesla)");
        plt.title((title+str(j)+' decreasing field decreasing resistance'));
        plt.subplot(2,2,4)
        plt.plot(Quad3,Res3, '.', color = 'black')
        plt.ylabel("Resistance (Ohms)");
        plt.xlabel("Magnetic Field Strength (Tesla)");
        plt.title((title+str(j)+' decreasing field increasing resistance'));
        plt.show()
