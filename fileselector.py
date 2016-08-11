
#Graham Jordan Prog with parts by Caspar Lant
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime
import os
    #naming conventions
Dict = {'y':1,'Y':1,'n':0,'N':0,'':0,'g':1,'G':1,'l':0,'L':0, 'c':2, 'C':2, 'R':3, 'r':3}
color = {1:'red',2:'green',3:'blue',4:'orange'}
evens = {'1':1,'2':1,'3':2,'4':2}
Local = raw_input('Graham\'s Computer or Lab, Caspar\'s, or relative path: G/L/C/R? ')
ResTitle = {1:'Log of Resistance (ln[ohms])',0:'Resistance (Ohms)'}
if Local == 'g' or Local == 'G':
    Location = 'C:\\Users\\Graham\\OneDrive\\LabData\\KentLab\\data'
elif Local == 'l' or Local == 'L':
    Location = 'C:\\Users\\KentLab\\Desktop\\caspar\\data'
elif Local == 'c' or Local == 'C':
    Location = './data'
else:
    Location = Local
sample = 1
while sample == 1:
    title = 'Magnetoresistance in F5 Nanopillar Sample '
    cont = 1
    DyeX = raw_input('X coordinate of sample ')
    DyeY = raw_input('Y coordinate of sample ')
    Current = raw_input('Current through sample (mA) ')
    while cont == 1:
        print('enter: 1 for single graph, 2 for two comparative trial graphs, 3 for range of trials ')
        print('4 for separated single graph, 5 for Quad Split')
        compare = int(raw_input('Which option listed above? ')) #compare is the variable used to determine the process for the data
        if compare == 5:
                philter = Dict[raw_input('Apply filter, Y/N? ')]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #option 1: Single Graph Print
        if compare == 1:
                #Data Grab
            j = raw_input('trial # ')
            field, resistance = np.loadtxt((Location+'/Sample_F5_'+DyeX+'_'+DyeY+'_'+Current+'mA_trial'+j), skiprows=0 , unpack=True, delimiter='\t')
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
            plt.ylabel('Resistance (Ohms)');
            plt.xlabel('Magnetic Field Strength (Tesla)');
            plt.title((title+DyeX+' by '+DyeY+', Trial '+str(j)+', '+str(Current)+'mA'))
            plt.show ()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #option 2: Comparative Graph Print For 2 Trials
        elif compare == 2 :
                    #data grab
            j = int(raw_input('first trial # '))
            a = int(raw_input('second trial # '))
            field, resistance = np.loadtxt((Location+'/Sample_F5_'+DyeX+'_'+DyeY+'_'+Current+'mA_trial'+str(j)), skiprows=0 , unpack=True, delimiter='\t')
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
            plt.ylabel('Resistance (Ohms)')
            plt.xlabel('Magnetic Field Strength (Tesla)')
            plt.title((title+DyeX+' by '+DyeY+', Trial '+str(j)+', '+str(Current)+'mA'))

            field, resistance = np.loadtxt((Location+'/Sample_F5_'+DyeX+'_'+DyeY+'_'+Current+'mA_trial'+str(a)), skiprows=0 , unpack=True, delimiter='\t');
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
            plt.ylabel('Resistance (Ohms)');
            plt.xlabel('Magnetic Field Strength (Tesla)');
            plt.title((title+DyeX+' by '+DyeY+', Trial '+str(a)+', '+str(Current)+'mA'))
            plt.show ()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #option 3: Print Range of Trials (from _ to _)
        elif compare == 3:
            j = int(raw_input('starting trial #'))
            first = j
            last = int(raw_input('Last Trial #'))

            while j <= last:

                # Data grab
                Trial = str(j);
                field, resistance = np.loadtxt((Location+'/Sample_F5_'+DyeX+'_'+DyeY+'_'+Current+'mA_trial'+str(j)), skiprows=0 , unpack=True, delimiter='	 ');
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
                    fig = plt.plot(field[i], (resistance[i] + math.fabs(float(i)/75000.00)), '.', color = co)
                    i = i+1

                    #Plot titles
                plt.ylabel('Resistance (Ohms)');
                plt.xlabel('Magnetic Field Strength (Tesla)');
                plt.title((title+DyeX+' by '+DyeY+', Trial '+str(j)+', '+str(Current)+'mA'));
                j = j+1

            plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #option 4: Separate Plot into Increasing Field and Decreasing Field
        elif compare == 4 or 5:
                #Data Grab
                j = raw_input('trial # ')
                field, resistance = np.loadtxt((Location+'/Sample_F5_'+DyeX+'_'+DyeY+'_'+Current+'mA_trial'+j), skiprows=0 , unpack=True, delimiter='\t')
                i = 0
                UpField = []
                DownField = []
                UpRes = []
                DownRes = []
                while (i < len(field)-1):
                    #Seperator and filter (written by Graham)
                    sig = np.std(resistance[(i-10):(i+10)])
                    if philter == 1 and float(Current) < 1 and (abs(resistance[i]-resistance[i+1]) > (0.5*sig)):#Due to the lower currents having variable data points (i.e. more noise) a stricter filter is applied of half a standard deviation
                        i=i+1
                    elif philter == 1 and float(Current) < 1 and (abs(resistance[i]-resistance[i-1]) > (0.5*sig)):#Due to the lower currents having variable data points (i.e. more noise) a stricter filter is applied of half a standard deviation
                        i=i+1
                    elif philter == 1 and (abs(resistance[i]-resistance[i+1]) > (sig)): #should exclude any data point that is of a distance larger than standard deviation from the next point
                        i=i+1
                    elif philter == 1 and (abs(resistance[i]-resistance[i-1]) > (sig)): #should exclude any data point that is of a distance larger than standard deviation from the next point
                        i=i+1
                    elif (field[i] < field[i+1] ): # While the magnetic field is increasing the prog will place the values in the separate arrays
                        UpField.extend([field[i]])
                        UpRes.extend([resistance[i]])
                        i = i + 1
                    else : #Will place all remaining data points (the decreasing mag field side) in a separate array
                        DownField.extend([field[i]])
                        DownRes.extend([resistance[i]])
                        i = i +1
                        #Plots and plot titles
                if compare == 4:
                    plt.subplot(2,1,1)
                    plt.plot(UpField, UpRes, '.', color='red')
                    plt.ylabel( 'Resistance (Ohms) ')
                    plt.xlabel( 'Magnetic Field Strength (Tesla) ')
                    plt.title((title+DyeX+' by '+DyeY+', Trial '+str(j)+', '+str(Current)+'mA increasing field'))
                    plt.subplot(2,1,2)
                    plt.plot(DownField, DownRes, '.', color='blue')
                    plt.ylabel( 'Resistance (Ohms) ')
                    plt.xlabel( 'Magnetic Field Strength (Tesla) ')
                    plt.title((title+DyeX+' by '+DyeY+', Trial '+str(j)+', '+str(Current)+'mA decreasing field'))
                    plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Option 5: Splits data into 4 quadrants as listed below
        elif compare == 5:
                zs = max(UpRes)
                s = UpRes.index(s)
                Quad1 = [] #increasing field part 1
                Res1 = []
                Quad2 = [] #increasing field part 2
                Res2 = []
                Quad3 = [] #decreasing field part 1
                Res3 = []
                Quad4 = [] #decreasing field part 2
                Res4 = []
                #divides the increasing magnetic field plot into increasing resistance and decreasing resist
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
                    Quad4.extend([DownField[i]])
                    Res4.extend([DownRes[i]])
                    i = i + 1
                while (i < len(DownRes)-1):
                    Quad3.extend([DownField[i]])
                    Res3.extend([DownRes[i]])
                    i = i +1
                a = 1
                STOP = 1
                    #Horizontal filter (under construction)
                while a<= 4:
                    i=0
                    X,Y = 0,0
                    X,Y = [],[]
                    while i < (len(eval('Quad'+str(a)))-1):
                        sig = np.std(resistance)
                        if abs(eval('Quad'+str(a))[i]-eval('Quad'+str(a))[i+1]) > (0.5*sig) and philter == 1 and STOP == 0:
                            i = i+1
                        elif abs(eval('Quad'+str(a))[i]-eval('Quad'+str(a))[i-1]) > (0.5*sig) and philter == 1 and STOP == 0:
                            i = i+1
                        else:
                            X.append(eval('Quad'+str(a))[i])
                            Y.append(eval('Res'+str(a))[i])
                            i = i+1
                    if a ==1:
                        Quad1 = np.array(X)
                        Res1 = np.array(Y)
                    elif a ==2:
                        Quad2 = np.array(X)
                        Res2 = np.array(Y)
                    elif a ==3:
                        Quad3 = np.array(X)
                        Res3 = np.array(Y)
                    elif a ==4:
                        Quad4 = np.array(X)
                        Res4 = np.array(Y)
                    a = a+1
                a = 1
                x = []
                y = []
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #Fitter (under construction-Linear works)
                Fit = Dict[raw_input('do a fit of the data, Y/N? ')]
                if Fit == 1:
                    Log = Dict[raw_input('Logrithmic Fit, Y/N? (default is Linear) ')]
                    if Log == 1:
                        Res1 = np.log(Res1)
                        Res2 = np.log(Res2)
                        Res3 = np.log(Res3)
                        Res4 = np.log(Res4)
                    def LineFit(x, y):
                #Returns slope and y-intercept of linear fit to (x,y) data set
                        xavg = x.mean()
                        B = (y*(x-xavg)).sum()/(x*(x-xavg)).sum() # slope
                        A = y.mean()-B*xavg    # intercept
                        return B, A
                    while a <= 4:
                        x = eval('Quad'+str(a))
                        y = eval('Res'+str(a))
                        B,A = LineFit(x,y)
                        firstx = x[0]
                        lastx = x[-1]
                        step = 0.001
                        if firstx > lastx:
                            xfit = np.arange(lastx,firstx,step)
                        else:
                            xfit = np.arange(firstx,lastx,step)
                        yfit = A + B*xfit
                        Loc = evens[str(a)]
                        plt.subplot(2,1,Loc)
                        plt.plot(xfit,yfit,'b-',color = color[a], label=('Lineit '+str(a)+' Y = '+str(B)+'X + '+str(A)))
                        plt.plot(x,y, '.', color = color[a])
                        a = a+1
                        plt.legend()

                plt.subplot(2,1,1)
                plt.plot(Quad1,Res1, '.', color = 'red', label='increasing resistance')
                plt.ylabel(ResTitle[Log]);
                plt.xlabel('Magnetic Field Strength (Tesla)');
                plt.title((title+DyeX+' by '+DyeY+', Trial '+str(j)+', '+str(Current)+'mA increasing field'));
                plt.plot(Quad2,Res2, '.', color = 'green', label='decreasing resistance')
                plt.legend()
                plt.subplot(2,1,2)
                plt.plot(Quad3,Res3, '.', color = 'blue', label='decreasing resistance')
                plt.ylabel(ResTitle[Log]);
                plt.xlabel('Magnetic Field Strength (Tesla)');
                plt.title((title+DyeX+' by '+DyeY+', Trial '+str(j)+', '+str(Current)+'mA decreasing field'));
                plt.plot(Quad4,Res4, '.', color = 'orange', label='increasing resistance')
                plt.legend()
                plt.show()
        cont = Dict[raw_input('Continue with this sample, Y/N? ')]
    sample = Dict[raw_input("Change sample, Y/N?")]
    print('Good bye')
