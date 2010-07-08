from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

fontsizeLabels = r'\LARGE '
fontsizeTicks = r'\Large '
fontsizeLegend = r'\Large '
axisTickFontSize = 16


def gis_insert_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/read_results_5_95/"
    csvFile = csvFolder + "gis4_insert_gl_traf.csv"
    filename = 'gis4_insert_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    insert_gl_traf_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def gis_insert_std_nodes_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/read_results_5_95/"
    csvFile = csvFolder + "gis4_insert_std_nodes.csv"
    filename = 'gis4_insert_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')    

    insert_std_nodes_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def gis_insert_std_rels_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/read_results_5_95/"
    csvFile = csvFolder + "gis4_insert_std_rels.csv"
    filename = 'gis4_insert_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    insert_std_rels_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def gis_insert_std_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/read_results_5_95/"
    csvFile = csvFolder + "gis4_insert_std_traf.csv"
    filename = 'gis4_insert_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')    

    insert_std_traf_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def gis_insert_edge_cut_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Insert/read_results_5_95/"
    csvFile = csvFolder + "gis4_insert_edge_cut.csv"
    filename = 'gis4_insert_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')    

    insert_edge_cut_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)




def fstree_insert_gl_traf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_gl_traf.csv"    
    filename = 'fstree4_insert_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_gl_traf_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def fstree_insert_std_nodes_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_std_nodes.csv"
    filename = 'fstree4_insert_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_std_nodes_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def fstree_insert_std_rels_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_std_rels.csv"
    filename = 'fstree4_insert_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_std_rels_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def fstree_insert_std_traf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_std_traf.csv"
    filename = 'fstree4_insert_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.2f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_std_traf_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def fstree_insert_edge_cut_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Insert/"
    csvFile = csvFolder + "tree4_insert_edge_cut.csv"
    filename = 'fstree4_insert_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_edge_cut_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)




def twitter_insert_gl_traf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_gl_traf.csv"    
    filename = 'twitter4_insert_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.1f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_gl_traf_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def twitter_insert_std_nodes_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_std_nodes.csv"
    filename = 'twitter4_insert_std_nodes.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_std_nodes_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def twitter_insert_std_rels_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_std_rels.csv"
    filename = 'twitter4_insert_std_rels.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_std_rels_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def twitter_insert_std_traf_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_std_traf.csv"
    filename = 'twitter4_insert_std_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_std_traf_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)     

def twitter_insert_edge_cut_4():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Insert/"
    csvFile = csvFolder + "twitter4_insert_edge_cut.csv"
    filename = 'twitter4_insert_edge_cut.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%s%3.0f %s' % (fontsizeTicks, x , '$\%$')
        
    insert_edge_cut_4_line(csvFolder, csvFile, filename=filename, axisYFormatterFun=axisYFormatterFun)




def insert_gl_traf_4_line(csvFolder, csvFile, filename='output.pdf', axisYFormatterFun=None):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fstree4_gtraf_line = get_line_from_file(csvFile, csvColumnChurn,
                                               [(csvColumnSize, 'blue', fontsizeLegend + r'Vertex Count', '-', 'o'),
                                                (csvColumnRand, 'red', fontsizeLegend + r'Random', '-', 'v'),
                                                (csvColumnTraf, 'green', fontsizeLegend + r'Traffic', '-', 'd')],
                                                csvFloats=(
                                                           csvColumnSize,
                                                           csvColumnRand,
                                                           csvColumnTraf),
                                                annotations=[],
                                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                                axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Percentage Global',
                                                axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                                axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                                axisXScale='linear', axisYScale='linear',
                                                legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                legendFancybox=False, legendPos='upper right',
                                                myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree4_gtraf_line]],
                show=False,
                fileName=filename)

