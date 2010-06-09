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
                val = 0
                try:
                    val = float(data[key])
                except ValueError:
                    val = 0
                csvDict[key] = [val]
            firstRow = False
        else:
            for key in data.keys():
                csvDict[key].append(float(data[key]))

    return csvDict

def gis_local_op_global_traffic_2(csvName):
    fname = 'global_traffic.csv'
    
    title = "Global Traffic per Operation"
    xlabel = "Operations"
    ylabel = "Global Traffic"
    
    axisLineWidth = 2.0
    axisLineAntialiased = True
    axisGrid = True
    
    legendFontsize = 12
    legendShadow = False    
    legendFancybox = False
    
    
    legendAlpha = 0.5
    legendColor = 'w'

    csvDict = csv_to_dict(fname)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # red dashes, blue squares and green triangles
#    lineHard, lineDidic, lineRandom = plt.plot(csvDict["OP"], csvDict["L HARD 2"],
#                                               csvDict["OP"], csvDict["L DiDiC 2"],
#                                               csvDict["OP"], csvDict["L RAND 2"],
#                                               linewidth=axisLineWidth)    
    lineHard = plt.plot(csvDict["OP"], csvDict["L HARD 2"],
                         linewidth=axisLineWidth)
    lineDidic = plt.plot(csvDict["OP"], csvDict["L DiDiC 2"],
                          linewidth=axisLineWidth)
    lineRandom = plt.plot(csvDict["OP"], csvDict["L RAND 2"],
                          linewidth=axisLineWidth)        

    plt.setp(lineHard, color='r', linewidth=axisLineWidth, antialiased=axisLineAntialiased)
    plt.setp(lineDidic, color='b', linewidth=axisLineWidth, antialiased=axisLineAntialiased)
    plt.setp(lineRandom, color='g', linewidth=axisLineWidth, antialiased=axisLineAntialiased)

    legend = ax.legend((lineHard, lineDidic, lineRandom),
                       (r'Hardcode', r'DiDiC', r'Random'),
                       'upper right',
                       shadow=legendShadow,
                       fancybox=legendFancybox)
    
    frame = legend.get_frame()  
    frame.set_facecolor(legendColor)
    frame.set_alpha(legendAlpha)
    
    ltext = legend.get_texts()
    pylab.setp(ltext[0], fontsize=legendFontsize)
    pylab.setp(ltext[1], fontsize=legendFontsize)
    pylab.setp(ltext[2], fontsize=legendFontsize)

#    plt.axis([0, 2000, 0, 100])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axisGrid)
        
    plb.savefig("bla.png",
                dpi=300,
                facecolor='w',
                edgecolor='w',
                orientation='portrait',
                papertype=None,
                format='png', #png, pdf, ps, eps and svg
                transparent=True)
    
    show()

def gis_local_op_global_traffic_2_separate(csvName):
    csvName = 'global_traffic.csv'
    
    axisLineWidth = 2.0
    axisGrid = True
    axisLineAntialiased = True
    legendFontsize = 12
    legendAlpha = 0.5
    legendShadow = False    
    legendColor = 'w'
    legendFancybox = False
    
    csvDict = csv_to_dict(csvName)
        
    fig = plt.figure(1)

    #  subplot(numrows, numcols, fignum) 
    #  plt.subplot(2,1,1) also valid 
    ax1 = fig.add_subplot(3, 1, 1)
    line1, = plt.plot(csvDict["OP"], csvDict["L HARD 2"], 'b')

    legend1 = ax1.legend((line1,),
                       (r'Hardcode',),
                       'upper right',
                       shadow=legendShadow,
                       fancybox=legendFancybox)
    ltext1 = legend1.get_texts()
    pylab.setp(ltext1[0], fontsize=legendFontsize)
