from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *



def gis_short_load_balance_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
    csvFile = csvFolder + "gis2_short_balance.csv" 
    
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
    barWidth = 0.3
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 2',
                                         r'Random 2',
                                         r'Hardcoded 2',
                                         ],
                                        csvFloats=(
                                                   csvColumnRelsHard,
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(csvColumnNodesHard,
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(csvColumnTrafHard,
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    

def gis_short_load_balance_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
    csvFile = csvFolder + "gis4_short_balance.csv" 
    
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
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 4',
                                         r'Random 4',
                                         r'Hardcoded 4',
                                         ],
                                        csvFloats=(
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand,
                                                   csvColumnRelsHard,
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=0.3,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
                                          r'Hardcoded 4',
                                          ],
                                         csvFloats=(
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    csvColumnNodesHard,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=0.3,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
                                          r'Hardcoded 4',
                                          ],
                                          csvFloats=(
                                                     csvColumnTrafDiDiC,
                                                     csvColumnTrafRand,
                                                     csvColumnTrafHard,
                                                     ),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=0.3,
                                          barLog=True,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisYLabel='Traffic',
                                          axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                          legendColor='w', legendFancybox=False, legendPos='upper right'
                                          )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    

def gis_long_load_balance_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
    csvFile = csvFolder + "gis2_long_balance.csv" 
    
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
    barWidth = 0.3
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 2',
                                         r'Random 2',
                                         r'Hardcoded 2',
                                         ],
                                        csvFloats=(
                                                   csvColumnRelsHard,
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(csvColumnNodesHard,
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(csvColumnTrafHard,
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    

def gis_long_load_balance_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
    csvFile = csvFolder + "gis4_long_balance.csv" 
    
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
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 4',
                                         r'Random 4',
                                         r'Hardcoded 4',
                                         ],
                                        csvFloats=(
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand,
                                                   csvColumnRelsHard,
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=0.3,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
                                          r'Hardcoded 4',
                                          ],
                                         csvFloats=(
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    csvColumnNodesHard,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=0.3,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
                                          r'Hardcoded 4',
                                          ],
                                          csvFloats=(
                                                     csvColumnTrafDiDiC,
                                                     csvColumnTrafRand,
                                                     csvColumnTrafHard,
                                                     ),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=0.3,
                                          barLog=True,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisYLabel='Traffic',
                                          axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                          legendColor='w', legendFancybox=False, legendPos='upper right'
                                          )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    

def gis_long5_short95_load_balance_2():
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
    barWidth = 0.3
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 2',
                                         r'Random 2',
                                         r'Hardcoded 2',
                                         ],
                                        csvFloats=(
                                                   csvColumnRelsHard,
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(csvColumnNodesHard,
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(csvColumnTrafHard,
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    

def gis_long5_short95_load_balance_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_short_balance.csv" 
    
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
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 4',
                                         r'Random 4',
                                         r'Hardcoded 4',
                                         ],
                                        csvFloats=(
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand,
                                                   csvColumnRelsHard,
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=0.3,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
                                          r'Hardcoded 4',
                                          ],
                                         csvFloats=(
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    csvColumnNodesHard,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=0.3,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
                                          r'Hardcoded 4',
                                          ],
                                          csvFloats=(
                                                     csvColumnTrafDiDiC,
                                                     csvColumnTrafRand,
                                                     csvColumnTrafHard,
                                                     ),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=0.3,
                                          barLog=True,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisYLabel='Traffic',
                                          axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                          legendColor='w', legendFancybox=False, legendPos='upper right'
                                          )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    


def gis_short_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_short_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 2', '-', ''),
                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")

def gis_short_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_short_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 4', '-', ''),
                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")

def gis_long_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 2', '-', ''),
                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")

def gis_long_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 4', '-', ''),
                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")

def gis_long5_short95_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long5_short95_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 2', '-', ''),
                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")

def gis_long5_short95_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long5_short95_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 4', '-', ''),
                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")


def gis_short_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_short_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 2',
                                            r'Random 2',
                                            r'Hardcoded 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")

def gis_short_perc_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_short_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 4',
                                            r'Random 4',
                                            r'Hardcoded 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")

def gis_long_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 2',
                                            r'Random 2',
                                            r'Hardcoded 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")

def gis_long_perc_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 4',
                                            r'Random 4',
                                            r'Hardcoded 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")

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
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 2',
                                            r'Random 2',
                                            r'Hardcoded 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")

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
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 4',
                                            r'Random 4',
                                            r'Hardcoded 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")



def gis_short_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_short_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 2', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")

def gis_short_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_short_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 4', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")

def gis_long_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 2', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")

def gis_long_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 4', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")

def gis_long5_short95_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis2_long5_short95_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 2', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")

def gis_long5_short95_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Static/"
    csvFile = csvFolder + "gis4_long5_short95_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 4', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")