def insert_std_nodes_4_line(csvFolder, csvFile, filename='output.pdf', axisYFormatterFun=None):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file(csvFile, csvColumnChurn,
                                [(csvColumnSize, 'blue', fontsizeLegend + r'Vertex Count', '-', 'o'),
                                 (csvColumnRand, 'red', fontsizeLegend + r'Random', '-', 'v'),
                                 (csvColumnTraf, 'green', fontsizeLegend + r'Traffic', '-', 'd')],
                                 csvFloats=(csvColumnSize,
                                            csvColumnRand,
                                            csvColumnTraf),
                                 annotations=[],
                                 axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                 axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                 axisXLabel=fontsizeLabels + 'Churn', axisYLabel=fontsizeLabels + 'Vertex Imbalance',
                                 axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                 axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                 axisXScale='linear', axisYScale='linear',
                                 legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                 legendFancybox=False, legendPos='upper right',
                                 myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName=filename)

def insert_std_rels_4_line(csvFolder, csvFile, filename='output.pdf', axisYFormatterFun=None):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file(csvFile, csvColumnChurn,
                                [(csvColumnSize, 'blue', fontsizeLegend + r'Vertex Count', '-', 'o'),
                                 (csvColumnRand, 'red', fontsizeLegend + r'Random', '-', 'v'),
                                 (csvColumnTraf, 'green', fontsizeLegend + r'Traffic', '-', 'd')],
                                 csvFloats=(csvColumnSize,
                                            csvColumnRand,
                                            csvColumnTraf),
                                 annotations=[],
                                 axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                 axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                 axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Edge Imbalance',
                                 axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                 axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                 axisXScale='linear', axisYScale='linear',
                                 legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                 legendFancybox=False, legendPos='upper right',
                                 myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName=filename)

def insert_std_traf_4_line(csvFolder, csvFile, filename='output.pdf', axisYFormatterFun=None):    
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fun = get_line_from_file(csvFile, csvColumnChurn,
                                [(csvColumnSize, 'blue', fontsizeLegend + r'Vertex Count', '-', 'o'),
                                 (csvColumnRand, 'red', fontsizeLegend + r'Random', '-', 'v'),
                                 (csvColumnTraf, 'green', fontsizeLegend + r'Traffic', '-', 'd')],
                                 csvFloats=(csvColumnSize,
                                            csvColumnRand,
                                            csvColumnTraf),
                                 annotations=[],
                                 axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                 axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                 axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Traffic Imbalance',
                                 axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                 axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                 axisXScale='linear', axisYScale='linear',
                                 legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                 legendFancybox=False, legendPos='upper right',
                                 myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fun]],
                show=False,
                fileName=filename)

def insert_edge_cut_4_line(csvFolder, csvFile, filename='output.pdf', axisYFormatterFun=None):
    csvColumnChurn = "churn"    

    csvColumnSize = "size"
    csvColumnRand = "rand"
    csvColumnTraf = "traf"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%3d %s' % (fontsizeTicks, x, '$\%$')    
    
    do_fstree4_gtraf_line = get_line_from_file(csvFile, csvColumnChurn,
                                               [(csvColumnSize, 'blue', fontsizeLegend + r'Vertex Count', '-', 'o'),
                                                (csvColumnRand, 'red', fontsizeLegend + r'Random', '-', 'v'),
                                                (csvColumnTraf, 'green', fontsizeLegend + r'Traffic', '-', 'd')],
                                                csvFloats=(
                                                           csvColumnSize,
                                                           csvColumnRand,
                                                           csvColumnTraf),
                                                annotations=[],
                                                axisLineWidth=2.0, axisGrid=True, axisLineAntialiased=True,
                                                axisFontSize=12, axisColor='k', axisTickFontSize=axisTickFontSize,
                                                axisXLabel=fontsizeLabels + r'Churn', axisYLabel=fontsizeLabels + r'Edge Cut',
                                                axisTitle='', axisXLim=(None, None), axisYLim=(None, None),
                                                axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                                axisXScale='linear', axisYScale='linear',
                                                legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                                legendFancybox=False, legendPos='upper right',
                                                myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    show_plots([[do_fstree4_gtraf_line]],
                show=False,
                fileName=filename)