#    ax1.set_xscale('log')
    plt.title("Global Traffic per Operation")
    ax1.set_xticklabels([])
    plt.ylabel('Global Traffic')
    plt.grid(axisGrid)
    
    # the matplotlib.patches.Rectangle instance surrounding the legend
    frame1 = legend1.get_frame()  
    frame1.set_facecolor(legendColor)
    frame1.set_alpha(legendAlpha)

    
    ax2 = plt.subplot(312)
    line2, = plt.plot(csvDict["OP"], csvDict["L DiDiC 2"], 'g')

    legend2 = ax2.legend((line2,),
                         (r'DiDiC',),
                         'upper right',
                         shadow=legendShadow,
                         fancybox=legendFancybox)
    ltext2 = legend2.get_texts()
    pylab.setp(ltext2[0], fontsize=legendFontsize)
#    ax2.set_xscale('log')
    ax2.set_xticklabels([])
    plt.ylabel('Global Traffic')
    plt.grid(axisGrid)

    # the matplotlib.patches.Rectangle instance surrounding the legend
    frame2 = legend2.get_frame()  
    frame2.set_facecolor(legendColor)
    frame2.set_alpha(legendAlpha)


    ax3 = plt.subplot(313)
    line3, = plt.plot(csvDict["OP"], csvDict["L RAND 2"], 'r')

    legend3 = ax3.legend((line3,),
                         (r'Random',),
                         'upper right',
                         shadow=legendShadow,
                         fancybox=legendFancybox)
    ltext3 = legend3.get_texts()
    pylab.setp(ltext3[0], fontsize=legendFontsize)
#    ax3.set_xscale('log')
    plt.xlabel('Operations')
    plt.ylabel('Global Traffic')
    plt.grid(axisGrid)
        
    # the matplotlib.patches.Rectangle instance surrounding the legend
    frame3 = legend3.get_frame()  
    frame3.set_facecolor(legendColor)
    frame3.set_alpha(legendAlpha)

    
    plt.setp(line1, linewidth=axisLineWidth, antialiased=axisLineAntialiased)
    plt.setp(line2, linewidth=axisLineWidth, antialiased=axisLineAntialiased)
    plt.setp(line3, linewidth=axisLineWidth, antialiased=axisLineAntialiased)    
        
    plb.savefig("bla.png",
                dpi=300,
                facecolor='w',
                edgecolor='w',
                orientation='portrait',
                papertype=None,
                format='png', #png, pdf, ps, eps and svg
                transparent=True)
    show()