def fstree_search_load_balance_2():
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
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_fstree2_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
#                                               [(csvColumnRelsHard, 'blue', None),
#                                                (csvColumnRelsDiDiC, 'red', None),
#                                                (csvColumnRelsRand, 'green', None)],
                                               [(csvColumnRelsHard, 'blue', None),
                                                (csvColumnRelsDiDiC, 'red', None),
                                                (csvColumnRelsRand, 'green', None)],
                                                [r'Hardcoded 2', r'DiDiC 2', r'Random 2'],
                                                csvFloats=(csvColumnRelsHard,
                                                           csvColumnRelsDiDiC,
                                                           csvColumnRelsRand),
                                                annotations=[],
                                                barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                barAlign='center', barOrientation='vertical', barWidth=0.3,
                                                barLog=True,
                                                axisGrid=True, axisFontSize=12, axisColor='k',
                                                axisYLabel='Stored Relationships',
                                                axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                                legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                                legendColor='w', legendFancybox=False, legendPos='upper right'
                                                )
    
    do_fstree2_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnNodesHard, 'blue', None),
                                                 (csvColumnNodesDiDiC, 'red', None),
                                                 (csvColumnNodesRand, 'green', None)],
                                                 [r'Hardcoded 2', r'DiDiC 2', r'Random 2'],
                                                 csvFloats=(csvColumnNodesHard,
                                                            csvColumnNodesDiDiC,
                                                            csvColumnNodesRand),
                                                 annotations=[],
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=0.3,
                                                 barLog=True,
                                                 axisGrid=True, axisFontSize=12, axisColor='k',
                                                 axisYLabel='Stored Nodes',
                                                 axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                                 legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos='upper right'
                                                 )
    
    do_fstree2_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnTrafHard, 'blue', None),
                                                 (csvColumnTrafDiDiC, 'red', None),
                                                 (csvColumnTrafRand, 'green', None)],
                                                 [r'Hardcoded 2', r'DiDiC 2', r'Random 2'],
                                                 csvFloats=(csvColumnTrafHard,
                                                            csvColumnTrafDiDiC,
                                                            csvColumnTrafRand),
                                                 annotations=[],
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=0.3,
                                                 barLog=True,
                                                 axisGrid=True, axisFontSize=12, axisColor='k',
                                                 axisYLabel='Traffic',
                                                 axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                                 legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos='upper right'
                                                 )
    
    show_plots([[do_fstree2_rel_bal_bar]],
                show=False,
                fileName="output-do_fstree2_rel_bal_bar.pdf")
    show_plots([[do_fstree2_node_bal_bar]],
                show=False,
                fileName="output-do_fstree2_node_bal_bar.pdf")
    show_plots([[do_fstree2_traf_bal_bar]],
                show=False,
                fileName="output-do_fstree2_traf_bal_bar.pdf")    

