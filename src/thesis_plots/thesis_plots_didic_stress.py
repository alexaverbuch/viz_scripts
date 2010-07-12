from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

#defFigWidth = 8.0
#defFigHeight = 7.0

#defFigLeftSpace = 0.16
#defFigBottomSpace = 0.17
#defFigRightSpace = 0.97
#defFigTopSpace = 0.8

defFigWidth = 9.0
defFigHeight = 9.0

defFigLeftSpace = 0.16
defFigBottomSpace = 0.11
defFigRightSpace = 0.98
defFigTopSpace = 0.86

def gis_stress_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFile = csvFolder + "gis4_didic_stress_gl_traf.csv"
    filename = 'gis4_didic_stress_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%3.1f' % (x)    

    stress_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun, axisYLim=(None, None))     

def gis_stress_std_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFileNode = csvFolder + "gis4_didic_stress_std_nodes.csv"
    csvFileRel = csvFolder + "gis4_didic_stress_std_rels.csv"
    csvFileTraf = csvFolder + "gis4_didic_stress_std_traf.csv"
    filename = 'gis4_didic_stress_std_all.pdf'    
    
    def axisYFormatterFunNode(x, pos=0):
        return '%3.2f' % (x)
    def axisYFormatterFunRel(x, pos=0):
        return '%3.1f' % (x)
    def axisYFormatterFunTraf(x, pos=0):
        return '%3.2f' % (x)
        
    stress_std_all_4_line(csvFolder, 
                          csvFileNode, csvFileRel, csvFileTraf,
                          axisYFormatterFunNode=axisYFormatterFunNode,
                          axisYFormatterFunRel=axisYFormatterFunRel,
                          axisYFormatterFunTraf=axisYFormatterFunTraf,
                          axisYLimNode=(None,0.25),
                          axisYLimTraf=(None,None),
                          filename=filename)     

def gis_stress_comms_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFileEdgeCut = csvFolder + "gis4_didic_stress_edge_cut.csv"
    csvFileGLTraf = csvFolder + "gis4_didic_stress_gl_traf.csv"
    filename = 'gis4_didic_stress_comms_all.pdf'    
    
    def axisYFormatterFunEdgeCut(x, pos=0):
        return '%3.0f\,%s' % (x, r'\%')
    def axisYFormatterFunGLTraf(x, pos=0):
        return '%3.1f\,%s' % (x, r'\%')
        
    stress_comms_all_4_line(csvFolder, csvFileEdgeCut, csvFileGLTraf,
                            axisYFormatterFunEdgeCut=axisYFormatterFunEdgeCut,
                            axisYFormatterFunGLTraf=axisYFormatterFunGLTraf,
                            filename=filename)     



def fstree_stress_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFile = csvFolder + "tree4_didic_stress_gl_traf.csv"
    filename = 'fstree4_didic_stress_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%3.1f' % (x)    

    stress_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun,
                           axisYLim=(None, None),
                           figLeftSpace = 0.18)     

def fstree_stress_std_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFileNode = csvFolder + "tree4_didic_stress_std_nodes.csv"
    csvFileRel = csvFolder + "tree4_didic_stress_std_rels.csv"
    csvFileTraf = csvFolder + "tree4_didic_stress_std_traf.csv"
    filename = 'fstree4_didic_stress_std_all.pdf'    
    
    def axisYFormatterFunNode(x, pos=0):
        return '%3.3f' % (x)
    def axisYFormatterFunRel(x, pos=0):
        return '%3.2f' % (x)
    def axisYFormatterFunTraf(x, pos=0):
        return '%3.3f' % (x)
        
    stress_std_all_4_line(csvFolder, 
                          csvFileNode, csvFileRel, csvFileTraf,
                          axisYFormatterFunNode=axisYFormatterFunNode,
                          axisYFormatterFunRel=axisYFormatterFunRel,
                          axisYFormatterFunTraf=axisYFormatterFunTraf,
                          axisYLimNode=(None,None),
                          axisYLimRel=(None,0.235),
                          axisYLimTraf=(None,0.157),
                          filename=filename)     

