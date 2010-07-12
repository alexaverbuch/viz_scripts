from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
import matplotlib.mlab as mlab
import pylab as plb
import csv
try:
    import Image
except ImportError, exc:
    raise SystemExit("PIL must be installed")

def csv_to_dict(filename, columns,
                default='float', ints=(), floats=()):
    
    csvFileName = filename
    csvDict = {}
    csvFile = open(csvFileName, "rb")
    csvReader = csv.DictReader(csvFile,
                               delimiter=',',
#                               delimiter=';',
                               quotechar='"',
                               quoting=csv.QUOTE_ALL)
    
    def read_int(val):
        returnVal = 0
        try:
            returnVal = int(float(val))
        except ValueError:
            if val == '':
#                print 'no val'
                returnVal = None
            else:
                raise ValueError
        return returnVal

    def read_float(val):
        returnVal = 0.0
        try:
            returnVal = float(val)
        except ValueError:
            if val == '':
#                print 'no val'
                returnVal = None
            else:
                raise ValueError
        return returnVal

    def read_string(val):
        return val
        
    firstRow = True
    for data in csvReader:        
        if firstRow:
            for key in data.keys():
                if (key in columns) == False:
                    continue
                
                val = None
                if key in floats:
                    val = [read_float(data[key])]
                elif key in ints:
                    val = [read_int(data[key])]
                else:
                    val = [read_string(data[key])]
                if val != [None]:
                    csvDict[key] = val
                    firstRow = False
        else:
            for key in data.keys():
                if (key in columns) == False:
                    continue
                
                val = None
                if key in floats:
                    val = read_float(data[key])
                elif key in ints:
                    val = read_int(data[key])
                else :
                    val = read_string(data[key])                
                if val != None:
                    csvDict[key].append(val)

    return csvDict

def init_tex():
#    rc('font', **{'family':'sans-serif', 'sans-serif':['Helvetica']})
#    rc('font', **{'family':'times'})
    ## for Palatino and other serif fonts use:
    #rc('font',**{'family':'serif','serif':['Palatino']})
#    rc('text', usetex=True)
    
    params = {'backend': 'ps',
              'axes.labelsize': 10,
              'text.fontsize': 8,
              'legend.fontsize': 8,
              'xtick.labelsize': 8,
              'ytick.labelsize': 8,
              'text.usetex': True,
              'font.family': 'times'}
    plb.rcParams.update(params)
        
def show_plots(plotFuns,
               fileName="output.pdf", show=True,
               figDpi=300, figFacecolor='w', figEdgecolor='w', figOrientation='portrait',
               figPapertype=None, figFormat='pdf', figTransparent=True,
               figWSpace=0.2, figHSpace=0.2, figSize=None,
               figLeftSpace=0.125, figRightSpace=0.9, figBottomSpace=0.1, figTopSpace=0.9):
    
    init_tex()
    
    fig = plt.figure(1, figsize=figSize)
    fig.clf()
    
    fig.subplots_adjust(wspace=figWSpace, hspace=figHSpace,
                        left=figLeftSpace, right=figRightSpace,
                        bottom=figBottomSpace, top=figTopSpace)
    
    numRows = len(plotFuns)    
        
    currentRow = 0
    
    axesDict = {}
    
    for plotFunsRow in plotFuns:
        currentRow += 1
        numCols = len(plotFunsRow)
        figNum = (currentRow - 1) * numCols
        for plotFun in plotFunsRow:
            figNum += 1            
            if plotFun == None:
                continue
            plotFun(fig, numRows, numCols, figNum, axesDict)
            
    plb.savefig(fileName,
                dpi=figDpi,
                facecolor=figFacecolor,
                edgecolor=figEdgecolor,
                orientation=figOrientation,
                papertype=figPapertype,
                format=figFormat, #png, pdf, ps, eps and svg
                transparent=figTransparent)

    if show == True:
        plb.show()
    
