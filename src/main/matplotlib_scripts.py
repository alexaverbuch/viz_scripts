import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
import matplotlib.mlab as mlab
import pylab as plb
import csv
from pylab import *

def csv_to_dict(filename):
    csvFileName = filename
    csvDict = {}
    csvFile = open(csvFileName, "rb")
    csvReader = csv.DictReader(csvFile,
                               delimiter=',',
                               quotechar='"',
                               quoting=csv.QUOTE_ALL)

    firstRow = True
    for data in csvReader:        
        if firstRow:
            for key in data.keys():
                csvDict[key] = [float(data[key])]
            firstRow = False
        else:
            for key in data.keys():
                csvDict[key].append(float(data[key]))

    return csvDict

def gis_local_op_global_traffic_2():
    fname = 'global_traffic.csv'
    csvDict = csv_to_dict(fname)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # red dashes, blue squares and green triangles
    lineHard, lineDidic, lineRandom = plt.plot(csvDict["OP"], csvDict["L HARD 2"],
                                               csvDict["OP"], csvDict["L DiDiC 2"],
                                               csvDict["OP"], csvDict["L RAND 2"],
                                               linewidth=2.0)    

    plt.setp(lineHard, color='r', linewidth=2.0, antialiased=True)
    plt.setp(lineDidic, color='b', linewidth=2.0, antialiased=True)
    plt.setp(lineRandom, color='g', linewidth=2.0, antialiased=True)

    fontSize = 12

    legend = ax.legend((lineHard, lineDidic, lineRandom),
                       (r'Hardcode', r'DiDiC', r'Random'),
                       'upper right',
                       shadow=True)

    ltext = legend.get_texts()
    pylab.setp(ltext[0], fontsize=fontSize)
    pylab.setp(ltext[1], fontsize=fontSize)
    pylab.setp(ltext[2], fontsize=fontSize)

#    plt.axis([0, 2000, 0, 100])
    plt.title("Global Traffic per Operation")
    plt.xlabel('Operations')
    plt.ylabel('Global Traffic')
    plt.grid(True)
        
    show()

def gis_local_op_global_traffic_2_separate():
    fname = 'global_traffic.csv'
    csvDict = csv_to_dict(fname)
    fontSize = 12
        
    fig = plt.figure(1)

    #  subplot(numrows, numcols, fignum) 
    #  plt.subplot(2,1,1) also valid 
    ax1 = fig.add_subplot(311)
    line1, = plt.plot(csvDict["OP"], csvDict["L HARD 2"], 'b')

    legend1 = ax1.legend((line1,),
                       (r'Hardcode',),
                       'upper right',
                       shadow=True)
    ltext1 = legend1.get_texts()
    pylab.setp(ltext1[0], fontsize=fontSize)
#    ax1.set_xscale('log')
    plt.title("Global Traffic per Operation")
    ax1.set_xticklabels([])
    plt.ylabel('Global Traffic')
    plt.grid(True)

    
    ax2 = plt.subplot(312)
    line2, = plt.plot(csvDict["OP"], csvDict["L DiDiC 2"], 'g')

    legend2 = ax2.legend((line2,),
                         (r'DiDiC',),
                         'upper right',
                         shadow=True)
    ltext2 = legend2.get_texts()
    pylab.setp(ltext2[0], fontsize=fontSize)
#    ax2.set_xscale('log')
    ax2.set_xticklabels([])
    plt.ylabel('Global Traffic')
    plt.grid(True)

    ax3 = plt.subplot(313)
    line3, = plt.plot(csvDict["OP"], csvDict["L RAND 2"], 'r')

    legend3 = ax3.legend((line3,),
                         (r'Random',),
                         'upper right',
                         shadow=True)
    ltext3 = legend3.get_texts()
    pylab.setp(ltext3[0], fontsize=fontSize)
#    ax3.set_xscale('log')
    plt.xlabel('Operations')
    plt.ylabel('Global Traffic')
    plt.grid(True)
    
    plt.setp(line1, linewidth=2.0, antialiased=True)
    plt.setp(line2, linewidth=2.0, antialiased=True)
    plt.setp(line3, linewidth=2.0, antialiased=True)    
        
    show()