def fstree_stress_comms_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFileEdgeCut = csvFolder + "tree4_didic_stress_edge_cut.csv"
    csvFileGLTraf = csvFolder + "tree4_didic_stress_gl_traf.csv"
    filename = 'fstree4_didic_stress_comms_all.pdf'    
    
    def axisYFormatterFunEdgeCut(x, pos=0):
        return '%3.0f\,%s' % (x, r'\%')
    def axisYFormatterFunGLTraf(x, pos=0):
        return '%3.0f\,%s' % (x, r'\%')
        
    stress_comms_all_4_line(csvFolder, csvFileEdgeCut, csvFileGLTraf,
                            axisYFormatterFunEdgeCut=axisYFormatterFunEdgeCut,
                            axisYFormatterFunGLTraf=axisYFormatterFunGLTraf,
                            filename=filename)     



def twitter_stress_gl_traf_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFile = csvFolder + "twitter4_didic_stress_gl_traf.csv"
    filename = 'twitter4_didic_stress_g_l_traf.pdf'    
    def axisYFormatterFun(x, pos=0):
        return '%3.0f' % (x)    

    stress_gl_traf_4_line(csvFolder, csvFile, filename=filename,
                           axisYFormatterFun=axisYFormatterFun,
                           axisYLim=(None, None))     

def twitter_stress_std_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFileNode = csvFolder + "twitter4_didic_stress_std_nodes.csv"
    csvFileRel = csvFolder + "twitter4_didic_stress_std_rels.csv"
    csvFileTraf = csvFolder + "twitter4_didic_stress_std_traf.csv"
    filename = 'twitter4_didic_stress_std_all.pdf'    
    
    def axisYFormatterFunNode(x, pos=0):
        return '%3.1f' % (x)
    def axisYFormatterFunRel(x, pos=0):
        return '%3.0f' % (x)
    def axisYFormatterFunTraf(x, pos=0):
        return '%3.1f' % (x)
        
    stress_std_all_4_line(csvFolder, 
                          csvFileNode, csvFileRel, csvFileTraf,
                          axisYFormatterFunNode=axisYFormatterFunNode,
                          axisYFormatterFunRel=axisYFormatterFunRel,
                          axisYFormatterFunTraf=axisYFormatterFunTraf,
                          axisYLimNode=(1.7,None),
                          axisYLimTraf=(None,None),
                          filename=filename)     

def twitter_stress_comms_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFileEdgeCut = csvFolder + "twitter4_didic_stress_edge_cut.csv"
    csvFileGLTraf = csvFolder + "twitter4_didic_stress_gl_traf.csv"
    filename = 'twitter4_didic_stress_comms_all.pdf'    
    
    def axisYFormatterFunEdgeCut(x, pos=0):
        return '%3.0f\,%s' % (x, r'\%')
    def axisYFormatterFunGLTraf(x, pos=0):
        return '%3.0f\,%s' % (x, r'\%')
        
    stress_comms_all_4_line(csvFolder, csvFileEdgeCut, csvFileGLTraf,
                            axisYFormatterFunEdgeCut=axisYFormatterFunEdgeCut,
                            axisYFormatterFunGLTraf=axisYFormatterFunGLTraf,
                            filename=filename)     