def get_line_from_file(csvName, xAxis, yAxes, annotations=[],
                       csvInts=(), csvFloats=(),
                       axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True, axisColor='k',
                       axisFontSize=12, axisTickFontSize=12,
                       axisXLabel='', axisYLabel='', axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                       axisXFormatterFun=None, axisYFormatterFun=None,
                       axisXScale='linear', axisYScale='linear',
                       legendFontsize=8, legendAlpha=0.5, legendShadow=False, legendColor='w',
                       legendFancybox=False, legendPos='upper right', legendCols=1,
                       myShareAxis=None, shareAxisX=None, shareAxisY=None):
    
    def do_line_from_file(fig, numRows, numCols, figNum, axesDict):
        
        csvDict = csv_to_dict(csvName,
                              (xAxis,) + tuple([yAxis for (yAxis, _c, _n, _s, _m) in yAxes]),
                              ints=csvInts,
                              floats=csvFloats)
        
        xlabel = axisXLabel
        ylabel = axisYLabel
        xticks = True
        yticks = True
        if axisXLabel == None:
            xticks = False
            xlabel = ''
        if axisYLabel == None:
            yticks = False
            ylabel = ''
            
        sharex = None
        sharey = None
        if shareAxisX != None:
            sharex = axesDict[shareAxisX]
        if shareAxisY != None:
            sharey = axesDict[shareAxisY]

        ax = fig.add_subplot(numRows, numCols, figNum,
                             sharex=sharex, sharey=sharey)
        
        if myShareAxis != None:
            axesDict[myShareAxis] = ax                    
        
        legendLines = ()
        legendLineNames = ()
        
        for (yAxis, yColor, axisName, lineStyle, lineMarker) in yAxes:
            line = plt.plot(csvDict[xAxis], csvDict[yAxis], linewidth=axisLineWidth)
            plt.setp(line, color=yColor, antialiased=axisLineAntialiased,
                     linewidth=axisLineWidth, linestyle=lineStyle, marker=lineMarker)
            legendLines += (line,)
            legendLineNames += (axisName,)
            
        for annotation in annotations:
            annotation(ax)
            
        legend = None
        
        if legendPos != None:        
            legend = ax.legend(legendLines,
                               legendLineNames,
                               legendPos,
                               shadow=legendShadow,
                               fancybox=legendFancybox,
                               ncol=legendCols)
        
        if legend != None: 
            frame = legend.get_frame()  
            frame.set_facecolor(legendColor)
            frame.set_alpha(legendAlpha)
        
            for ltext in legend.get_texts():
                plb.setp(ltext, fontsize=legendFontsize)
        
        formx = None
        if axisXFormatterFun == None:
            formx = plt.ScalarFormatter()
            formx.set_powerlimits((-3, 4))
            formx.set_scientific(True)
            ax.xaxis.set_major_formatter(formx)        
            ax.set_xscale(axisXScale, fontsize=axisFontSize) # linear,log,symlog
            for xticklabel in ax.xaxis.get_ticklabels():
#                label.set_color('red')
#                label.set_rotation(45)
                xticklabel.set_fontsize(axisTickFontSize)
        else:
            ax.set_xscale(axisXScale, fontsize=axisFontSize) # linear,log,symlog
            formx = ticker.FuncFormatter(axisXFormatterFun)
            ax.xaxis.set_major_formatter(formx)        

        formy = None
        if axisYFormatterFun == None:
            formy = plt.ScalarFormatter()
            formy.set_powerlimits((-3, 4))
            formy.set_scientific(True)
            ax.yaxis.set_major_formatter(formy)
            ax.set_yscale(axisYScale, fontsize=axisFontSize) # linear,log,symlog
            for yticklabel in ax.yaxis.get_ticklabels():
#                label.set_color('red')
#                label.set_rotation(45)
                yticklabel.set_fontsize(axisTickFontSize)
        else:
            ax.set_yscale(axisYScale, fontsize=axisFontSize) # linear,log,symlog
            formy = ticker.FuncFormatter(axisYFormatterFun)
            ax.yaxis.set_major_formatter(formy)        

        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_xlabel(xlabel, fontsize=axisFontSize)
        ax.set_ylabel(ylabel, fontsize=axisFontSize)
#        ax.set_xscale(axisXScale) # linear,log,symlog
#        ax.set_yscale(axisYScale) # linear,log,symlog
        ax.grid(axisGrid)
        if xticks == False:
            ax.set_xticks([])
#        else:
#            xticks = ax.get_xticks()
#            ax.set_xticklabels([r"$\mathbf{%s}$" % x for x in xticks])
            
        if yticks == False:
            ax.set_yticks([])
