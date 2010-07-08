from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

fontsizeLabels = r'\LARGE '
fontsizeTicks = r'\Large '
fontsizeLegend = r'\Large '
axisTickFontSize = 16
barWidth = 0.2

def gis_long5_short95_load_balance_all_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long5_short95_balance.csv"
     
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
    
    legendAlpha = 0.8 
    maxY = 100
    reducedBarWidth = barWidth / 3.0
    axisGrid = False
    
    def do_annotation_avg_gltraf(ax):
        ax.axhline(y=50, linewidth=1, color='black', alpha=1.0, linestyle='--')
    
    annotations = [do_annotation_avg_gltraf]    

    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsHard, 'blue', None),
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        ],
                                        [
                                         fontsizeLegend + r'Hardcoded 2',
                                         fontsizeLegend + r'DiDiC 2',
                                         fontsizeLegend + r'Random 2',
                                         ],
                                         csvFloats=(
                                                    csvColumnRelsHard,
                                                    csvColumnRelsDiDiC,
                                                    csvColumnRelsRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Edges', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right',
                                         legendCols=3,
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
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Vertices', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
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
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    show_plots([
                [do_rel_bal_bar],
                [do_node_bal_bar],
                [do_traf_bal_bar]],
                show=False,
                figHSpace=0.3,
                fileName="gis2_bal_all.pdf")

def gis_long5_short95_load_balance_all_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long5_short95_balance.csv"
     
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
    
    legendAlpha = 0.8 
    maxY = 50
    reducedBarWidth = barWidth
    axisGrid = False
    
    def do_annotation_avg_gltraf(ax):
        ax.axhline(y=25, linewidth=1, color='black', alpha=1.0, linestyle='--')
    
    annotations = [do_annotation_avg_gltraf]
        
    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsHard, 'blue', None),
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        ],
                                        [
                                         fontsizeLegend + r'Hardcoded 4',
                                         fontsizeLegend + r'DiDiC 4',
                                         fontsizeLegend + r'Random 4',
                                         ],
                                         csvFloats=(
                                                    csvColumnRelsHard,
                                                    csvColumnRelsDiDiC,
                                                    csvColumnRelsRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Edges', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right',
                                         legendCols=3,
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
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Vertices', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
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
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    show_plots([
                [do_rel_bal_bar],
                [do_node_bal_bar],
                [do_traf_bal_bar]],
                show=False,
                figHSpace=0.3,
                fileName="gis4_bal_all.pdf")

def gis_traf():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/"
    csvFile = csvFolder + "gis_traffic.csv"     
    
    csvColumnIndex = "index"    
    csvColumnTraf = "traffic"

    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
    do_fstree2_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                               [(csvColumnTraf, 'blue', fontsizeLegend + r'Traffic', '-', ''), ],
                                                csvInts=(csvColumnTraf),
                                                annotations=[],
                                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                axisTickFontSize=axisTickFontSize, axisColor='k',
                                                axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Traffic',
                                                axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                                axisXFormatterFun=None, axisYFormatterFun=None,
                                                axisXScale='linear', axisYScale='log',
                                                legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                legendFancybox=False, legendPos='upper right',
                                                myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree2_gtraf_line]],
                show=False,
                fileName="gis_traf.pdf")

def gis_long5_short95_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long5_short95_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            fontsizeLegend + r'DiDiC 2',
                                            fontsizeLegend + r'Random 2',
                                            fontsizeLegend + r'Hardcoded 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                            barLog=True,
                                            axisGrid=True, axisTickFontSize=axisTickFontSize, axisColor='k',
                                            axisYLabel=fontsizeLabels + r'Percentage of Operations',
                                            axisXLabel=fontsizeLabels + r'Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="gis2_long5_short95_perc_gtraf.pdf")

