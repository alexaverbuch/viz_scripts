from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

fontsizeLabels = r'\LARGE '
fontsizeTicks = r'\Large '
fontsizeLegend = r'\Large '
axisTickFontSize = 16

def gis_dynamic_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Dynamic/"
    csvFile = csvFolder + "gis4_dynamic_gl_traf.csv"
    filename = 'gis4_dynamic_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun, axisYLim=(None, 2.0))     

def gis_dynamic_std_nodes_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Dynamic/"
    csvFile = csvFolder + "gis4_dynamic_std_nodes.csv"
    filename = 'gis4_dynamic_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_nodes_4_line(csvFolder, csvFile, filename=filename,
                             axisYFormatterFun=axisYFormatterFun, axisYLim=(None, 0.255))     

def gis_dynamic_std_rels_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Dynamic/"
    csvFile = csvFolder + "gis4_dynamic_std_rels.csv"
    filename = 'gis4_dynamic_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_rels_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def gis_dynamic_std_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Dynamic/"
    csvFile = csvFolder + "gis4_dynamic_std_traf.csv"
    filename = 'gis4_dynamic_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_traf_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun, axisYLim=(None, 0.4))     

def gis_dynamic_edge_cut_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Dynamic/"
    csvFile = csvFolder + "gis4_dynamic_edge_cut.csv"
    filename = 'gis4_dynamic_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_edge_cut_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun, axisYLim=(None, 16))



def fstree_dynamic_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Dynamic/"
    csvFile = csvFolder + "tree4_dynamic_gl_traf.csv"
    filename = 'fstree4_dynamic_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun,
                           axisYLim=(None, 18))     

def fstree_dynamic_std_nodes_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Dynamic/"
    csvFile = csvFolder + "tree4_dynamic_std_nodes.csv"
    filename = 'fstree4_dynamic_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_nodes_4_line(csvFolder, csvFile, filename=filename,
                             axisYFormatterFun=axisYFormatterFun,
                             axisYLim=(None, 0.08))     

def fstree_dynamic_std_rels_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Dynamic/"
    csvFile = csvFolder + "tree4_dynamic_std_rels.csv"
    filename = 'fstree4_dynamic_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_rels_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))     

def fstree_dynamic_std_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Dynamic/"
    csvFile = csvFolder + "tree4_dynamic_std_traf.csv"
    filename = 'fstree4_dynamic_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.3f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_traf_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, 0.16),
                            figLeftSpace=0.135)     

def fstree_dynamic_edge_cut_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Dynamic/"
    csvFile = csvFolder + "tree4_dynamic_edge_cut.csv"
    filename = 'fstree4_dynamic_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_edge_cut_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, 30))



def twitter_dynamic_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Dynamic/"
    csvFile = csvFolder + "twitter4_dynamic_gl_traf.csv"
    filename = 'twitter4_dynamic_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun,
                           axisYLim=(None, 24))     

def twitter_dynamic_std_nodes_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Dynamic/"
    csvFile = csvFolder + "twitter4_dynamic_std_nodes.csv"
    filename = 'twitter4_dynamic_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_nodes_4_line(csvFolder, csvFile, filename=filename,
                             axisYFormatterFun=axisYFormatterFun,
                             axisYLim=(None, None))     

def twitter_dynamic_std_rels_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Dynamic/"
    csvFile = csvFolder + "twitter4_dynamic_std_rels.csv"
    filename = 'twitter4_dynamic_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_rels_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))     

def twitter_dynamic_std_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Dynamic/"
    csvFile = csvFolder + "twitter4_dynamic_std_traf.csv"
    filename = 'twitter4_dynamic_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_std_traf_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))     

def twitter_dynamic_edge_cut_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Dynamic/"
    csvFile = csvFolder + "twitter4_dynamic_edge_cut.csv"
    filename = 'twitter4_dynamic_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    dynamic_edge_cut_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, 60))