#        else:
#            yticks = ax.get_yticks()
#            ax.set_yticklabels([r"$\mathbf{%s}$" % y for y in yticks])
            
        ax.set_xlim(axisXLim)
        ax.set_ylim(axisYLim)

                            
    return do_line_from_file

def get_line_from_file_multi_x(csvName, axes, annotations=[],
                               csvInts=(), csvFloats=(),
                               axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True, axisColor='k',
                               axisFontSize=10, axisTickFontSize=10,
                               axisXLabel='', axisYLabel='', axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                               axisXFormatterFun=None, axisYFormatterFun=None,
                               axisXScale='linear', axisYScale='linear',
                               legendFontsize=8, legendAlpha=0.5, legendShadow=False, legendColor='w',
                               legendFancybox=False, legendPos='upper right', legendCols=1, 
                               legendBorderAxesPad=0.0, legendBorderPad=0.2, legendTop = True, 
                               legendTopAnchor = (0., 1.07, 1., .102), legendLabelSpace=0.1,
                               myShareAxis=None, shareAxisX=None, shareAxisY=None):
    
    def do_line_from_file(fig, numRows, numCols, figNum, axesDict):
        
        csvDict = csv_to_dict(csvName,
                              tuple([yAxis for (_xAxis, yAxis, _c, _n, _s, _m) in axes]) + 
                              tuple([xAxis for (xAxis, _yAxis, _c, _n, _s, _m) in axes]),
                              ints=csvInts,
                              floats=csvFloats)
        
        xlabel = axisXLabel
        ylabel = axisYLabel
        xticks = True
        yticks = True
        if axisXLabel == None:
            xticks = False
            xlabel = ''
        if axisYLabel == None:
            yticks = False
            ylabel = ''
            
        sharex = None
        sharey = None
        if shareAxisX != None:
            sharex = axesDict[shareAxisX]
        if shareAxisY != None:
            sharey = axesDict[shareAxisY]

        ax = fig.add_subplot(numRows, numCols, figNum,
                             sharex=sharex, sharey=sharey)
        
        if myShareAxis != None:
            axesDict[myShareAxis] = ax                    
        
        legendLines = ()
        legendLineNames = ()
        
        for (xAxis, yAxis, yColor, axisName, lineStyle, lineMarker) in axes:
            line = plt.plot(csvDict[xAxis], csvDict[yAxis], linewidth=axisLineWidth)
            plt.setp(line, color=yColor, antialiased=axisLineAntialiased,
                     linewidth=axisLineWidth, linestyle=lineStyle, marker=lineMarker,
                     markersize=4.0)
            legendLines += (line,)
            legendLineNames += (axisName,)
            
        for annotation in annotations:
            annotation(ax)
            
        legend = None
        
        if legendPos != None:        
            if legendTop == True:
                legend = ax.legend(legendLines,
                                   legendLineNames,
                                   'lower right',
                                   shadow=legendShadow,
                                   fancybox=legendFancybox,
                                   ncol=legendCols,
                                   bbox_to_anchor=(0., 1.07, 1., .102),
                                   mode="expand",
                                   borderpad=legendBorderPad,
                                   labelspacing=legendLabelSpace, 
                                   borderaxespad=legendBorderAxesPad)
            else:            
                legend = ax.legend(legendLines,
                                   legendLineNames,
                                   legendPos,
                                   shadow=legendShadow,
                                   fancybox=legendFancybox,
                                   ncol=legendCols,
                                   borderpad=legendBorderPad,
                                   labelspacing=legendLabelSpace)
        
        if legend != None: 
            frame = legend.get_frame()  
            frame.set_facecolor(legendColor)
            frame.set_alpha(legendAlpha)
        
            for ltext in legend.get_texts():
                plb.setp(ltext, fontsize=legendFontsize)
        
        formx = None
        if axisXFormatterFun == None:
            formx = plt.ScalarFormatter()
            formx.set_powerlimits((-3, 4))
            formx.set_scientific(True)
            ax.xaxis.set_major_formatter(formx)        
            ax.set_xscale(axisXScale, fontsize=axisFontSize) # linear,log,symlog
            for xticklabel in ax.xaxis.get_ticklabels():