def gis_long5_short95_perc_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long5_short95_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            fontsizeLegend + r'DiDiC 4',
                                            fontsizeLegend + r'Random 4',
                                            fontsizeLegend + r'Hardcoded 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                            barLog=True,
                                            axisGrid=True, axisTickFontSize=axisTickFontSize, axisColor='k',
                                            axisYLabel=fontsizeLabels + r'Percentage of Operations',
                                            axisXLabel=fontsizeLabels + r'Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="gis4_long5_short95_perc_gtraf.pdf")

def gis_long5_short95_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long5_short95_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    csvFileAnnotate = csvFolder + "gis2_long5_short95_gtraf.csv"
    csvColumnGLAvgHard = "g_l_avg_hard"
    csvColumnGLAvgDiDiC = "g_l_avg_didic"
    csvColumnGLAvgRand = "g_l_avg_rand"
    
    csvDict = csv_to_dict(csvFileAnnotate,
                          (csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand),
                          floats=(csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand))

    def get_do_annotation_avg_gltraf(column, color):
        def do_annotation_avg_gltraf(ax):
            ax.axhline(y=csvDict[column][0], linewidth=1, color=color, alpha=1.0, linestyle='--')
        return do_annotation_avg_gltraf
    
    annotations = []    
    for (column, color) in ((csvColumnGLAvgHard, 'blue'),
                           (csvColumnGLAvgDiDiC, 'red'),
                           (csvColumnGLAvgRand, 'green')):    
        annotations += [get_do_annotation_avg_gltraf(column, color)]
        
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    def axisYFormatterFun(x, pos=0):        
        return '%s%3d %s' % (fontsizeTicks, x * 100., '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', fontsizeLegend + r'Hardcoded 2', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', fontsizeLegend + r'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', fontsizeLegend + r'Random 2', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=annotations,
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisTickFontSize=axisTickFontSize, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Percentage Global',
                                          axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                          axisXScale='linear', axisYScale='linear',
                                          legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="gis2_long5_short95_g_l_traf.pdf")

def gis_long5_short95_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long5_short95_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    csvFileAnnotate = csvFolder + "gis2_long5_short95_gtraf.csv"
    csvColumnGLAvgHard = "g_l_avg_hard"
    csvColumnGLAvgDiDiC = "g_l_avg_didic"
    csvColumnGLAvgRand = "g_l_avg_rand"
    
    csvDict = csv_to_dict(csvFileAnnotate,
                          (csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand),
                          floats=(csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand))

    def get_do_annotation_avg_gltraf(column, color):
        def do_annotation_avg_gltraf(ax):
            ax.axhline(y=csvDict[column][0], linewidth=1, color=color, alpha=1.0, linestyle='--')
        return do_annotation_avg_gltraf
    
    annotations = []    
    for (column, color) in ((csvColumnGLAvgHard, 'blue'),
                           (csvColumnGLAvgDiDiC, 'red'),
                           (csvColumnGLAvgRand, 'green')):    
        annotations += [get_do_annotation_avg_gltraf(column, color)]

#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    def axisYFormatterFun(x, pos=0):        
        return '%s%3d %s' % (fontsizeTicks, x * 100., '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', fontsizeLegend + r'Hardcoded 4', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', fontsizeLegend + r'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', fontsizeLegend + r'Random 4', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=annotations,
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisTickFontSize=axisTickFontSize, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Percentage Global',
                                          axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                          axisXScale='linear', axisYScale='linear',
                                          legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="gis4_long5_short95_g_l_traf.pdf")




