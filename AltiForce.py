from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
import matplotlib.pyplot as plt

class AltiForce():
    def __init__(self, filepath):
        self.filepath = filepath
        
        self.loadCSV()
        self.plotdata()
        
    def loadCSV(self):
        colnames = ['vid_timestamp', 'abs_press', 'altitude', 'temp', 'accel_x', 'accel_y', 'accel_z',
                    'flags', 'lat', 'lon', 'gps_alt', 'gps_speed', 'heading', 'dist', 'accuracy',
                    'used_sat', 'total_sat', 'gps_timestamp']
        alldata = np.genfromtxt(self.filepath, delimiter=',', skip_header=11, names=colnames)

        # Convert data
        # Conversion factors are included in the header, starting manually for now
        alldata['vid_timestamp'] /= 1000.0  # Convert to seconds
        alldata['abs_press'] /= 100.0       # Convert to millibar
        alldata['altitude'] /= 1.0          # Convert to feet
        alldata['temp'] /= 10.0             # Convert to degrees C
        alldata['accel_x'] /= 2048          # Convert to Gees
        alldata['accel_y'] /= 2048          # Convert to Gees
        alldata['accel_z'] /= 2048          # Convert to Gees

        self.alldata = alldata

    def plotdata(self):
        x = self.alldata['vid_timestamp']
        y1 = self.alldata['altitude']
        y2 = self.alldata['accel_z']

        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.plot(x, y1, 'g-')
        ax2.plot(x, y2, 'b-')

        ax1.set_xlabel('Time (seconds)')
        ax1.set_ylabel('Altitude (feet)', color='g')
        ax2.set_ylabel('Z Acceleration (Gees)', color='b')

        plt.show()


if __name__ == "__main__":
    Tk().withdraw()
    filepath = askopenfilename()
    
    if filepath:
        mydata = AltiForce(filepath)