#                label.set_color('red')
#                label.set_rotation(45)
                xticklabel.set_fontsize(axisTickFontSize)
        else:
            ax.set_xscale(axisXScale, fontsize=axisFontSize) # linear,log,symlog
            formx = ticker.FuncFormatter(axisXFormatterFun)
            ax.xaxis.set_major_formatter(formx)        

        formy = None
        if axisYFormatterFun == None:
            formy = plt.ScalarFormatter()
            formy.set_powerlimits((-3, 4))
            formy.set_scientific(True)
            ax.yaxis.set_major_formatter(formy)
            ax.set_yscale(axisYScale, fontsize=axisFontSize) # linear,log,symlog
            for yticklabel in ax.yaxis.get_ticklabels():
#                label.set_color('red')
#                label.set_rotation(45)
                yticklabel.set_fontsize(axisTickFontSize)
        else:
            ax.set_yscale(axisYScale, fontsize=axisFontSize) # linear,log,symlog
            formy = ticker.FuncFormatter(axisYFormatterFun)
            ax.yaxis.set_major_formatter(formy)        

        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_xlabel(xlabel, fontsize=axisFontSize)
        ax.set_ylabel(ylabel, fontsize=axisFontSize)
        ax.grid(axisGrid)
        if xticks == False:
            ax.xaxis.set_ticklabels([])
            
        if yticks == False:
            ax.yaxis.set_ticklabels([])
            
        ax.set_xlim(axisXLim)
        ax.set_ylim(axisYLim)

                            
    return do_line_from_file
        
def get_hist_from_file(csvName, values, annotations=[],
                       csvInts=(), csvFloats=(),
                       barBinCount=10, barFacecolor='blue', barEdgecolor='gray', barHisttype='bar',
                       barAlpha=0.8, barAlign='mid', barOrientation='vertical', barRWidth=None, barLog=False,
                       axisGrid=True, axisFontSize=10, axisTickFontSize=8,
                       axisColor='k', axisXLim=(None, None), axisYLim=(None, None),
                       axisXLabel='', axisYLabel='', axisName='', axisTitle='',
                       axisXFormatterFun=None, axisYFormatterFun=None,
                       legendFontsize=8, legendAlpha=0.5, legendShadow=False, legendColor='w',
                       legendBorderPad=0.2, legendLabelSpace=0.1, legendBorderAxesPad=0.0,
                       legendFancybox=False, legendPos='upper right',
                       myShareAxis=None, shareAxisX=None, shareAxisY=None):
    
    def do_hist_from_file(fig, numRows, numCols, figNum, axesDict):            
        
        csvDict = csv_to_dict(csvName, (values,), ints=csvInts, floats=csvFloats)
        
        xlabel = axisXLabel
        ylabel = axisYLabel
        xticks = True
        yticks = True
        if axisXLabel == None:
            xticks = False
            xlabel = ''
        if axisYLabel == None:
            yticks = False
            ylabel = ''
             
        sharex = None
        sharey = None
        if shareAxisX != None:            
            sharex = axesDict[shareAxisX]
        if shareAxisY != None:
            sharey = axesDict[shareAxisY]

        ax = fig.add_subplot(numRows, numCols, figNum,
                             sharex=sharex, sharey=sharey)
        
        if myShareAxis != None:
            axesDict[myShareAxis] = ax                    

        #histtype = 'bar' 'barstacked' 'step' 'stepfilled'
        #align = 'left' 'mid' 'right'
        #orientation: 'horizontal' 'vertical'
        n, bins, patches = ax.hist(csvDict[values], barBinCount,
                                   label=axisName,
                                   normed=0, cumulative=0,
                                   facecolor=barFacecolor, edgecolor=barEdgecolor,
                                   alpha=barAlpha, histtype=barHisttype, align=barAlign,
                                   orientation=barOrientation, rwidth=barRWidth, log=barLog)
                
        for annotation in annotations:
            annotation(ax)
            
        legend = ax.legend(shadow=legendShadow, 
                           fancybox=legendFancybox,
                           borderpad=legendBorderPad,
                           labelspacing=legendLabelSpace,
                           borderaxespad=legendBorderAxesPad)
        
        if legend != None: 
            frame = legend.get_frame()  
            frame.set_facecolor(legendColor)
            frame.set_alpha(legendAlpha)
        
            for ltext in legend.get_texts():
                plb.setp(ltext, fontsize=legendFontsize)
                
        formy = None
        if axisYFormatterFun == None:
            formy = plt.ScalarFormatter()
            formy.set_powerlimits((-3, 4))
            formy.set_scientific(True)
            ax.yaxis.set_major_formatter(formy)
            for yticklabel in ax.yaxis.get_ticklabels():
