from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *
import numpy

defBarWidth = 0.2

defFigWidthAll = 9.0
defFigHeightAll = 9.0
defFigLeftSpaceAll = 0.17
defFigBottomSpaceAll = 0.06
defFigRightSpaceAll = 0.98
defFigTopSpaceAll = 0.84

defFigWidthOne = 6.0
defFigHeightOne = 5.0
defFigLeftSpaceOne = 0.22
defFigBottomSpaceOne = 0.19
defFigRightSpaceOne = 0.92
defFigTopSpaceOne = 0.93

def gis_load_balance_all_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long5_short95_balance.csv"
    
    legends = [r'Hardcoded 2',
               r'DiDiC 2',
               r'Random 2']
    
    barWidth = defBarWidth / 3.0
    
    load_balance_all(csvFile, legends,
                     fileName="gis2_bal_all.pdf",
                     horizontalLineY=50,
                     barWidth=barWidth)

def gis_load_balance_all_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long5_short95_balance.csv"
    
    legends = [r'Hardcoded 4',
               r'DiDiC 4',
               r'Random 4']
    
    barWidth = defBarWidth
    
    load_balance_all(csvFile, legends,
                     fileName="gis4_bal_all.pdf",
                     horizontalLineY=25,
                     barWidth=barWidth)

def gis_traf():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/"
    csvFile = csvFolder + "gis_traffic.csv"     
    
    fileName = "gis_traf.pdf"
    
    traf(csvFile,
         legendName='GIS Traffic',
         fileName=fileName,
         figLeftSpace=0.20,
         figRightSpace=0.91)

def gis_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long5_short95_gtraf.csv"
         
    glratio(csvFile,
            legendNameHard='Hardcoded 2',
            legendNameDiDiC='DiDiC 2',
            legendNameRand='Random 2',
            fileName='gis2_g_l_traf.pdf')

def gis_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long5_short95_gtraf.csv"
         
    glratio(csvFile,
            legendNameHard='Hardcoded 4',
            legendNameDiDiC='DiDiC 4',
            legendNameRand='Random 4',
            fileName='gis4_g_l_traf.pdf')



def fstree_load_balance_all_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree2_search_balance.csv" 
    
    legends = [r'Hardcoded 2',
               r'DiDiC 2',
               r'Random 2']
    
    barWidth = defBarWidth / 3.0
    
    load_balance_all(csvFile, legends,
                     fileName="fstree2_bal_all.pdf",
                     horizontalLineY=50,
                     barWidth=barWidth)

def fstree_load_balance_all_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree4_search_balance.csv" 
    
    legends = [r'Hardcoded 4',
               r'DiDiC 4',
               r'Random 4']
    
    barWidth = defBarWidth
    
    load_balance_all(csvFile, legends,
                     fileName="fstree4_bal_all.pdf",
                     horizontalLineY=25,
                     barWidth=barWidth)

def fstree_traf():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/"
    csvFile = csvFolder + "fstree_traffic.csv"     
    
    fileName = "fstree_traf.pdf"
    
    traf(csvFile,
         legendName='FS-Tree Traffic',
         fileName=fileName,
         figLeftSpace=0.20,
         figRightSpace=0.91)        

def fstree_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree2_search_gtraf.csv"     
    
    glratio(csvFile,
            legendNameHard='Hardcoded 2',
            legendNameDiDiC='DiDiC 2',
            legendNameRand='Random 2',
            fileName='fstree2_g_l_traf.pdf',
            axisYLimUpper=None)

def fstree_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree4_search_gtraf.csv"     
    
    glratio(csvFile,
            legendNameHard='Hardcoded 4',
            legendNameDiDiC='DiDiC 4',
            legendNameRand='Random 4',
            fileName='fstree4_g_l_traf.pdf',
            axisYLimUpper=0.40)



def twitter_load_balance_all_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter2_balance.csv" 
    
    legends = [r'Hardcoded 2',
               r'DiDiC 2',
               r'Random 2']
    
    barWidth = defBarWidth / 3.0
    
    load_balance_all(csvFile, legends,
                     fileName="twitter2_bal_all.pdf",
                     horizontalLineY=50,
                     barWidth=barWidth)

def twitter_load_balance_all_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter4_balance.csv" 
    
    legends = [r'Hardcoded 4',
               r'DiDiC 4',
               r'Random 4']
    
    barWidth = defBarWidth
    
    load_balance_all(csvFile, legends,
                     fileName="twitter4_bal_all.pdf",
                     horizontalLineY=25,
                     barWidth=barWidth)

def twitter_traf():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/"
    csvFile = csvFolder + "twitter_traffic.csv"     
    
    fileName = "twitter_traf.pdf"
    
    traf(csvFile,
         legendName='Twitter Traffic',
         fileName=fileName,
         figLeftSpace=0.20,
         figRightSpace=0.91)        
    