def fstree_search_load_balance_4():
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
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_fstree4_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                               [(csvColumnRelsHard, 'blue', None),
                                                (csvColumnRelsDiDiC, 'red', None),
                                                (csvColumnRelsRand, 'green', None)],
                                                [r'Hardcoded 4', r'DiDiC 4', r'Random 4'],
                                                csvFloats=(csvColumnRelsHard,
                                                           csvColumnRelsDiDiC,
                                                           csvColumnRelsRand),
                                                annotations=[],
                                                barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                barAlign='center', barOrientation='vertical', barWidth=0.3,
                                                barLog=True,
                                                axisGrid=True, axisFontSize=12, axisColor='k',
                                                axisYLabel='Stored Relationships',
                                                axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                                legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                                legendColor='w', legendFancybox=False, legendPos='upper right'
                                                )
    
    do_fstree4_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnNodesHard, 'blue', None),
                                                 (csvColumnNodesDiDiC, 'red', None),
                                                 (csvColumnNodesRand, 'green', None)],
                                                 [r'Hardcoded 4', r'DiDiC 4', r'Random 4'],
                                                 csvFloats=(csvColumnNodesHard,
                                                            csvColumnNodesDiDiC,
                                                            csvColumnNodesRand),
                                                 annotations=[],
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=0.3,
                                                 barLog=True,
                                                 axisGrid=True, axisFontSize=12, axisColor='k',
                                                 axisYLabel='Stored Nodes',
                                                 axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                                 legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos='upper right'
                                                 )
    
    do_fstree4_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                                [(csvColumnTrafHard, 'blue', None),
                                                 (csvColumnTrafDiDiC, 'red', None),
                                                 (csvColumnTrafRand, 'green', None)],
                                                 [r'Hardcoded 4', r'DiDiC 4', r'Random 4'],
                                                 csvFloats=(csvColumnTrafHard,
                                                            csvColumnTrafDiDiC,
                                                            csvColumnTrafRand),
                                                 annotations=[],
                                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                                 barAlign='center', barOrientation='vertical', barWidth=0.3,
                                                 barLog=True,
                                                 axisGrid=True, axisFontSize=12, axisColor='k',
                                                 axisYLabel='Traffic',
                                                 axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                                 legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                                 legendColor='w', legendFancybox=False, legendPos='upper right'
                                                 )
    
    show_plots([[do_fstree4_rel_bal_bar]],
                show=False,
                fileName="output-do_fstree4_rel_bal_bar.pdf")
    show_plots([[do_fstree4_node_bal_bar]],
                show=False,
                fileName="output-do_fstree4_node_bal_bar.pdf")
    show_plots([[do_fstree4_traf_bal_bar]],
                show=False,
                fileName="output-do_fstree4_traf_bal_bar.pdf")    


def fstree_search_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree2_search_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_fstree2_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                               [(csvColumnGtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                                (csvColumnGtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                                (csvColumnGtrafRand, 'green', 'Random 2', '-', '')],
                                                csvInts=(csvColumnGtrafHard,
                                                         csvColumnGtrafDiDiC,
                                                         csvColumnGtrafRand),
                                                annotations=[],
                                                
                                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                axisFontSize=12, axisColor='k',
                                                axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                                axisXLim=(None, None), axisYLim=(0, 30000),
                                                axisXFormatterFun=None, axisYFormatterFun=None,
                                                axisXScale='linear', axisYScale='log',
                                                legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                legendFancybox=False, legendPos='upper right',
                                                myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree2_gtraf_line]],
                show=False,
                fileName="output.pdf")

def fstree_search_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree4_search_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_fstree4_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                               [(csvColumnGtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                                (csvColumnGtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                                (csvColumnGtrafRand, 'green', 'Random 4', '-', '')],
                                                csvInts=(csvColumnGtrafHard,
                                                         csvColumnGtrafDiDiC,
                                                         csvColumnGtrafRand),
                                                annotations=[],
                                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                axisFontSize=12, axisColor='k',
                                                axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                                axisXLim=(None, None), axisYLim=(None, None),
                                                axisXFormatterFun=None, axisYFormatterFun=None,
                                                axisXScale='linear', axisYScale='log',
                                                legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                legendFancybox=False, legendPos='upper right',
                                                myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree4_gtraf_line]],
                show=False,
                fileName="output.pdf")


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
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
                            
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnSearchDiDiC, 'red', None),
                                           (csvColumnSearchRand, 'green', None),
                                           (csvColumnSearchHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 2',
                                            r'Random 2',
                                            r'Hardcoded 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnSearchDiDiC,
                                                       csvColumnSearchRand,
                                                       csvColumnSearchHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")

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
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
                            
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnSearchDiDiC, 'red', None),
                                           (csvColumnSearchRand, 'green', None),
                                           (csvColumnSearchHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 4',
                                            r'Random 4',
                                            r'Hardcoded 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnSearchDiDiC,
                                                       csvColumnSearchRand,
                                                       csvColumnSearchHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 130),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")