#                label.set_color('red')
#                label.set_rotation(45)
                yticklabel.set_fontsize(axisTickFontSize)
        else:
            formy = ticker.FuncFormatter(axisYFormatterFun)
            ax.yaxis.set_major_formatter(formy)        
                    
        formx = None
        if axisXFormatterFun == None:
            formx = plt.ScalarFormatter()
            formx.set_powerlimits((-3, 4))
            formx.set_scientific(True)
            ax.xaxis.set_major_formatter(formx)        
            for xticklabel in ax.xaxis.get_ticklabels():
#                label.set_color('red')
#                label.set_rotation(45)
                xticklabel.set_fontsize(axisTickFontSize)
        else:
            formx = ticker.FuncFormatter(axisXFormatterFun)
            ax.xaxis.set_major_formatter(formx)        
                                
        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_xlabel(xlabel, fontsize=axisFontSize)
        ax.set_ylabel(ylabel, fontsize=axisFontSize)
        ax.set_xlim(axisXLim)
        ax.set_ylim(axisYLim)
        ax.grid(axisGrid)
        if xticks == False:
            ax.set_xticks([])
        if yticks == False:
            ax.set_yticks([])
    
    return do_hist_from_file

def get_bar_from_file(csvName, xAxis, yAxes, yLabels,
                      annotations=[],
                      csvInts=(), csvFloats=(),
                      barEdgecolor='gray', barHisttype='bar', barAlpha=0.75,
                      barAlign='edge', barOrientation='vertical', barWidth=0.3,
                      barLog=False,
                      axisGrid=True, axisFontSize=10, axisTickFontSize=8, axisColor='k',
                      axisXLim=(None, None), axisYLim=(None, None),
                      axisXLabel='', axisYLabel='', axisTitle='',
                      axisXFormatterFun=lambda x: x, axisYFormatterFun=None,
                      legendFontsize=8, legendAlpha=0.8, legendShadow=False, legendColor='w',
                      legendFancybox=False, legendPos='upper right', legendCols=1, 
                      legendBorderPad=0.2, legendBorderAxesPad=0.0, legendLabelSpace=0.1, 
                      legendTop=True, legendTopAnchor=(0., 1.07, 1., .102),
                      myShareAxis=None, shareAxisX=None, shareAxisY=None):
    
    def do_bar_from_file(fig, numRows, numCols, figNum, axesDict):
            
        csvDict = csv_to_dict(csvName,
                              (xAxis,) + tuple([yAxis for (yAxis, _color, _hatch) in yAxes]),
                              ints=csvInts,
                              floats=csvFloats)

        xlabel = axisXLabel
        ylabel = axisYLabel
        xticks = True
        yticks = True
        if axisXLabel == None:
            xticks = False
            xlabel = ''
        if axisYLabel == None:
            yticks = False
            ylabel = ''

        sharex = None
        sharey = None
        if shareAxisX != None:
            sharex = axesDict[shareAxisX]
        if shareAxisY != None:
            sharey = axesDict[shareAxisY]

        ax = fig.add_subplot(numRows, numCols, figNum,
                             sharex=sharex, sharey=sharey)
        
        if myShareAxis != None:
            axesDict[myShareAxis] = ax                    
    
        n = max([len(csvDict[val]) for (val, _clr, _hatch) in yAxes])
        ind = np.arange(n)  # the x locations for the groups
        
        rectsColl = []
        barCount = -1    
        for (yAxis, barColor, barHatching) in yAxes:
            barCount += 1
                        
            rects = ax.bar(ind + (barWidth - barWidth * barCount), csvDict[yAxis], barWidth,
                           color=barColor, edgecolor=barEdgecolor, linewidth=None,
                           align=barAlign, log=barLog, hatch=barHatching)
            
            rectsColl += [rects]
        
        for annotation in annotations:
            annotation(ax)
            
        def autolabel(rects):
            # attach some text labels (Optional)
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
                        ha='center', va='bottom')
        
        # Uncomment to apply value labels to tops of bars