def stress_gl_traf_4_line(csvFolder, csvFile, filename='output.pdf',
                          axisYFormatterFun=None,
                          axisXLim=(-0.2, 26), axisYLim=(None, None),
                          figLeftSpace=defFigLeftSpace,
                          figBottomSpace=defFigBottomSpace,
                          figRightSpace=defFigRightSpace,
                          figTopSpace=defFigTopSpace,
                          figWidth=defFigWidth,
                          figHeight=defFigHeight):
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    def axisXFormatterFun(x, pos=0):
        return '%3d %s' % (x, '$\%$')    
    
    do_fun = get_line_from_file_multi_x(csvFile,
                                        [(csvColumnChurn, csvColumnRand, 'blue', r'Churn', '-', 'o'),
                                         (csvColumnChurn, csvColumnDiDiC, 'red', r'Churn + DiDiC', '-', 'v'), ],
                                         csvFloats=(csvColumnChurn,
                                                    csvColumnRand,
                                                    csvColumnDiDiC,),
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=12, axisColor='k',
                                         axisXLabel=r'Churn', axisYLabel=r'Percentage Global',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLim,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFun,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right',
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    figSize = (figWidth / 2.54, figHeight / 2.54)

    show_plots([[do_fun]],
                show=False,
                fileName=filename,
                figLeftSpace=figLeftSpace,
                figRightSpace=figRightSpace,
                figBottomSpace=figBottomSpace,
                figTopSpace=figTopSpace,
                figSize=figSize)

def stress_std_all_4_line(csvFolder, 
                          csvFileNode, csvFileRel, csvFileTraf,
                          axisYFormatterFunNode=None,
                          axisYFormatterFunRel=None,
                          axisYFormatterFunTraf=None,
                          filename='output.pdf',                          
                          axisXLim=(-0.2, 26), 
                          axisYLimNode=(None, None),
                          axisYLimRel=(None, None),
                          axisYLimTraf=(None, None),
                          figLeftSpace=defFigLeftSpace,
                          figBottomSpace=defFigBottomSpace,
                          figRightSpace=defFigRightSpace,
                          figTopSpace=defFigTopSpace,
                          figWidth=defFigWidth,
                          figHeight=defFigHeight):
    
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    lines = [(csvColumnChurn, csvColumnRand, 'blue', r'Churn', '-', 'o'),
            (csvColumnChurn, csvColumnDiDiC, 'red', r'Churn + DiDiC', '-', 'v')]
    
    csvFloats=(csvColumnChurn,
               csvColumnRand,
               csvColumnDiDiC)

    def axisXFormatterFun(x, pos=0):
        return '%3d\,%s' % (x, '$\%$')    
    
    do_fun1 = get_line_from_file_multi_x(csvFileNode,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=10, axisColor='k',
                                         axisXLabel=None, axisYLabel='Vertex',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimNode,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunNode,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=10, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right', legendBorderPad=0.0,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    do_fun2 = get_line_from_file_multi_x(csvFileRel,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=10, axisColor='k', 
                                         axisXLabel=None, axisYLabel=r'Edge',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimRel,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunRel,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=10, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos=None,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)
        
    do_fun3 = get_line_from_file_multi_x(csvFileTraf,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=10, axisColor='k', 
                                         axisXLabel=r'Churn', axisYLabel=r'Traffic',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimTraf,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunTraf,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=10, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos=None,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)
        
    figSize = (figWidth / 2.54, figHeight / 2.54)

    show_plots([[do_fun1],
                [do_fun2],
                [do_fun3]],
                show=False,
                fileName=filename,
                figWSpace=0.2, 
                figHSpace=0.2,
                figLeftSpace=figLeftSpace,
                figRightSpace=figRightSpace,
                figBottomSpace=figBottomSpace,
                figTopSpace=figTopSpace,
                figSize=figSize)

def stress_comms_all_4_line(csvFolder, 
                            csvFileEdgeCut, csvFileGLTraf,
                            axisYFormatterFunEdgeCut=None,
                            axisYFormatterFunGLTraf=None,
                            filename='output.pdf',                          
                            axisXLim=(-0.2, 26), 
                            axisYLimEdgeCut=(None, None),
                            axisYLimGLTraf=(None, None),
                            figLeftSpace=defFigLeftSpace,
                            figBottomSpace=defFigBottomSpace,
                            figRightSpace=defFigRightSpace,
                            figTopSpace=defFigTopSpace,
                            figWidth=defFigWidth,
                            figHeight=defFigHeight):
    
    csvColumnChurn = "churn"    
    csvColumnRand = "rand"
    csvColumnDiDiC = "didic"
    
    lines = [(csvColumnChurn, csvColumnRand, 'blue', r'Churn', '-', 'o'),
            (csvColumnChurn, csvColumnDiDiC, 'red', r'Churn + DiDiC', '-', 'v')]
    
    csvFloats=(csvColumnChurn,
               csvColumnRand,
               csvColumnDiDiC)
    
    def axisXFormatterFun(x, pos=0):
        return '%3d\,%s' % (x, '$\%$')    
    
    do_fun1 = get_line_from_file_multi_x(csvFileEdgeCut,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=10, axisColor='k', 
                                         axisXLabel=None, axisYLabel='Edge Cut',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimEdgeCut,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunEdgeCut,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=10, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right', legendBorderPad=0.0,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    do_fun2 = get_line_from_file_multi_x(csvFileGLTraf,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisFontSize=10, axisColor='k',
                                         axisXLabel=r'Churn', 
                                         axisYLabel=r'Global Traffic',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimGLTraf,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunGLTraf,
                                         axisXScale='linear', axisYScale='linear',
                                         legendFontsize=10, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos=None,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)
                
    figSize = (figWidth / 2.54, figHeight / 2.54)

    show_plots([[do_fun1],
                [do_fun2]],
                show=False,
                fileName=filename,
                figWSpace=0.2, 
                figHSpace=0.2,
                figLeftSpace=figLeftSpace,
                figRightSpace=figRightSpace,
                figBottomSpace=figBottomSpace,
                figTopSpace=figTopSpace,
                figSize=figSize)