def fstree_search_load_balance_all_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree2_search_balance.csv" 
    
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
    
    legendAlpha = 0.8 
    maxY = 100
    reducedBarWidth = barWidth / 3.0
    axisGrid = False
    
    def do_annotation_avg_gltraf(ax):
        ax.axhline(y=50, linewidth=1, color='black', alpha=1.0, linestyle='--')
    
    annotations = [do_annotation_avg_gltraf]    

    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_fstree2_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                               [(csvColumnRelsHard, 'blue', None),
                                                (csvColumnRelsDiDiC, 'red', None),
                                                (csvColumnRelsRand, 'green', None)],
                                                [
                                                 fontsizeLegend + r'Hardcoded 2',
                                                 fontsizeLegend + r'DiDiC 2',
                                                 fontsizeLegend + r'Random 2',
                                                 ],
                                                csvFloats=(csvColumnRelsHard,
                                                           csvColumnRelsDiDiC,
                                                           csvColumnRelsRand),
                                                annotations=annotations,
                                                barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                                barLog=True,
                                                axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                                axisYLabel=fontsizeLabels + r'Edges', # axisXLabel=None,
                                                axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                                axisYLim=(0, maxY),
                                                legendAlpha=legendAlpha, legendShadow=False,
                                                legendColor='w', legendFancybox=False, legendPos='upper right',
                                                legendCols=3,
                                                )
    
    do_fstree2_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnNodesHard, 'blue', None),
                                                 (csvColumnNodesDiDiC, 'red', None),
                                                 (csvColumnNodesRand, 'green', None)],
                                                 [
#                                                  fontsizeLegend + r'Hardcoded 2',
#                                                  fontsizeLegend + r'DiDiC 2',
#                                                  fontsizeLegend + r'Random 2',
                                                  ],
                                                 csvFloats=(csvColumnNodesHard,
                                                            csvColumnNodesDiDiC,
                                                            csvColumnNodesRand),
                                                 annotations=annotations,
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                                 barLog=True,
                                                 axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                                 axisYLabel=fontsizeLabels + r'Vertices', # axisXLabel=None,
                                                 axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                                 axisYLim=(0, maxY),
                                                 legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos=None
                                                 )
    
    do_fstree2_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnTrafHard, 'blue', None),
                                                 (csvColumnTrafDiDiC, 'red', None),
                                                 (csvColumnTrafRand, 'green', None)],
                                                 [
#                                                  fontsizeLegend + r'Hardcoded 2',
#                                                  fontsizeLegend + r'DiDiC 2',
#                                                  fontsizeLegend + r'Random 2',
                                                  ],
                                                 csvFloats=(csvColumnTrafHard,
                                                            csvColumnTrafDiDiC,
                                                            csvColumnTrafRand),
                                                 annotations=annotations,
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                                 barLog=True,
                                                 axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                                 axisYLabel=fontsizeLabels + r'Traffic',
                                                 axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                                 axisYLim=(0, maxY),
                                                 legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos=None
                                                 )
    
    show_plots([
                [do_fstree2_rel_bal_bar],
                [do_fstree2_node_bal_bar],
                [do_fstree2_traf_bal_bar]],
                show=False,
                figHSpace=0.3,
                fileName="fstree2_bal_all.pdf")