#        for rects in rectsColl:
#            autolabel(rects)
        
        legend = None
        
        if legendPos != None:            
            if legendTop == True:
                legend = ax.legend([rects[0] for rects in rectsColl],
                                   yLabels,
                                   'lower right',
                                   shadow=legendShadow,
                                   fancybox=legendFancybox,
                                   ncol=legendCols,
                                   bbox_to_anchor=(0., 1.07, 1., .102),
                                   mode="expand",
                                   borderpad=legendBorderPad,
                                   labelspacing=legendLabelSpace, 
                                   borderaxespad=legendBorderAxesPad
                                   )
            else:
                legend = ax.legend([rects[0] for rects in rectsColl],
                                   yLabels,
                                   legendPos,
                                   shadow=legendShadow,
                                   fancybox=legendFancybox,
                                   ncol=legendCols,
                                   borderpad=legendBorderPad,
                                   labelspacing=legendLabelSpace,
                                   borderaxespad=legendBorderAxesPad 
                                   )
                            
        
        if legend != None: 
            frame = legend.get_frame()  
            frame.set_facecolor(legendColor)
            frame.set_alpha(legendAlpha)
        
            for ltext in legend.get_texts():
                plb.setp(ltext, fontsize=legendFontsize)

        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_xlabel(xlabel, fontsize=axisFontSize)
        ax.set_ylabel(ylabel, fontsize=axisFontSize)
        ax.grid(axisGrid)
        
        barCount += 1
        ax.set_xticks(ind + ((3 - barCount) / 2.) * barWidth)
        
        ax.set_xticklabels([axisXFormatterFun(xLabel) for xLabel in csvDict[xAxis]])
        ax.set_xlim(axisXLim)
        ax.set_ylim(axisYLim)
        if xticks == False:
#            ax.set_xticks([])
            ax.set_xticklabels([])
        if yticks == False:
#            ax.set_yticks([])
            ax.set_xticklabels([])
        
#        for xticklabel in ax.xaxis.get_ticklabels():
#            xticklabel.set_rotation(45)
                
        formy = None
        if axisYFormatterFun == None:
            formy = plt.ScalarFormatter()
            formy.set_powerlimits((-3, 4))
            formy.set_scientific(True)
            ax.yaxis.set_major_formatter(formy)
            for yticklabel in ax.yaxis.get_ticklabels():
#                yticklabel.set_color('red')
#                yticklabel.set_rotation(45)
                yticklabel.set_fontsize(axisTickFontSize)
        else:
            formy = plt.FuncFormatter(axisYFormatterFun)
            ax.yaxis.set_major_formatter(formy)        


    return do_bar_from_file

def get_barh_from_file(csvName, baseAxis, valuesColl, labels, annotations=[],
                       csvInts=(), csvFloats=(),
                       barEdgecolor='gray', barHisttype='bar', barAlpha=0.75,
                       barAlign='edge', barOrientation='vertical', barHeight=0.3,
                       barLog=False, barReverse=False,
                       axisGrid=True, axisFontSize=12, axisTickFontSize=12, axisColor='k',
                       axisXLim=(None, None), axisYLim=(None, None),
                       axisXLabel='', axisYLabel='', axisTitle='',
                       axisXFormatterFun=None, axisYFormatterFun=lambda x: x,
                       legendFontsize=8, legendAlpha=0.8, legendShadow=False, legendColor='w',                       
                       legendFancybox=False, legendPos='upper right', legendCols=1, legendTop=True,
                       legendBorderPad=0.1, legendLabelSpace=0.1, legendBorderAxesPad=0.0,
                       myShareAxis=None, shareAxisX=None, shareAxisY=None):
    
    def do_barh_from_file(fig, numRows, numCols, figNum, axesDict):
            
        csvDict = csv_to_dict(csvName,
                              (baseAxis,) + tuple([values for (values, _color) in valuesColl]),
                              ints=csvInts,
                              floats=csvFloats)

        xlabel = axisXLabel
        ylabel = axisYLabel
        xticks = True
        yticks = True
        if axisXLabel == None:
            xticks = False
            xlabel = ''
        if axisYLabel == None:
            yticks = False
            ylabel = ''

        sharex = None
        sharey = None
        if shareAxisX != None:
            sharex = axesDict[shareAxisX]
        if shareAxisY != None:
            sharey = axesDict[shareAxisY]

        ax = fig.add_subplot(numRows, numCols, figNum,
                             sharex=sharex, sharey=sharey)
        
        if myShareAxis != None:
            axesDict[myShareAxis] = ax                    
    
        n = max([len(csvDict[val]) for (val, clr) in valuesColl])
        ind = np.arange(n)  # the y locations for the groups    
    
        rectsColl = []
        barCount = -1    
        for (values, barColor) in valuesColl:
            barCount += 1
            
            maybeReversedVals = csvDict[values]
            if barReverse == True:
                maybeReversedVals = [value for value in reversed(csvDict[values])]
            
            rects = ax.barh(ind + (barHeight - barHeight * barCount), maybeReversedVals, barHeight,
                            color=barColor, edgecolor=barEdgecolor, linewidth=None,
                            align=barAlign, log=barLog)
            
            rectsColl += [rects]
        
        for annotation in annotations:
            annotation(ax)
            
        def autolabel(rects):
            maxWidth = max([rect.get_width() for rect in rects])
            for rect in rects:
                width = rect.get_width()
                x = width + maxWidth * 0.02
                y = rect.get_y() + rect.get_height() / 2.
                print x, y, width
                ax.text(x, y, '%d' % int(width),
                        ha='left', va='center')
        
        # Attach some text labels (Optional)
        # Uncomment to apply value labels to tops of bars
