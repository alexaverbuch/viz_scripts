from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

def gis_insert_gl_traf4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/"
    csvFile = csvFolder + "gis4_insert_gl_traf.csv"    
    insert_gl_traf4_line(csvFolder, csvFile)     

def gis_insert_std_nodes_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/"
    csvFile = csvFolder + "gis4_insert_std_nodes.csv"
    insert_std_nodes_4_line(csvFolder, csvFile)     

def gis_insert_std_rels_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/"
    csvFile = csvFolder + "gis4_insert_std_rels.csv"
    insert_std_rels_4_line(csvFolder, csvFile)     

def gis_insert_std_traf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/"
    csvFile = csvFolder + "gis4_insert_std_traf.csv"
    insert_std_traf_4_line(csvFolder, csvFile)     





def fstree_insert_gl_traf4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_gl_traf.csv"    
    insert_gl_traf4_line(csvFolder, csvFile)     

def fstree_insert_std_nodes_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_std_nodes.csv"
    insert_std_nodes_4_line(csvFolder, csvFile)     

def fstree_insert_std_rels_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_std_rels.csv"
    insert_std_rels_4_line(csvFolder, csvFile)     

def fstree_insert_std_traf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_std_traf.csv"
    insert_std_traf_4_line(csvFolder, csvFile)     





def twitter_insert_gl_traf4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_gl_traf.csv"    
    insert_gl_traf4_line(csvFolder, csvFile)     

def twitter_insert_std_nodes_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_std_nodes.csv"
    insert_std_nodes_4_line(csvFolder, csvFile)     

def twitter_insert_std_rels_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_std_rels.csv"
    insert_std_rels_4_line(csvFolder, csvFile)     

def twitter_insert_std_traf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_std_traf.csv"
    insert_std_traf_4_line(csvFolder, csvFile)     





def insert_gl_traf4_line(csvFolder, csvFile):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    #markers
#('.',point)(',',pixel)('o',circle)('v',triangle_down)('^',triangle_up)
#('<',triangle_left)('>',triangle_right)('1',tri_down)('2',tri_up)
#('3',tri_left)('4',tri_right)('s',square)('p',pentagon)
#('*',star)('h',hexagon1)('H',hexagon2)('+',plus)('x',x)
#('D',diamond)('d',thin_diamond)('|',vline)('_',hline)

    
    def axisYFormatterFun(x, pos=0):
        return '%3.1f %s' % (x , '$\%$')    

    def axisXFormatterFun(x, pos=0):
#        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
        return '%3d %s' % (x, '$\%$')    
    
    do_fstree4_gtraf_line = get_line_from_file(csvFile, csvColumnChurn,
                                               [(csvColumnSize, 'blue', 'Node Count', '-', 'o'),
                                                (csvColumnRand, 'red', 'Random', '-', 'v'),
                                                (csvColumnTraf, 'green', 'Traffic', '-', 'd')],
                                                csvFloats=(
                                                           csvColumnSize,
                                                           csvColumnRand,
                                                           csvColumnTraf),
                                                annotations=[],
                                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                axisFontSize=12, axisColor='k',
                                                axisXLabel='Churn', axisYLabel=r'Global Traffic / Local Traffic', axisTitle='',
                                                axisXLim=(None, None), axisYLim=(None, None),
                                                axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                                axisXScale='linear', axisYScale='linear',
                                                legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                legendFancybox=False, legendPos='upper right',
                                                myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree4_gtraf_line]],
                show=False,
                fileName="output.pdf")

def insert_std_nodes_4_line(csvFolder, csvFile):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisYFormatterFun(x, pos=0):
        return '%3.1f %s' % (x , '$\%$')    

    def axisXFormatterFun(x, pos=0):
#        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
        return '%3d %s' % (x, '$\%$')    
    
    do_fun = get_line_from_file(csvFile, csvColumnChurn,
                                [(csvColumnSize, 'blue', 'Node Count', '-', 'o'),
                                 (csvColumnRand, 'red', 'Random', '-', 'v'),
                                 (csvColumnTraf, 'green', 'Traffic', '-', 'd')],
                                 csvFloats=(csvColumnSize,
                                            csvColumnRand,
                                            csvColumnTraf),
                                 annotations=[],
                                 axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                 axisFontSize=12, axisColor='k',
                                 axisXLabel='Churn', axisYLabel=r'Nodes per Partition (Standard Deviation)', axisTitle='',
                                 axisXLim=(None, None), axisYLim=(None, None),
                                 axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                 axisXScale='linear', axisYScale='linear',
                                 legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                 legendFancybox=False, legendPos='upper right',
                                 myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName="output.pdf")