def fstree_search_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree2_search_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 2', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")

def fstree_search_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Static/"
    csvFile = csvFolder + "tree4_search_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafHard = "g_l_hard"
    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [(csvColumnGLtrafHard, 'blue', 'Hardcoded 4', '-', ''),
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 4', '-', '')],
                                          csvFloats=(csvColumnGLtrafHard,
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")




def twitter_load_balance_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter2_balance.csv" 
    
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
    barWidth = 0.3
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
#                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 2',
                                         r'Random 2',
#                                         r'Hardcoded 2',
                                         ],
                                        csvFloats=(
#                                                   csvColumnRelsHard,
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
#                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
#                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(
#                                                    csvColumnNodesHard,
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
#                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 2',
                                          r'Random 2',
#                                          r'Hardcoded 2',
                                          ],
                                         csvFloats=(
#                                                    csvColumnTrafHard,
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    

def twitter_load_balance_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter4_balance.csv" 
    
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
    barWidth = 0.3
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_rel_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                       [
                                        (csvColumnRelsDiDiC, 'red', None),
                                        (csvColumnRelsRand, 'green', None),
#                                        (csvColumnRelsHard, 'blue', None),
                                        ],
                                        [
                                         r'DiDiC 4',
                                         r'Random 4',
#                                         r'Hardcoded 4',
                                         ],
                                        csvFloats=(
#                                                   csvColumnRelsHard,
                                                   csvColumnRelsDiDiC,
                                                   csvColumnRelsRand
                                                   ),
                                        annotations=[],
                                        barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                        barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                        barLog=True,
                                        axisGrid=True, axisFontSize=12, axisColor='k',
                                        axisYLabel='Stored Relationships',
                                        axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                        legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                        legendColor='w', legendFancybox=False, legendPos='upper right'
                                        )
    
    do_node_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnNodesDiDiC, 'red', None),
                                         (csvColumnNodesRand, 'green', None),
#                                         (csvColumnNodesHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
#                                          r'Hardcoded 4',
                                          ],
                                         csvFloats=(
#                                                    csvColumnNodesHard,
                                                    csvColumnNodesDiDiC,
                                                    csvColumnNodesRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Stored Nodes',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    do_traf_bal_bar = get_bar_from_file(csvFile, csvColumnPartition,
                                        [
                                         (csvColumnTrafDiDiC, 'red', None),
                                         (csvColumnTrafRand, 'green', None),
#                                         (csvColumnTrafHard, 'blue', None),
                                         ],
                                         [
                                          r'DiDiC 4',
                                          r'Random 4',
#                                          r'Hardcoded 4',
                                          ],
                                         csvFloats=(
#                                                    csvColumnTrafHard,
                                                    csvColumnTrafDiDiC,
                                                    csvColumnTrafRand,
                                                    ),
                                         annotations=[],
                                         barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                         barAlign='center', barOrientation='vertical', barWidth=barWidth,
                                         barLog=True,
                                         axisGrid=True, axisFontSize=12, axisColor='k',
                                         axisYLabel='Traffic',
                                         axisYFormatterFun=axisYFormatterFun, axisYLim=(0, 100),
                                         legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                         legendColor='w', legendFancybox=False, legendPos='upper right'
                                         )
    
    show_plots([[do_rel_bal_bar]],
                show=False,
                fileName="output-do_rel_bal_bar.pdf")
    show_plots([[do_node_bal_bar]],
                show=False,
                fileName="output-do_node_bal_bar.pdf")
    show_plots([[do_traf_bal_bar]],
                show=False,
                fileName="output-do_traf_bal_bar.pdf")    


def twitter_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter2_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 2', '-', ''),
#                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
#                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")