def fstree_search_load_balance_all_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree4_search_balance.csv" 
    
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
    
    legendAlpha = 0.8 
    maxY = 50
    axisGrid = False
        
    def do_annotation_avg_gltraf(ax):
        ax.axhline(y=25, linewidth=1, color='black', alpha=1.0, linestyle='--')
    
    annotations = [do_annotation_avg_gltraf]
        
    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_fstree4_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                               [(csvColumnRelsHard, 'blue', None),
                                                (csvColumnRelsDiDiC, 'red', None),
                                                (csvColumnRelsRand, 'green', None)],
                                                [
                                                 fontsizeLegend + r'Hardcoded 4',
                                                 fontsizeLegend + r'DiDiC 4',
                                                 fontsizeLegend + r'Random 4',
                                                 ],
                                                csvFloats=(csvColumnRelsHard,
                                                           csvColumnRelsDiDiC,
                                                           csvColumnRelsRand),
                                                annotations=annotations,
                                                barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                                barLog=True,
                                                axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                                axisYLabel=fontsizeLabels + r'Edges', # axisXLabel=None,
                                                axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                                axisYLim=(0, maxY),
                                                legendAlpha=legendAlpha, legendShadow=False,
                                                legendColor='w', legendFancybox=False, legendPos='upper right',
                                                legendCols=3,
                                                )
    
    do_fstree4_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnNodesHard, 'blue', None),
                                                 (csvColumnNodesDiDiC, 'red', None),
                                                 (csvColumnNodesRand, 'green', None)],
                                                 [
                                                  fontsizeLegend + r'Hardcoded 4',
                                                  fontsizeLegend + r'DiDiC 4',
                                                  fontsizeLegend + r'Random 4',
                                                  ],
                                                 csvFloats=(csvColumnNodesHard,
                                                            csvColumnNodesDiDiC,
                                                            csvColumnNodesRand),
                                                 annotations=annotations,
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                                 barLog=True,
                                                 axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                                 axisYLabel=fontsizeLabels + r'Vertices', # axisXLabel=None,
                                                 axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                                 axisYLim=(0, maxY),
                                                 legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos=None
                                                 )
    
    do_fstree4_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnTrafHard, 'blue', None),
                                                 (csvColumnTrafDiDiC, 'red', None),
                                                 (csvColumnTrafRand, 'green', None)],
                                                 [
#                                                  fontsizeLegend + r'Hardcoded 4',
#                                                  fontsizeLegend + r'DiDiC 4',
#                                                  fontsizeLegend + r'Random 4',
                                                  ],
                                                 csvFloats=(csvColumnTrafHard,
                                                            csvColumnTrafDiDiC,
                                                            csvColumnTrafRand),
                                                 annotations=annotations,
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                                 barLog=True,
                                                 axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                                 axisYLabel=fontsizeLabels + r'Traffic',
                                                 axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                                 axisYLim=(0, maxY),
                                                 legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos=None
                                                 )
    
    show_plots([
                [do_fstree4_rel_bal_bar],
                [do_fstree4_node_bal_bar],
                [do_fstree4_traf_bal_bar]],
                show=False,
                figHSpace=0.3,
                fileName="fstree4_bal_all.pdf")

def fstree_traf():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/"
    csvFile = csvFolder + "fstree_traffic.csv"     
    
    csvColumnIndex = "index"    
    csvColumnTraf = "traffic"

    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
    do_fstree2_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                               [(csvColumnTraf, 'blue', fontsizeLegend + r'Traffic', '-', ''), ],
                                                csvInts=(csvColumnTraf),
                                                annotations=[],
                                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                axisTickFontSize=axisTickFontSize, axisColor='k',
                                                axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Traffic',
                                                axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                                axisXFormatterFun=None, axisYFormatterFun=None,
                                                axisXScale='linear', axisYScale='log',
                                                legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                legendFancybox=False, legendPos='upper right',
                                                myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree2_gtraf_line]],
                show=False,
                fileName="fstree_traf.pdf")