def twitter_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter2_gtraf.csv"     
    
    glratio(csvFile,
            legendNameHard='Hardcoded 2',
            legendNameDiDiC='DiDiC 2',
            legendNameRand='Random 2',
            fileName='twitter2_g_l_traf.pdf',
            axisYLimUpper=None,
            csvColumnGLtrafHard=None)

def twitter_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter4_gtraf.csv"     
    
    glratio(csvFile,
            legendNameHard='Hardcoded 4',
            legendNameDiDiC='DiDiC 4',
            legendNameRand='Random 4',
            fileName='twitter4_g_l_traf.pdf',
            axisYLimUpper=None,
            csvColumnGLtrafHard=None)



def load_balance_all(csvFile, legends,
                     fileName='output_bal_all.pdf',
                     legendAlpha=0.8,
                     horizontalLineY=50,
                     barWidth=defBarWidth,
                     axisGrid=False,
                     figLeftSpace=defFigLeftSpaceAll,
                     figBottomSpace=defFigBottomSpaceAll,
                     figRightSpace=defFigRightSpaceAll,
                     figTopSpace=defFigTopSpaceAll,
                     figWidth=defFigWidthAll,
                     figHeight=defFigHeightAll,
                     legendFontsize=8,
                     legendBorderPad=0.3,
                     axisYLimRel=(0, None),
                     axisYLimNode=(0, None),
                     axisYLimTraf=(0, None)
                 ):
    
    csvColumnPartition = "partitions"
    
    csvColumnRelsHard = "rels_hard"
    csvColumnRelsDiDiC = "rels_didic"
    csvColumnRelsRand = "rels_rand"
    
    csvColumnNodesHard = "nodes_hard"
    csvColumnNodesDiDiC = "nodes_didic"
    csvColumnNodesRand = "nodes_rand"
    
    csvColumnTrafHard = "traf_hard"
    csvColumnTrafDiDiC = "traf_didic"
    csvColumnTrafRand = "traf_rand"    
        
    def do_annotation_avg_gltraf(ax):
        ax.axhline(y=horizontalLineY, linewidth=1, color='black', alpha=1.0, linestyle='--')
    
    annotations = []
    if horizontalLineY != None:
        annotations = [do_annotation_avg_gltraf]    

    def axisYFormatterFun(x, pos=0):
        return '%3d\,%s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s' % (x)    
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsHard, 'blue', None),
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        ],
                                        legends,
                                        csvFloats=(
                                                   csvColumnRelsHard,
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand,
                                                   ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=False,
                                         axisGrid=axisGrid, axisColor='k',
                                         axisYLabel=r'Edges', axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=axisYLimRel,
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendFontsize=legendFontsize, legendBorderPad=legendBorderPad,
                                         legendColor='w', legendFancybox=False, legendPos='upper right',
                                         legendCols=1,
                                         )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesHard, 'blue', None),
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
                                         ],
                                         [],
                                         csvFloats=(
                                                    csvColumnNodesHard,
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=False,
                                         axisGrid=axisGrid, axisColor='k',
                                         axisYLabel=r'Vertices', axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=axisYLimNode,
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendFontsize=legendFontsize, legendBorderPad=legendBorderPad,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafHard, 'blue', None),
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
                                         ],
                                         [],
                                         csvFloats=(
                                                    csvColumnTrafHard,
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=False,
                                         axisGrid=axisGrid, axisColor='k',
                                         axisYLabel=r'Traffic',
                                         axisYFormatterFun=axisYFormatterFun,
                                         axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=axisYLimTraf,
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendFontsize=legendFontsize, legendBorderPad=legendBorderPad,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    
    figSize = (figWidth / 2.54, figHeight / 2.54)

    show_plots([[do_rel_bal_bar],
                [do_node_bal_bar],
                [do_traf_bal_bar]],
                show=False,
                fileName=fileName,
                figWSpace=0.2,
                figHSpace=0.2,
                figLeftSpace=figLeftSpace,
                figRightSpace=figRightSpace,
                figBottomSpace=figBottomSpace,
                figTopSpace=figTopSpace,
                figSize=figSize)

def traf(csvFile,
         legendName='Traffic',
         fileName='output_traf.pdf',
         figLeftSpace=defFigLeftSpaceOne,
         figBottomSpace=defFigBottomSpaceOne,
         figRightSpace=defFigRightSpaceOne,
         figTopSpace=defFigTopSpaceOne,
         figWidth=defFigWidthOne,
         figHeight=defFigHeightOne):
    
    csvColumnIndex = "index"    
    csvColumnTraf = "traffic"

    def axisYFormatterFun(x, pos=0):
        return '%3d\,%s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f\,%s' % ((float(x) / 10000.) * 100., '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnIndex, csvColumnTraf, 'blue', legendName, '-', '')],
                                        csvInts=(csvColumnTraf),
                                        annotations=[],
                                        axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                        axisColor='k',
                                        axisXLabel=r'Operations', axisYLabel=r'Traffic',
                                        axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right', legendTop=False,
                                        legendBorderPad=0.3, legendLabelSpace=0.1,
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    figSize = (figWidth / 2.54, figHeight / 2.54)
    
    show_plots([[do_fun]],
                show=False,
                fileName=fileName,
                figWSpace=0.2,
                figHSpace=0.2,
                figLeftSpace=figLeftSpace,
                figRightSpace=figRightSpace,
                figBottomSpace=figBottomSpace,
                figTopSpace=figTopSpace,
                figSize=figSize)                
    
def glratio(csvFile,
            legendNameHard='Hardcoded 2',
            legendNameDiDiC='DiDiC 2',
            legendNameRand='Random 2',
            axisYLimUpper=None,
            fileName='output_g_l_traf.pdf',
            figLeftSpace=defFigLeftSpaceOne,
            figBottomSpace=defFigBottomSpaceOne,
            figRightSpace=defFigRightSpaceOne,
            figTopSpace=defFigTopSpaceOne,
            figWidth=defFigWidthOne,
            figHeight=defFigHeightOne,
            csvColumnGLtrafHard="g_l_hard",
            csvColumnGLtrafDiDiC="g_l_didic",
            csvColumnGLtrafRand="g_l_rand",
            csvColumnIndex="index"):     
    
    baseLines = [(csvColumnIndex, csvColumnGLtrafHard, 'blue', legendNameHard, '-', ''),
                 (csvColumnIndex, csvColumnGLtrafDiDiC, 'red', legendNameDiDiC, '-', ''),
                 (csvColumnIndex, csvColumnGLtrafRand, 'green', legendNameRand, '-', '')]
    
    lines = [(x, y, color, legend, lineType, markerType) for 
             (x, y, color, legend, lineType, markerType) in baseLines 
             if y != None]
    
    csvFloats = [y for (_, y, _, _, _, _) in lines if y != None] + [csvColumnIndex]
    
    csvDict = csv_to_dict(csvFile,
                          (csvColumnGLtrafHard, csvColumnGLtrafDiDiC, csvColumnGLtrafRand),
                          floats=tuple(csvFloats))

    def get_do_annotation_avg_gltraf(column, color):
        def do_annotation_avg_gltraf(ax):
            ax.axhline(y=numpy.mean(csvDict[column]),
                       linewidth=1, color=color, alpha=1.0, linestyle='--')
        return do_annotation_avg_gltraf
    
    def get_do_annotation_std_gltraf(column, color):
        def do_annotation_std_gltraf(ax):
            std_low = numpy.min(numpy.mean(csvDict[column]) - numpy.std(csvDict[column]), 0)
            std_high = numpy.max(numpy.mean(csvDict[column]) + numpy.std(csvDict[column]), 100)
#            ax.axhline(y=std_low,
#                       linewidth=1, color=color, alpha=1.0, linestyle='--')
#            ax.axhline(y=std_high,
#                       linewidth=1, color=color, alpha=1.0, linestyle='--')
#            ax.axhspan(std_low, std_high, facecolor=color, alpha=0.3)            
        return do_annotation_std_gltraf

    
    annotations = []    
    for (column, color) in [(column, color) 
                            for (_, column, color, _, _, _) in lines 
                            if y != None]:
        annotations += [get_do_annotation_avg_gltraf(column, color)]
    
    for (column, color) in [(column, color) 
                            for (_, column, color, _, _, _) in lines 
                            if y != None]:    
        annotations += [get_do_annotation_std_gltraf(column, color)]

        
    def axisYFormatterFun(x, pos=0):        
        return '%3d\,%s' % (x * 100., '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d\,%s' % ((float(x) / 10000.) * 100., '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        lines,
                                        csvFloats=csvFloats,
                                        annotations=annotations,
                                        axisLineWidth=1.0, axisGrid=False, axisLineAntialiased=True,
                                        axisColor='k',
                                        axisXLabel=r'Operations', axisYLabel=r'Percentage Global',
                                        axisTitle='', axisXLim=(-1, None), axisYLim=(0, axisYLimUpper),
                                        axisXFormatterFun=axisXFormatterFun,
                                        axisYFormatterFun=axisYFormatterFun,
                                        axisXScale='linear', axisYScale='linear',
                                        legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right', legendTop=False,
                                        legendBorderPad=0.3, legendLabelSpace=0.1,
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    figSize = (figWidth / 2.54, figHeight / 2.54)
    
    show_plots([[do_fun]],
                show=False,
                fileName=fileName,
                figWSpace=0.2,
                figHSpace=0.2,
                figLeftSpace=figLeftSpace,
                figRightSpace=figRightSpace,
                figBottomSpace=figBottomSpace,
                figTopSpace=figTopSpace,
                figSize=figSize)