#        autolabel(rects)

        legend = None
        
        if legendPos != None:            
            if legendTop == True:
                legend = ax.legend([rects[0] for rects in rectsColl],
                                   labels,
                                   'lower left',
                                   shadow=legendShadow,
                                   fancybox=legendFancybox,
                                   ncol=legendCols,
                                   bbox_to_anchor=(0., 1.05, 1., .102),
                                   mode="expand",
                                   borderpad=legendBorderPad,
                                   labelspacing=legendLabelSpace, 
                                   borderaxespad=legendBorderAxesPad
                                   )
            else:
                legend = ax.legend([rects[0] for rects in rectsColl],
                                   labels,
                                   legendPos,
                                   shadow=legendShadow,
                                   fancybox=legendFancybox,
                                   ncol=legendCols)
        
        
        if legend != None: 
            frame = legend.get_frame()  
            frame.set_facecolor(legendColor)
            frame.set_alpha(legendAlpha)
        
            for ltext in legend.get_texts():
                plb.setp(ltext, fontsize=legendFontsize)

        formx = None
        if axisXFormatterFun == None:
            formx = plt.ScalarFormatter()
            formx.set_powerlimits((-3, 4))
            formx.set_scientific(True)
            ax.xaxis.set_major_formatter(formx)
            for xticklabel in ax.xaxis.get_ticklabels():
#                label.set_color('red')
#                label.set_rotation(45)
                xticklabel.set_fontsize(axisTickFontSize)
        else:
            formx = ticker.FuncFormatter(axisXFormatterFun)
            ax.xaxis.set_major_formatter(formx)                
                    
        ax.set_title(axisTitle, fontsize=axisFontSize)
        ax.set_xlabel(xlabel, fontsize=axisFontSize)
        ax.set_ylabel(ylabel, fontsize=axisFontSize)
        ax.grid(axisGrid)
        ax.set_yticks(ind + barHeight)        
        
        tempYLabels = [axisYFormatterFun(yLabel) for yLabel in csvDict[baseAxis]]
        if barReverse == True:
            tempYLabels = [axisYFormatterFun(yLabel) for yLabel in reversed(csvDict[baseAxis])]            
        ax.set_yticklabels(tempYLabels)        
        
        ax.set_xlim(axisXLim)
        ax.set_ylim(axisYLim)
        if yticks == False:
            ax.set_yticks([])
            ax.set_yticklabels([])
        if xticks == False:
            ax.set_xticks([])

    return do_barh_from_file

def get_img_from_file(imgFile, annotations=[]):

    def do_img_from_file(fig, numRows, numCols, figNum, _axesDict):
        
        ax = fig.add_subplot(numRows, numCols, figNum)
                
        img = Image.open(imgFile)
#        ax.set_axes([0, 0, 1, 1], frameon=False)
        ax.set_axis_off()
        ax.imshow(img, origin='lower')
    
    return do_img_from_file
