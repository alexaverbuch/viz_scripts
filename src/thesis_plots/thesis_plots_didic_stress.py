from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

defFigWidth3 = 9.0
defFigHeight3 = 9.0
defFigLeftSpace3 = 0.16
defFigBottomSpace3 = 0.10
defFigRightSpace3 = 0.99
defFigTopSpace3 = 0.88

defFigWidth2 = 9.0
defFigHeight2 = 7.0
defFigLeftSpace2 = 0.16
defFigBottomSpace2 = 0.13
defFigRightSpace2 = 0.98
defFigTopSpace2 = 0.85


def gis_stress_std_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Stress/"
    csvFileNode = csvFolder + "gis4_didic_stress_std_nodes.csv"
    csvFileRel = csvFolder + "gis4_didic_stress_std_rels.csv"
    csvFileTraf = csvFolder + "gis4_didic_stress_std_traf.csv"
    filename = 'gis4_didic_stress_std_all.pdf'    
    
    def axisYFormatterFunNode(x, pos=0):
        return '%3.2f' % (x)
    def axisYFormatterFunRel(x, pos=0):
        return '%3.2f' % (x)
    def axisYFormatterFunTraf(x, pos=0):
        return '%3.2f' % (x)
        
    stress_std_all_4_line(csvFolder, 
                          csvFileNode, csvFileRel, csvFileTraf,
                          axisYFormatterFunNode=axisYFormatterFunNode,
                          axisYFormatterFunRel=axisYFormatterFunRel,
                          axisYFormatterFunTraf=axisYFormatterFunTraf,
                          axisYLimNode=(None,0.246),
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



def fstree_stress_std_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Stress/"
    csvFileNode = csvFolder + "tree4_didic_stress_std_nodes.csv"
    csvFileRel = csvFolder + "tree4_didic_stress_std_rels.csv"
    csvFileTraf = csvFolder + "tree4_didic_stress_std_traf.csv"
    filename = 'fstree4_didic_stress_std_all.pdf'    
    
    def axisYFormatterFunNode(x, pos=0):
        return '%3.3f' % (x)
    def axisYFormatterFunRel(x, pos=0):
        return '%3.3f' % (x)
    def axisYFormatterFunTraf(x, pos=0):
        return '%3.2f' % (x)
        
    stress_std_all_4_line(csvFolder, 
                          csvFileNode, csvFileRel, csvFileTraf,
                          axisYFormatterFunNode=axisYFormatterFunNode,
                          axisYFormatterFunRel=axisYFormatterFunRel,
                          axisYFormatterFunTraf=axisYFormatterFunTraf,
                          axisYLimNode=(None,None),
                          axisYLimRel=(None,0.13),
                          axisYLimTraf=(None,0.24),
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



def twitter_stress_std_all_4():
    csvFolder = r"/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Stress/"
    csvFileNode = csvFolder + "twitter4_didic_stress_std_nodes.csv"
    csvFileRel = csvFolder + "twitter4_didic_stress_std_rels.csv"
    csvFileTraf = csvFolder + "twitter4_didic_stress_std_traf.csv"
    filename = 'twitter4_didic_stress_std_all.pdf'    
    
    def axisYFormatterFunNode(x, pos=0):
        return '%3.1f' % (x)
    def axisYFormatterFunRel(x, pos=0):
        return '%3.1f' % (x)
    def axisYFormatterFunTraf(x, pos=0):
        return '%3.0f' % (x)
        
    stress_std_all_4_line(csvFolder, 
                          csvFileNode, csvFileRel, csvFileTraf,
                          axisYFormatterFunNode=axisYFormatterFunNode,
                          axisYFormatterFunRel=axisYFormatterFunRel,
                          axisYFormatterFunTraf=axisYFormatterFunTraf,
                          axisYLimNode=(None,None),
                          axisYLimRel=(None,8.2),
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
                          figLeftSpace=defFigLeftSpace3,
                          figBottomSpace=defFigBottomSpace3,
                          figRightSpace=defFigRightSpace3,
                          figTopSpace=defFigTopSpace3,
                          figWidth=defFigWidth3,
                          figHeight=defFigHeight3):
    
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
                                         axisColor='k',
                                         axisXLabel=None, axisYLabel='Vertex',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimNode,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunNode,
                                         axisXScale='linear', axisYScale='linear',
                                         legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right', legendBorderAxesPad=0.0,
                                         legendBorderPad=0.3, legendLabelSpace=0.2,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    do_fun2 = get_line_from_file_multi_x(csvFileRel,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisColor='k', 
                                         axisXLabel=None, axisYLabel=r'Edge',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimRel,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunRel,
                                         axisXScale='linear', axisYScale='linear',
                                         legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos=None,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)
        
    do_fun3 = get_line_from_file_multi_x(csvFileTraf,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisColor='k', 
                                         axisXLabel=r'Churn', axisYLabel=r'Traffic',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimTraf,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunTraf,
                                         axisXScale='linear', axisYScale='linear',
                                         legendAlpha=0.8, legendShadow=False, legendColor='w',
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
                            figLeftSpace=defFigLeftSpace2,
                            figBottomSpace=defFigBottomSpace2,
                            figRightSpace=defFigRightSpace2,
                            figTopSpace=defFigTopSpace2,
                            figWidth=defFigWidth2,
                            figHeight=defFigHeight2):
    
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
                                         axisColor='k', 
                                         axisXLabel=None, axisYLabel='Edge Cut',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimEdgeCut,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunEdgeCut,
                                         axisXScale='linear', axisYScale='linear',
                                         legendAlpha=0.8, legendShadow=False, legendColor='w',
                                         legendFancybox=False, legendPos='upper right', legendBorderAxesPad=0.0,
                                         legendBorderPad=0.3, legendLabelSpace=0.2,
                                         myShareAxis=None, shareAxisX=None, shareAxisY=None)    
    
    do_fun2 = get_line_from_file_multi_x(csvFileGLTraf,
                                         lines,
                                         csvFloats=csvFloats,
                                         annotations=[],
                                         axisLineWidth=1.0, axisGrid=True, axisLineAntialiased=True,
                                         axisColor='k',
                                         axisXLabel=r'Churn', 
                                         axisYLabel=r'Global Traffic',
                                         axisTitle='', axisXLim=axisXLim, axisYLim=axisYLimGLTraf,
                                         axisXFormatterFun=axisXFormatterFun, axisYFormatterFun=axisYFormatterFunGLTraf,
                                         axisXScale='linear', axisYScale='linear',
                                         legendAlpha=0.8, legendShadow=False, legendColor='w',
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
