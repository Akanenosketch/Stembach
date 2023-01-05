from matplotlib import pyplot as plt
import numpy as np
from turtle import color
import serial as ser
import mouse #keyboard can also be used (1)

plt.style.use('dark_background')
s = ser.Serial('COM4', 9600) #Reads the data coming from the arduino readings
counter1= 0
counter = 0

data = np.array([])
data1 = np.array([])

plt.close('all')
plt.figure()
plt.ion()
plt.show()
while not mouse.is_pressed('right'): #quick fix to a never-closing bug (1)
    if(counter==0):
        a = s.readline()
        a.decode()
        counter= counter +1
    else:
        a = s.readline()
        a.decode()
        b = float(a[0:4])
        c = 54
        data = np.append(data, b)
        data1 = np.append(data1, c)
        plt.subplot(1, 2, 1) # row 1, col 2 index 1
        plt.plot(data, color='slateblue')
        plt.plot(data1, color='crimson')
        plt.title("Valores de conductividad")
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Conductividad (ms/m^2) ')
        plt.subplot(1, 2, 2) # index 2
        if (b>54): #Text plot 
            plt.text(0.5, 0.5, b, fontsize = 20, color=('crimson'))
            plt.pause(0.5)
            plt.text(0.5, 0.5,b , fontsize = 20, color=('black'))
        else:
            plt.text(0.5, 0.5, b, fontsize = 20, color=('white'))
            plt.pause(0.5)
            plt.text(0.5, 0.5,b , fontsize = 20, color=('black'))
        plt.title("Valores de conductividad (ms/m^2)")        
quit()