def insert_std_rels_4_line(csvFolder, csvFile):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisYFormatterFun(x, pos=0):
        return '%3.1f %s' % (x , '$\%$')    

    def axisXFormatterFun(x, pos=0):
#        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
        return '%3d %s' % (x, '$\%$')    
    
    do_fun = get_line_from_file(csvFile, csvColumnChurn,
                                [(csvColumnSize, 'blue', 'Node Count', '-', 'o'),
                                 (csvColumnRand, 'red', 'Random', '-', 'v'),
                                 (csvColumnTraf, 'green', 'Traffic', '-', 'd')],
                                 csvFloats=(csvColumnSize,
                                            csvColumnRand,
                                            csvColumnTraf),
                                 annotations=[],
                                 axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                 axisFontSize=12, axisColor='k',
                                 axisXLabel='Churn', axisYLabel=r'Relationships per Partition (Standard Deviation)', axisTitle='',
                                 axisXLim=(None, None), axisYLim=(None, None),
                                 axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                 axisXScale='linear', axisYScale='linear',
                                 legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                 legendFancybox=False, legendPos='upper right',
                                 myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName="output.pdf")

def insert_std_traf_4_line(csvFolder, csvFile):    
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisYFormatterFun(x, pos=0):
        return '%3.1f %s' % (x , '$\%$')    

    def axisXFormatterFun(x, pos=0):
#        return '%3.1f %s' % ((float(x) / 10000.) * 100., '$\%$')    
        return '%3d %s' % (x, '$\%$')    
    
    do_fun = get_line_from_file(csvFile, csvColumnChurn,
                                [(csvColumnSize, 'blue', 'Node Count', '-', 'o'),
                                 (csvColumnRand, 'red', 'Random', '-', 'v'),
                                 (csvColumnTraf, 'green', 'Traffic', '-', 'd')],
                                 csvFloats=(csvColumnSize,
                                            csvColumnRand,
                                            csvColumnTraf),
                                 annotations=[],
                                 axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                 axisFontSize=12, axisColor='k',
                                 axisXLabel='Churn', axisYLabel=r'Traffic per Partition (Standard Deviation)', axisTitle='',
                                 axisXLim=(None, None), axisYLim=(None, None),
                                 axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                 axisXScale='linear', axisYScale='linear',
                                 legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                 legendFancybox=False, legendPos='upper right',
                                 myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName="output.pdf")


def insert_gl_traf4_bar(csvFolder, csvFile, axisYLim=(None, None)):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    legendAlpha = 0.8 
    
    def axisYFormatterFun(x, pos=0):
        return '%3.2f %s' % (x, '$\%$')    

    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')
    
#    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    
    do_fun = get_bar_from_file(csvFile, csvColumnChurn,
                               [
                                (csvColumnSize, 'red', None),
                                (csvColumnRand, 'green', None),
                                (csvColumnTraf, 'blue', None),
                                ],
                                [
                                 r'Node Count',
                                 r'Random',
                                 r'Traffic',
                                 ],
                                 csvFloats=(
                                            csvColumnChurn,
                                            csvColumnSize,
                                            csvColumnRand,
                                            csvColumnTraf,
                                            ),
                                 annotations=[],
                                 barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                 barAlign='center', barOrientation='vertical', barWidth=0.3,
                                 barLog=True,
                                 axisGrid=True, axisFontSize=12, axisColor='k',
                                 axisYLabel=r'Global Traffic / Local Traffic',
                                 axisYFormatterFun=axisYFormatterFun, axisXFormatterFun=axisXFormatterFun,
                                 axisYLim=axisYLim,
                                 legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                 legendColor='w', legendFancybox=False, legendPos='upper right'
                                 )    
    
    show_plots([[do_fun]],
                show=False,
                fileName="output.pdf")