def fstree_search_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree2_search_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    
    csvColumnSearchHard = "hard"
    csvColumnSearchDiDiC = "didic"
    csvColumnSearchRand = "rand"
        
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
                            
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnSearchDiDiC, 'red', None),
                                           (csvColumnSearchRand, 'green', None),
                                           (csvColumnSearchHard, 'blue', None),
                                           ],
                                           [
                                            fontsizeLegend + r'DiDiC 2',
                                            fontsizeLegend + r'Random 2',
                                            fontsizeLegend + r'Hardcoded 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnSearchDiDiC,
                                                       csvColumnSearchRand,
                                                       csvColumnSearchHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                            barLog=True,
                                            axisGrid=True, axisTickFontSize=axisTickFontSize, axisColor='k',
                                            axisYLabel=fontsizeLabels + r'Percentage of Operations',
                                            axisXLabel=fontsizeLabels + r'Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="fstree2_search_perc_gtraf.pdf")

def fstree_search_perc_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree4_search_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnSearchHard = "hard"
    csvColumnSearchDiDiC = "didic"
    csvColumnSearchRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
                            
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnSearchDiDiC, 'red', None),
                                           (csvColumnSearchRand, 'green', None),
                                           (csvColumnSearchHard, 'blue', None),
                                           ],
                                           [
                                            fontsizeLegend + r'DiDiC 4',
                                            fontsizeLegend + r'Random 4',
                                            fontsizeLegend + r'Hardcoded 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnSearchDiDiC,
                                                       csvColumnSearchRand,
                                                       csvColumnSearchHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                            barLog=True,
                                            axisGrid=True, axisTickFontSize=axisTickFontSize, axisColor='k',
                                            axisYLabel=fontsizeLabels + r'Percentage of Operations',
                                            axisXLabel=fontsizeLabels + 'Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="fstree4_search_perc_gtraf.pdf")

def fstree_search_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree2_search_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    csvFileAnnotate = csvFolder + "tree2_search_gtraf.csv"
    csvColumnGLAvgHard = "g_l_avg_hard"
    csvColumnGLAvgDiDiC = "g_l_avg_didic"
    csvColumnGLAvgRand = "g_l_avg_rand"
    
    csvDict = csv_to_dict(csvFileAnnotate,
                          (csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand),
                          floats=(csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand))

    def get_do_annotation_avg_gltraf(column, color):
        def do_annotation_avg_gltraf(ax):
            ax.axhline(y=csvDict[column][0], linewidth=1, color=color, alpha=1.0, linestyle='--')
        return do_annotation_avg_gltraf
    
    annotations = []    
    for (column, color) in ((csvColumnGLAvgHard, 'blue'),
                           (csvColumnGLAvgDiDiC, 'red'),
                           (csvColumnGLAvgRand, 'green')):    
        annotations += [get_do_annotation_avg_gltraf(column, color)]
        
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    def axisYFormatterFun(x, pos=0):        
        return '%s%3d %s' % (fontsizeTicks, x * 100., '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', fontsizeLegend + r'Hardcoded 2', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', fontsizeLegend + r'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', fontsizeLegend + r'Random 2', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=annotations,
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisTickFontSize=axisTickFontSize, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Percentage Global',
                                          axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                          axisXScale='linear', axisYScale='linear',
                                          legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="fstree2_search_g_l_traf.pdf")

def fstree_search_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree4_search_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    csvFileAnnotate = csvFolder + "tree4_search_gtraf.csv"
    csvColumnGLAvgHard = "g_l_avg_hard"
    csvColumnGLAvgDiDiC = "g_l_avg_didic"
    csvColumnGLAvgRand = "g_l_avg_rand"
    
    csvDict = csv_to_dict(csvFileAnnotate,
                          (csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand),
                          floats=(csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand))

    def get_do_annotation_avg_gltraf(column, color):
        def do_annotation_avg_gltraf(ax):
            ax.axhline(y=csvDict[column][0], linewidth=1, color=color, alpha=1.0, linestyle='--')
        return do_annotation_avg_gltraf
    
    annotations = []    
    for (column, color) in ((csvColumnGLAvgHard, 'blue'),
                           (csvColumnGLAvgDiDiC, 'red'),
                           (csvColumnGLAvgRand, 'green')):    
        annotations += [get_do_annotation_avg_gltraf(column, color)]
    
    def axisYFormatterFun(x, pos=0):        
        return '%s%3d %s' % (fontsizeTicks, x * 100., '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', fontsizeLegend + r'Hardcoded 4', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', fontsizeLegend + r'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', fontsizeLegend + r'Random 4', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=annotations,
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisTickFontSize=axisTickFontSize, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Percentage Global',
                                          axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                          axisXScale='linear', axisYScale='linear',
                                          legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="fstree4_search_g_l_traf.pdf")



def twitter_load_balance_all_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter2_balance.csv" 
    
    csvColumnPartition = "partitions"
    
    csvColumnRelsDiDiC = "rels_didic"
    csvColumnRelsRand = "rels_rand"
    
    csvColumnNodesDiDiC = "nodes_didic"
    csvColumnNodesRand = "nodes_rand"
    
    csvColumnTrafDiDiC = "traf_didic"
    csvColumnTrafRand = "traf_rand"
    
    legendAlpha = 0.8 
    maxY = 100
    reducedBarWidth = barWidth / 3.0
    axisGrid = False
    
    def do_annotation_avg_gltraf(ax):
        ax.axhline(y=50, linewidth=1, color='black', alpha=1.0, linestyle='--')
    
    annotations = [do_annotation_avg_gltraf]    
    
    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None)],
                                        [
                                         fontsizeLegend + r'DiDiC 2',
                                         fontsizeLegend + r'Random 2',
                                         ],
                                         csvFloats=(
                                                    csvColumnRelsDiDiC,
                                                    csvColumnRelsRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Edges', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right',
                                         legendCols=2,
                                         )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None)],
                                         [],
                                         csvFloats=(
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Vertices', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None)],
                                         [],
                                         csvFloats=(
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    show_plots([
                [do_rel_bal_bar],
                [do_node_bal_bar],
                [do_traf_bal_bar]],
                show=False,
                figHSpace=0.3,
                fileName="twitter2_bal_all.pdf")

def twitter_load_balance_all_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter4_balance.csv" 
    
    csvColumnPartition = "partitions"
    
    csvColumnRelsDiDiC = "rels_didic"
    csvColumnRelsRand = "rels_rand"
    
    csvColumnNodesDiDiC = "nodes_didic"
    csvColumnNodesRand = "nodes_rand"
    
    csvColumnTrafDiDiC = "traf_didic"
    csvColumnTrafRand = "traf_rand"
    
    legendAlpha = 0.8 
    maxY = 50
    reducedBarWidth = barWidth
    axisGrid = False
    
    def do_annotation_avg_gltraf(ax):
        ax.axhline(y=25, linewidth=1, color='black', alpha=1.0, linestyle='--')
    
    annotations = [do_annotation_avg_gltraf]    
        
    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None)],
                                        [
                                         fontsizeLegend + r'DiDiC 4',
                                         fontsizeLegend + r'Random 4',
                                         ],
                                         csvFloats=(
                                                    csvColumnRelsDiDiC,
                                                    csvColumnRelsRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Edges', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right',
                                         legendCols=2,
                                         )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None)],
                                         [],
                                         csvFloats=(
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Vertices', # axisXLabel=None,
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None)],
                                         [],
                                         csvFloats=(
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=annotations,
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=reducedBarWidth,
                                         barLog=True,
                                         axisGrid=axisGrid, axisTickFontSize=axisTickFontSize, axisColor='k',
                                         axisYLabel=fontsizeLabels + r'Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                         axisYLim=(0, maxY),
                                         legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos=None
                                         )
    
    show_plots([
                [do_rel_bal_bar],
                [do_node_bal_bar],
                [do_traf_bal_bar]],
                show=False,
                figHSpace=0.3,
                fileName="twitter4_bal_all.pdf")

