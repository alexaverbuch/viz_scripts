from matplotlib import rc
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

def init_tex():
#    rc('font', **{'family':'sans-serif', 'sans-serif':['Helvetica']})
    rc('font', **{'family':'times'})
    ## for Palatino and other serif fonts use:
    #rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)
    
        
def show_plot(plot_fun,
              fileName="output.pdf",
              figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait',
              figPapertype=None, figFormat='pdf', figTransparent=True):
    
    init_tex()
    
    fig = plt.figure(1)
    
    plot_fun(fig, 1, 1, 1)
    
    plb.savefig(fileName,
                dpi=figDpi,
                facecolor=figFacecolor,
                edgecolor=figEdgecolor,
                orientation=figOrientation,
                papertype=figPapertype,
                format=figFormat, #png, pdf, ps, eps and svg
                transparent=figTransparent)
    
    show()
    
def show_plots(plotFuns,
               fileName="output.pdf",
               figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait',
               figPapertype=None, figFormat='pdf', figTransparent=True):
    
    init_tex()
    
    fig = plt.figure(1)
    
    numRows = len(plotFuns)    
        
    currentRow = 0
    
    for plotFunsRow in plotFuns:
        currentRow += 1
        numCols = len(plotFunsRow)
        figNum = (currentRow - 1) * numCols
        for plotFun in plotFunsRow:
            figNum += 1
            
            plotFun(fig, numRows, numCols, figNum)
            
    plb.savefig(fileName,
                dpi=figDpi,
                facecolor=figFacecolor,
                edgecolor=figEdgecolor,
                orientation=figOrientation,
                papertype=figPapertype,
                format=figFormat, #png, pdf, ps, eps and svg
                transparent=figTransparent)

    show()
    
def get_line_from_file(csvName, xAxis, yAxes,
                       axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True, axisFontSize=12, axisColor='k',
                       axisXLabel='xLabel', axisYLabel='yLabel', axisTitle='axisTitle',
                       legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                       legendFancybox=False, legendPos='upper right'):
    
    def do_line_from_file(fig, numRows, numCols, figNum):
        
        csvDict = csv_to_dict(csvName)

        ax = fig.add_subplot(numRows, numCols, figNum)
        
        legendLines = ()
        legendLineNames = ()
        
        for (yAxis, yColor, axisName) in yAxes:
            line = plt.plot(csvDict[xAxis], csvDict[yAxis], linewidth=axisLineWidth)
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
        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_xlabel(axisXLabel, fontsize=axisFontSize)
        ax.set_ylabel(axisYLabel, fontsize=axisFontSize)
        ax.grid(axisGrid)
        
    return do_line_from_file
        
def get_hist_from_file(csvName, values,
                       barBinCount=10, barFacecolor='blue', barEdgecolor='gray', barHisttype='bar',
                       barAlpha=0.75, barAlign='mid', barOrientation='vertical',
                       axisGrid=True, axisFontSize=12, axisColor='k',
                       axisXLabel='xLabel', axisYLabel='yLabel', axisName='axisName', axisTitle='Title Goes Here',
                       legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                       legendFancybox=False, legendPos='upper right'):
    
    def do_hist_from_file(fig, numRows, numCols, figNum):            
        
        csvDict = csv_to_dict(csvName)
    
        if fig == False:
            fig = plt.figure()
            
        ax = fig.add_subplot(numRows, numCols, figNum)
        
        #histtype = 'bar' 'barstacked' 'step' 'stepfilled'
        #align = 'left' 'mid' 'right'
        #orientation: 'horizontal' 'vertical'
        n, bins, patches = ax.hist(csvDict[values], barBinCount,
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
        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_xlabel(axisXLabel, fontsize=axisFontSize)
        ax.set_ylabel(axisYLabel, fontsize=axisFontSize)
        ax.grid(axisGrid)
    #    plt.axis([0, max(csvDict[values]), 0, len(csvDict[values])])
    
    return do_hist_from_file

def get_bar_from_file(csvName, xAxis, yAxes, yLabels,
                      barEdgecolor='gray', barHisttype='bar', barAlpha=0.75,
                      barAlign='mid', barOrientation='vertical', barWidth=0.3,
                      axisGrid=True, axisFontSize=12, axisColor='k',
                      axisYLabel='yLabel', axisTitle='Title Goes Here',
                      legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                      legendFancybox=False, legendPos='upper right'):
    
    def do_bar_from_file(fig, numRows, numCols, figNum):
            
        csvDict = csv_to_dict(csvName)
    
        ax = fig.add_subplot(numRows, numCols, figNum)
    
        n = max([len(csvDict[val]) for (val, clr) in yAxes])
        ind = np.arange(n)  # the x locations for the groups
    
        rectsColl = []
        barCount = -1    
        for (yAxis, barColor) in yAxes:
            barCount += 1
            
            rects = ax.bar(ind + (barWidth * barCount), csvDict[yAxis], barWidth,
                           color=barColor, edgecolor=barEdgecolor, linewidth=None)
            rectsColl += [rects]
        
#    #    ax.set_ylabel(axisYLabel)
#    #    ax.set_title(axisTitle)
#        ax.set_xticks(ind + barWidth)
#        ax.set_xticklabels(csvDict[xAxis])
    
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
        
    #    ax.axis([0, 2000, 0, 100])
        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_ylabel(axisYLabel, fontsize=axisFontSize)
        ax.grid(axisGrid)
        ax.set_xticks(ind + barWidth)
        ax.set_xticklabels(csvDict[xAxis])
    #    plt.axis([0, max(csvDict[values]), 0, len(csvDict[values])])

    return do_bar_from_file
