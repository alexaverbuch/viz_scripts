from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

fontsizeLabels = r'\LARGE '
fontsizeTicks = r'\Large '
fontsizeLegend = r'\Large '
axisTickFontSize = 16

def gis_stress_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFile = csvFolder + "gis4_didic_stress_gl_traf.csv"
    filename = 'gis4_didic_stress_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    stress_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun, axisYLim=(None, 2.0))     

def gis_stress_std_nodes_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFile = csvFolder + "gis4_didic_stress_std_nodes.csv"
    filename = 'gis4_didic_stress_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_nodes_4_line(csvFolder, csvFile, filename=filename,
                             axisYFormatterFun=axisYFormatterFun, axisYLim=(None, 0.25))     

def gis_stress_std_rels_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFile = csvFolder + "gis4_didic_stress_std_rels.csv"
    filename = 'gis4_didic_stress_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_rels_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def gis_stress_std_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFile = csvFolder + "gis4_didic_stress_std_traf.csv"
    filename = 'gis4_didic_stress_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_traf_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun, axisYLim=(None, None))     

def gis_stress_edge_cut_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFile = csvFolder + "gis4_didic_stress_edge_cut.csv"
    filename = 'gis4_didic_stress_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    stress_edge_cut_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun, axisYLim=(None, 16))



def fstree_stress_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFile = csvFolder + "tree4_didic_stress_gl_traf.csv"
    filename = 'fstree4_didic_stress_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    stress_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun,
                           axisYLim=(None, None))     

def fstree_stress_std_nodes_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFile = csvFolder + "tree4_didic_stress_std_nodes.csv"
    filename = 'fstree4_didic_stress_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_nodes_4_line(csvFolder, csvFile, filename=filename,
                             axisYFormatterFun=axisYFormatterFun,
                             axisYLim=(None, None))     

def fstree_stress_std_rels_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFile = csvFolder + "tree4_didic_stress_std_rels.csv"
    filename = 'fstree4_didic_stress_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_rels_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))     

def fstree_stress_std_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFile = csvFolder + "tree4_didic_stress_std_traf.csv"
    filename = 'fstree4_didic_stress_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.3f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_traf_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))     

def fstree_stress_edge_cut_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFile = csvFolder + "tree4_didic_stress_edge_cut.csv"
    filename = 'fstree4_didic_stress_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    stress_edge_cut_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))



def twitter_stress_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFile = csvFolder + "twitter4_didic_stress_gl_traf.csv"
    filename = 'twitter4_didic_stress_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    stress_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun,
                           axisYLim=(None, None))     

def twitter_stress_std_nodes_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFile = csvFolder + "twitter4_didic_stress_std_nodes.csv"
    filename = 'twitter4_didic_stress_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_nodes_4_line(csvFolder, csvFile, filename=filename,
                             axisYFormatterFun=axisYFormatterFun,
                             axisYLim=(None, None))     

def twitter_stress_std_rels_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFile = csvFolder + "twitter4_didic_stress_std_rels.csv"
    filename = 'twitter4_didic_stress_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_rels_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))     

def twitter_stress_std_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFile = csvFolder + "twitter4_didic_stress_std_traf.csv"
    filename = 'twitter4_didic_stress_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    stress_std_traf_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))     

def twitter_stress_edge_cut_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFile = csvFolder + "twitter4_didic_stress_edge_cut.csv"
    filename = 'twitter4_didic_stress_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    stress_edge_cut_4_line(csvFolder, csvFile, filename=filename,
                            axisYFormatterFun=axisYFormatterFun,
                            axisYLim=(None, None))



def stress_gl_traf_4_line(csvFolder, csvFile, filename='output.pdf',
                           axisYFormatterFun=None,
                           axisXLim=(-0.2, 26), axisYLim=(None, None),
                           figLeftSpace=0.125):
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurn, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurn, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurn,
                                                    csvColumnRand,
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

def stress_std_nodes_4_line(csvFolder, csvFile, filename='output.pdf',
                             axisYFormatterFun=None,
                             axisXLim=(-0.2, 26), axisYLim=(None, None),
                             figLeftSpace=0.125):
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurn, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurn, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurn,
                                                    csvColumnRand,
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

def stress_std_rels_4_line(csvFolder, csvFile, filename='output.pdf',
                            axisYFormatterFun=None,
                            axisXLim=(-0.2, 26), axisYLim=(None, None),
                            figLeftSpace=0.125):
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurn, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurn, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurn,
                                                    csvColumnRand,
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

def stress_std_traf_4_line(csvFolder, csvFile, filename='output.pdf',
                            axisYFormatterFun=None,
                            axisXLim=(-0.2, 26), axisYLim=(None, None),
                            figLeftSpace=0.125):    
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurn, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                         (csvColumnChurn, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurn,
                                                    csvColumnRand,
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

def stress_edge_cut_4_line(csvFolder, csvFile, filename='output.pdf',
                            axisYFormatterFun=None,
                            axisXLim=(-0.2, 26), axisYLim=(None, None),
                            figLeftSpace=0.125):
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fstree4_gtraf_line = get_line_from_file_multi_x(csvFile,
                                                       [(csvColumnChurn, csvColumnRand, 'blue', fontsizeLegend + r'Churn', '-', 'o'),
                                                        (csvColumnChurn, csvColumnDiDiC, 'red', fontsizeLegend + r'Churn + DiDiC', '-', 'v'), ],
                                                        csvFloats=(csvColumnChurn,
                                                                   csvColumnRand,
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