def dynamic_gl_traf_4_line(csvFolder, csvFile, filename='output.pdf',
                           axisYFormatterFun=None,
                           axisXLim=(-0.2, 26), axisYLim=(None, None),
                           figLeftSpace=0.125):
    csvColumnChurnRand = "churn_rand"    
    csvColumnRand = "rand"
    csvColumnChurnDiDiC = "churn_didic"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurnRand, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurnDiDiC, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurnRand,
                                                    csvColumnRand,
                                                    csvColumnChurnDiDiC,
                                                    csvColumnDiDiC,),
                                         annotations=[],
                                         axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                         axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Percentage Global',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLim,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right',
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName=filename,
                figLeftSpace=figLeftSpace)

def dynamic_std_nodes_4_line(csvFolder, csvFile, filename='output.pdf',
                             axisYFormatterFun=None,
                             axisXLim=(-0.2, 26), axisYLim=(None, None),
                             figLeftSpace=0.125):
    csvColumnChurnRand = "churn_rand"    
    csvColumnRand = "rand"
    csvColumnChurnDiDiC = "churn_didic"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurnRand, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurnDiDiC, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurnRand,
                                                    csvColumnRand,
                                                    csvColumnChurnDiDiC,
                                                    csvColumnDiDiC),
                                         annotations=[],
                                         axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                         axisXLabel=fontsizeLabels + 'Churn', axisYLabel=fontsizeLabels + 'Vertex Imbalance',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLim,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right',
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName=filename,
                figLeftSpace=figLeftSpace)

def dynamic_std_rels_4_line(csvFolder, csvFile, filename='output.pdf',
                            axisYFormatterFun=None,
                            axisXLim=(-0.2, 26), axisYLim=(None, None),
                            figLeftSpace=0.125):
    csvColumnChurnRand = "churn_rand"    
    csvColumnRand = "rand"
    csvColumnChurnDiDiC = "churn_didic"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurnRand, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurnDiDiC, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurnRand,
                                                    csvColumnRand,
                                                    csvColumnChurnDiDiC,
                                                    csvColumnDiDiC),
                                         annotations=[],
                                         axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                         axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Edge Imbalance',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLim,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right',
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName=filename,
                figLeftSpace=figLeftSpace)

def dynamic_std_traf_4_line(csvFolder, csvFile, filename='output.pdf',
                            axisYFormatterFun=None,
                            axisXLim=(-0.2, 26), axisYLim=(None, None),
                            figLeftSpace=0.125):    
    csvColumnChurnRand = "churn_rand"    
    csvColumnRand = "rand"
    csvColumnChurnDiDiC = "churn_didic"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurnRand, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurnDiDiC, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurnRand,
                                                    csvColumnRand,
                                                    csvColumnChurnDiDiC,
                                                    csvColumnDiDiC),
                                         annotations=[],
                                         axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                         axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Traffic Imbalance',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLim,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right',
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName=filename,
                figLeftSpace=figLeftSpace)

def dynamic_edge_cut_4_line(csvFolder, csvFile, filename='output.pdf',
                            axisYFormatterFun=None,
                            axisXLim=(-0.2, 26), axisYLim=(None, None),
                            figLeftSpace=0.125):
    csvColumnChurnRand = "churn_rand"    
    csvColumnRand = "rand"
    csvColumnChurnDiDiC = "churn_didic"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fstree4_gtraf_line = get_line_from_file_multi_x(csvFile,
                                                       [(csvColumnChurnRand, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                                        (csvColumnChurnDiDiC, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                                        csvFloats=(csvColumnChurnRand,
                                                                   csvColumnRand,
                                                                   csvColumnChurnDiDiC,
                                                                   csvColumnDiDiC),
                                                        annotations=[],
                                                        axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                        axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                                        axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Edge Cut',
                                                        axisTitle='', axisXLim=axisXLim, axisYLim=axisYLim,
                                                        axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                                        axisXScale='linear', axisYScale='linear',
                                                        legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                        legendFancybox=False, legendPos='upper right',
                                                        myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree4_gtraf_line]],
                show=False,
                fileName=filename,
                figLeftSpace=figLeftSpace)