def line_from_file(csvName, xAxis, yAxes, fileName="output.pdf", title='Title Goes Here', xLabel='xLabel', yLabel='yLabel',
                   figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait', figPapertype=None, figFormat='pdf', figTransparent=True,
                   axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                   legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w', legendFancybox=False, legendPos='upper right'):
    
    csvDict = csv_to_dict(csvName)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    legendLines = ()
    legendLineNames = ()
    
    for (yAxis, yColor, axisName) in yAxes:
        line = plt.plot(csvDict[xAxis], csvDict[yAxis],
                        linewidth=axisLineWidth)
        plt.setp(line, color=yColor, linewidth=axisLineWidth, antialiased=axisLineAntialiased)
        legendLines += (line,)
        legendLineNames += (axisName,)
        
    legend = ax.legend(legendLines,
                       legendLineNames,
                       legendPos,
                       shadow=legendShadow,
                       fancybox=legendFancybox)
    
    frame = legend.get_frame()  
    frame.set_facecolor(legendColor)
    frame.set_alpha(legendAlpha)
    
    for ltext in legend.get_texts():
        pylab.setp(ltext, fontsize=legendFontsize)
    
#    plt.axis([0, 2000, 0, 100])
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(axisGrid)
        
    plb.savefig(fileName,
                dpi=figDpi,
                facecolor=figFacecolor,
                edgecolor=figEdgecolor,
                orientation=figOrientation,
                papertype=figPapertype,
                format=figFormat, #png, pdf, ps, eps and svg
                transparent=figTransparent)
    
    show()

def line_from_file_separate_sym(csvName, axes, fileName="output.pdf",

                                figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait', figPapertype=None, figFormat='pdf', figTransparent=True,
                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w', legendFancybox=False, legendPos='upper right'):
                
    csvDict = csv_to_dict(csvName)
    
    numRows = len(axes)    
    numCols = max([len(row) for row in axes])
    figNum = 0
        
    fig = plt.figure(1)

    currentRow = -1
    for axesRow in axes:
        currentRow += 1
        figNum = currentRow * numCols
        for (xAxis, yAxis, yColor, xLabel, yLabel, axisTitle) in axesRow:
            figNum += 1
            
            print numRows, numCols, figNum
            
            #  subplot(numrows, numcols, fignum) 
            #  plt.subplot(2,1,1) also valid 
            ax = fig.add_subplot(numRows, numCols, figNum)
            line, = plt.plot(csvDict[xAxis], csvDict[yAxis], yColor)
            
            legend = ax.legend((line,),
                               (yLabel,),
                               legendPos,
                               shadow=legendShadow,
                               fancybox=legendFancybox)
            ltext = legend.get_texts()
            pylab.setp(ltext[0], fontsize=legendFontsize)
        #    ax.set_xscale('log')
            plt.title(axisTitle)
            plt.xlabel(xLabel)
            plt.ylabel(yLabel)
            if xLabel == '':
                ax.set_xticklabels([])
            plt.grid(axisGrid)
            
            # the matplotlib.patches.Rectangle instance surrounding the legend
            frame1 = legend.get_frame()  
            frame1.set_facecolor(legendColor)
            frame1.set_alpha(legendAlpha)
        
            plt.setp(line, linewidth=axisLineWidth, antialiased=axisLineAntialiased)
    
    
    plb.savefig(fileName,
                dpi=figDpi,
                facecolor=figFacecolor,
                edgecolor=figEdgecolor,
                orientation=figOrientation,
                papertype=figPapertype,
                format=figFormat, #png, pdf, ps, eps and svg
                transparent=figTransparent)
    show()

def hist_from_file(csvName, values,
                   binCount=10, fileName="output.pdf",
                   figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait', figPapertype=None, figFormat='pdf', figTransparent=True,
                   barFacecolor='blue', barEdgecolor='gray', barHisttype='bar', barAlpha=0.75, barAlign='mid', barOrientation='vertical',
                   axisGrid=True, axisFontSize=12, axisXLabel='xLabel', axisYLabel='yLabel', axisName='axisName', axisColor='b', axisTitle='Title Goes Here',
                   legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w', legendFancybox=False, legendPos='upper right'):
    
    csvDict = csv_to_dict(csvName)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    #histtype = 'bar' 'barstacked' 'step' 'stepfilled'
    #align = 'left' 'mid' 'right'
    #orientation: 'horizontal' 'vertical'
    n, bins, patches = ax.hist(csvDict[values], binCount,
                               label=axisName,
                               normed=0, cumulative=0,
                               facecolor=barFacecolor, edgecolor=barEdgecolor,
                               alpha=barAlpha, histtype=barHisttype, align=barAlign,
                               orientation=barOrientation)
    
#    n, bins, patches = plt.hist([x0, x1, x2], 10, histtype='bar')
#    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
        
    legend = ax.legend(shadow=legendShadow, fancybox=legendFancybox)
    
    frame = legend.get_frame()  
    frame.set_facecolor(legendColor)
    frame.set_alpha(legendAlpha)
    
    for ltext in legend.get_texts():
        pylab.setp(ltext, fontsize=legendFontsize)
    
#    plt.axis([0, 2000, 0, 100])
    plt.title(axisTitle)
    plt.xlabel(axisXLabel, fontsize=axisFontSize)
    plt.ylabel(axisYLabel, fontsize=axisFontSize)
    plt.grid(axisGrid)
#    plt.axis([0, max(csvDict[values]), 0, len(csvDict[values])])

        
    plb.savefig(fileName,
                dpi=figDpi,
                facecolor=figFacecolor,
                edgecolor=figEdgecolor,
                orientation=figOrientation,
                papertype=figPapertype,
                format=figFormat, #png, pdf, ps, eps and svg
                transparent=figTransparent)
    
    show()
