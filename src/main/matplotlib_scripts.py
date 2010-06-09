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
                    val = data[key]
                csvDict[key] = [val]
            firstRow = False
        else:
            for key in data.keys():
                val = 0
                try:
                    val = float(data[key])
                except ValueError:
                    val = data[key]
                csvDict[key].append(val)

    return csvDict

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

def line_from_file_separate(csvName, axes, fileName="output.pdf",
                            figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait', figPapertype=None, figFormat='pdf', figTransparent=True,
                            axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                            legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w', legendFancybox=False, legendPos='upper right'):
                
    csvDict = csv_to_dict(csvName)
        
    fig = plt.figure(1)
    
    numRows = len(axes)    

    currentRow = 0
    
    for axesRow in axes:
        currentRow += 1
        numCols = len(axesRow)
        figNum = (currentRow - 1) * numCols
        for (xAxis, yAxis, yColor, xLabel, yLabel, axisTitle) in axesRow:
            figNum += 1
            
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
            if yLabel == '':
                ax.set_yticklabels([])                
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

def hist_from_file_separate(csvName, axes,
                            fileName="output.pdf", figTitle='Title Goes Here',
                            figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait', figPapertype=None, figFormat='pdf', figTransparent=True,
                            barFacecolor='blue', barEdgecolor='gray', barHisttype='bar', barAlpha=0.75, barAlign='mid', barOrientation='vertical',
                            axisGrid=True, axisFontSize=12,
                            legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w', legendFancybox=False, legendPos='upper right'):
                
    csvDict = csv_to_dict(csvName)
    
    fig = plt.figure(1)

    numRows = len(axes)    
        
    currentRow = 0
    
    for axesRow in axes:
        currentRow += 1
        numCols = len(axesRow)
        figNum = (currentRow - 1) * numCols
        for (vals, valsBins, barFaceColor, barEdgeColor, axisXLabel, axisYLabel, axisName, axisTitle) in axesRow:
            figNum += 1
            
            print vals, valsBins, barFaceColor, barEdgeColor, axisXLabel, axisYLabel, axisTitle

            #  subplot(numrows, numcols, fignum) 
            #  plt.subplot(2,1,1) also valid 
            ax = fig.add_subplot(numRows, numCols, figNum)
#            ax.set_yscale('log')

            
            #histtype = 'bar' 'barstacked' 'step' 'stepfilled'
            #align = 'left' 'mid' 'right'
            #orientation: 'horizontal' 'vertical'
            n, bins, patches = ax.hist(csvDict[vals], valsBins,
                                       label=axisName,
                                       normed=0, cumulative=0,
                                       facecolor=barFaceColor, edgecolor=barEdgecolor,
                                       alpha=barAlpha, histtype=barHisttype, align=barAlign,
                                       orientation=barOrientation)
            
            legend = ax.legend(shadow=legendShadow, fancybox=legendFancybox)
            
            frame = legend.get_frame()  
            frame.set_facecolor(legendColor)
            frame.set_alpha(legendAlpha)
            
            for ltext in legend.get_texts():
                pylab.setp(ltext, fontsize=legendFontsize)

#            plt.axis([0, 2000, 0, 100])
            plt.title(axisTitle)
            plt.xlabel(axisXLabel, fontsize=axisFontSize)
            plt.ylabel(axisYLabel, fontsize=axisFontSize)
            if axisXLabel == '':
                ax.set_xticklabels([])
            if axisYLabel == '':
                ax.set_yticklabels([])                
            plt.grid(axisGrid)
#            plt.axis([0, max(csvDict[values]), 0, len(csvDict[values])])


    plb.savefig(fileName,
                dpi=figDpi,
                facecolor=figFacecolor,
                edgecolor=figEdgecolor,
                orientation=figOrientation,
                papertype=figPapertype,
                format=figFormat, #png, pdf, ps, eps and svg
                transparent=figTransparent)

    show()

def bar_from_file(csvName, xAxis, yAxes, yLabels,
                  binCount=10, fileName="output.pdf",
                  figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait', figPapertype=None, figFormat='pdf', figTransparent=True,
                  barEdgecolor='gray', barHisttype='bar', barAlpha=0.75, barAlign='mid', barOrientation='vertical',
                  axisGrid=True, axisFontSize=12, axisYLabel='yLabel', axisTitle='Title Goes Here',
                  legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w', legendFancybox=False, legendPos='upper right'):
    
    csvDict = csv_to_dict(csvName)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    n = max([len(csvDict[val]) for (val, clr) in yAxes])
    ind = np.arange(n)  # the x locations for the groups
    width = 0.4       # the width of the bars

    rectsColl = []
    barCount = -1    
    for (yAxis, barColor) in yAxes:
        barCount += 1
        
        rects = ax.bar(ind + (width * barCount), csvDict[yAxis], width,
                       color=barColor, edgecolor=barEdgecolor, linewidth=None)
        rectsColl += [rects]
    
#    ax.set_ylabel(axisYLabel)
#    ax.set_title(axisTitle)
    print ind
    print width
    print ind + width
    ax.set_xticks(ind + width)
    ax.set_xticklabels(csvDict[xAxis])

    legend = ax.legend([rects[0] for rects in rectsColl], yLabels,
                       shadow=legendShadow, fancybox=legendFancybox)
    
    def autolabel(rects):
        # attach some text labels (Optional)
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
                    ha='center', va='bottom')
    
    for rects in rectsColl:
        autolabel(rects)
    
    frame = legend.get_frame()  
    frame.set_facecolor(legendColor)
    frame.set_alpha(legendAlpha)
    
    for ltext in legend.get_texts():
        pylab.setp(ltext, fontsize=legendFontsize)
    
#    plt.axis([0, 2000, 0, 100])
    plt.title(axisTitle)
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