def twitter_traf():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/"
    csvFile = csvFolder + "twitter_traffic.csv"     
    
    csvColumnIndex = "index"    
    csvColumnTraf = "traffic"

    def axisYFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
    do_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                      [(csvColumnTraf, 'blue', fontsizeLegend + r'Traffic', '-', ''), ],
                                      csvInts=(csvColumnTraf),
                                      annotations=[],
                                      axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                      axisTickFontSize=axisTickFontSize, axisColor='k',
                                      axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Traffic',
                                      axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                      axisXFormatterFun=None, axisYFormatterFun=None,
                                      axisXScale='linear', axisYScale='log',
                                      legendAlpha=0.8, legendShadow=False, legendColor='w',
                                      legendFancybox=False, legendPos='upper right',
                                      myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_traf_line]],
                show=False,
                fileName="twitter_traf.pdf")

def twitter_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter2_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           ],
                                           [
                                            fontsizeLegend + r'DiDiC 2',
                                            fontsizeLegend + r'Random 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                            barLog=True,
                                            axisGrid=True, axisTickFontSize=axisTickFontSize, axisColor='k',
                                            axisYLabel=fontsizeLabels + r'Percentage of Operations',
                                            axisXLabel=fontsizeLabels + r'Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 100),
                                            legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="twitter2_perc_gtraf.pdf")