def twitter_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter4_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGtrafHard = "g_hard"
    csvColumnGtrafDiDiC = "g_didic"
    csvColumnGtrafRand = "g_rand"
    
    def axisYFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gtraf_line = get_line_from_file(csvFile, csvColumnIndex,
                                       [
                                        (csvColumnGtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                        (csvColumnGtrafRand, 'green', 'Random 4', '-', ''),
#                                        (csvColumnGtrafHard, 'blue', 'Hardcoded 2', '-', ''),
                                        ],
                                        csvFloats=(
                                                   csvColumnGtrafDiDiC,
                                                   csvColumnGtrafRand,
#                                                   csvColumnGtrafHard,
                                                   ),
                                        annotations=[],
                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                        axisFontSize=12, axisColor='k',
                                        axisXLabel='Operations', axisYLabel='Global Traffic', axisTitle='',
                                        axisXLim=(None, None), axisYLim=(None, None),
                                        axisXFormatterFun=None, axisYFormatterFun=None,
                                        axisXScale='linear', axisYScale='log',
                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                        legendFancybox=False, legendPos='upper right',
                                        myShareAxis=None, shareAxisX=None, shareAxisY=None
                                        )    
    
    show_plots([[do_gtraf_line]],
                show=False,
                fileName="output.pdf")


def twitter_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter2_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
#                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 2',
                                            r'Random 2',
#                                            r'Hardcoded 2',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
#                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 100),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")

def twitter_perc_gtraf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
    csvFile = csvFolder + "twitter4_perc_gtraf.csv"     
    
    csvColumnPerc = "perc_gtraf"    

    csvColumnGlobalHard = "hard"
    csvColumnGlobalDiDiC = "didic"
    csvColumnGlobalRand = "rand"
    
    def axisYFormatterFun(x, pos=0):
        if x > 100:
            return ""        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
        
    do_perc_gtraf_bar = get_bar_from_file(csvFile, csvColumnPerc,
                                          [
                                           (csvColumnGlobalDiDiC, 'red', None),
                                           (csvColumnGlobalRand, 'green', None),
#                                           (csvColumnGlobalHard, 'blue', None),
                                           ],
                                           [
                                            r'DiDiC 4',
                                            r'Random 4',
#                                            r'Hardcoded 4',
                                            ],
                                            csvFloats=(
                                                       csvColumnPerc,
                                                       csvColumnGlobalDiDiC,
                                                       csvColumnGlobalRand,
#                                                       csvColumnGlobalHard,
                                                       ),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=0.2,
                                            barLog=True,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisYLabel='Percentage of Operations',
                                            axisXLabel='Amount of Global Traffic',
                                            axisYFormatterFun=axisYFormatterFun,
                                            axisXFormatterFun=axisXFormatterFun,
                                            axisYLim=(0, 100),
                                            legendFontsize=12, legendAlpha=0.8, legendShadow=False,
                                            legendColor='w', legendFancybox=False, legendPos='upper right'
                                            )

    show_plots([[do_perc_gtraf_bar]],
                show=False,
                fileName="output.pdf")


def twitter_glratio_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter2_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 2', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 2', '-', ''),
                                          ],
                                          csvFloats=(
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand,
                                                     ),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")

def twitter_glratio_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Static/"
    csvFile = csvFolder + "twitter4_gtraf.csv"     
    
    csvColumnIndex = "index"    

    csvColumnGLtrafDiDiC = "g_l_didic"
    csvColumnGLtrafRand = "g_l_rand"
    
    def axisYFormatterFun(x, pos=0):        
        return '%3d %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3.0f %s' % ((float(x) / 10000.) * 100., '$\%$')    
    
#linestyles
# ('-',solid)('--',dashed)('-.',dash-dot)(':',dotted)

#markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)
    
    do_gl_traf_line = get_line_from_file(csvFile, csvColumnIndex,
                                         [
                                          (csvColumnGLtrafDiDiC, 'red', 'DiDiC 4', '-', ''),
                                          (csvColumnGLtrafRand, 'green', 'Random 4', '-', ''),
                                          ],
                                          csvFloats=(
                                                     csvColumnGLtrafDiDiC,
                                                     csvColumnGLtrafRand,
                                                     ),
                                          annotations=[],
                                          axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                          axisFontSize=12, axisColor='k',
                                          axisXLabel=r'Operations', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                          axisXLim=(None, None), axisYLim=(None, None),
                                          axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=None,
                                          axisXScale='linear', axisYScale='linear',
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_gl_traf_line]],
                show=False,
                fileName="output.pdf")