def twitter_perc_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter4_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           ],
                                           [
                                            fontsizeLegend + r'DiDiC 4',
                                            fontsizeLegend + r'Random 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                            barLog=True,
                                            axisGrid=True, axisTickFontSize=axisTickFontSize, axisColor='k',
                                            axisYLabel=fontsizeLabels + r'Percentage of Operations',
                                            axisXLabel=fontsizeLabels + r'Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 100),
                                            legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="twitter4_perc_gtraf.pdf")
    
def twitter_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter2_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"

    csvFileAnnotate = csvFolder + "twitter2_gtraf.csv"
    csvColumnGLAvgHard = "g_l_avg_hard"
    csvColumnGLAvgDiDiC = "g_l_avg_didic"
    csvColumnGLAvgRand = "g_l_avg_rand"
    
    csvDict = csv_to_dict(csvFileAnnotate,
                          (csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand),
                          floats=(csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand))

    def get_do_annotation_avg_gltraf(column, color):
        def do_annotation_avg_gltraf(ax):
            ax.axhline(y=csvDict[column][0], linewidth=1, color=color, alpha=1.0, linestyle='--')
        return do_annotation_avg_gltraf
    
    annotations = []    
    for (column, color) in ((csvColumnGLAvgHard, 'blue'),
                           (csvColumnGLAvgDiDiC, 'red'),
                           (csvColumnGLAvgRand, 'green')):    
        annotations += [get_do_annotation_avg_gltraf(column, color)]
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)

    def axisYFormatterFun(x, pos=0):        
        return '%s%3d %s' % (fontsizeTicks, x * 100., '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
        
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [
                                          (csvColumnGLtrafDiDiC, 'red', fontsizeLegend + r'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', fontsizeLegend + r'Random 2', '-', ''),
                                          ],
                                          csvFloats=(
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand,
                                                     ),
                                          annotations=annotations,
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisTickFontSize=axisTickFontSize, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Percentage Global',
                                          axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                          axisXScale='linear', axisYScale='linear',
                                          legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="twitter2_g_l_traf.pdf")

def twitter_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter4_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    csvFileAnnotate = csvFolder + "twitter4_gtraf.csv"
    csvColumnGLAvgHard = "g_l_avg_hard"
    csvColumnGLAvgDiDiC = "g_l_avg_didic"
    csvColumnGLAvgRand = "g_l_avg_rand"
    
    csvDict = csv_to_dict(csvFileAnnotate,
                          (csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand),
                          floats=(csvColumnGLAvgHard, csvColumnGLAvgDiDiC, csvColumnGLAvgRand))

    def get_do_annotation_avg_gltraf(column, color):
        def do_annotation_avg_gltraf(ax):
            ax.axhline(y=csvDict[column][0], linewidth=1, color=color, alpha=1.0, linestyle='--')
        return do_annotation_avg_gltraf
    
    annotations = []    
    for (column, color) in ((csvColumnGLAvgHard, 'blue'),
                           (csvColumnGLAvgDiDiC, 'red'),
                           (csvColumnGLAvgRand, 'green')):    
        annotations += [get_do_annotation_avg_gltraf(column, color)]
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    def axisYFormatterFun(x, pos=0):        
        return '%s%3d %s' % (fontsizeTicks, x * 100., '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, (float(x) / 10000.) * 100., '$\%$')    
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [
                                          (csvColumnGLtrafDiDiC, 'red', fontsizeLegend + r'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', fontsizeLegend + r'Random 4', '-', ''),
                                          ],
                                          csvFloats=(
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand,
                                                     ),
                                          annotations=annotations,
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisTickFontSize=axisTickFontSize, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Operations', axisYLabel=fontsizeLabels + r'Percentage Global',
                                          axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                          axisXScale='linear', axisYScale='linear',
                                          legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="twitter4_g_l_traf.pdf")
