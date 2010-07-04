from matplotlib import rc
from matplotlib_scripts import *

#dropboxDir = "/media/disk/alex/Dropbox/"
dropboxDir = "/home/alex/Dropbox/"

bucharest_lon = 26.1
bucharest_lat = 44.44    
iasi_lon = 27.590505
iasi_lat = 47.160365
galati_lon = 28.054665
galati_lat = 45.433675
timisoara_lon = 21.223305
timisoara_lat = 45.75343    
constanta_lon = 28.65328
constanta_lat = 44.176975

cities = [('Bucharest', bucharest_lon, bucharest_lat),
         ('Iasi', iasi_lon, iasi_lat),
         ('Galati', galati_lon, galati_lat),
         ('Timisoara', timisoara_lon, timisoara_lat),
         ('Constanta', constanta_lon, constanta_lat)]

def gis_nodes_by_lon_lat(): 
    csvName = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvColumnLon = "raw_nodes_by_lon"
    csvColumnLat = "raw_nodes_by_lat"
            
    axisYmin = 0.0
    axisYmax = 40000.0
    axisFontsize = 12
    
    annotateRotateLon = 'vertical'
    annotateFontsize = 9
    annotateLinewidth = 3
    annotateLinecolor = 'red'#'black'
    annotateLinealpha = 0.5
    annotateLinestyle = '-'
    
    lineYmin = 0.0
    lineYmax = 37000.0
    
    boxStyle = "round,pad=0.2"
    boxFacecolor = '0.9'
    boxEdgecolor = '0.0'
    boxAlpha = 1.0
    boxLinewidth = 0.1
    
    arrowStyle = 'wedge,tail_width=1.'
    arrowFacecolor = '0.9'
    arrowEdgecolor = '0.0'
    arrowAlpha = 1.0
    
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)
    arrow_props = dict(arrowstyle=arrowStyle,
                       fc=arrowFacecolor, ec=arrowEdgecolor, alpha=arrowAlpha,
                       patchA=None)
            
    annotations_lon = []
    
    def get_do_annotation_lon(city_name, city_lon):
        def do_annotation_lon(ax):
            ha = 'center'
            if city_name == 'Iasi':
                ha = 'right'
            if city_name == 'Constanta':
                ha = 'left'
            ax.axvline(x=city_lon, ymin=lineYmin / axisYmax, ymax=lineYmax / axisYmax,
                       linewidth=annotateLinewidth, color=annotateLinecolor,
                       alpha=annotateLinealpha, linestyle=annotateLinestyle)
            
            ax.annotate(city_name, xy=(city_lon + 0.0, lineYmax), #xycoords='data',
                        xytext=(city_lon + 0.0, lineYmax + 1000), #textcoords='offset points',
                        size=annotateFontsize, rotation=annotateRotateLon, ha=ha, va='bottom',
#                        arrowprops=arrow_props,
                        bbox=bbox_props
                        )
        return do_annotation_lon
        
    for (city_name, city_lon, city_lat) in cities:
        annotations_lon += [get_do_annotation_lon(city_name, city_lon)]
        
    def axisXFormatterFunLon(x, pos=0):
        return '%2d%s' % (x, '$^{\circ}$')            

    def axisYFormatterFunLon(x, pos=0):
        return '%1.1F' % (float(x) / 10000.)            
        
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisXLabel=r'Longitude',
                                   axisYLabel=r'Node Count $(\times 10^4)$',
                                   axisYLim=(axisYmin, axisYmax),
                                   axisXFormatterFun=axisXFormatterFunLon,
                                   axisYFormatterFun=axisYFormatterFunLon)

    axisXmin = 0.0
    axisXmax = 30000.0
    
    annotateRotateLat = 'horizontal'
    
    lineXmin = 0.0
    lineXmax = 27000.0
    annotations_lat = []
    
    def get_do_annotation_lat(city_name, city_lat):
        def do_annotation_lat(ax):
            va = 'center'
            if city_name == 'Bucharest' or city_name == 'Timisoara':
                va = 'bottom'
            if city_name == 'Galati' or city_name == 'Constanta':
                va = 'top'
            ax.axhline(y=city_lat, xmin=lineXmin / axisXmax, xmax=lineXmax / axisXmax,
                       linewidth=annotateLinewidth, color=annotateLinecolor,
                       alpha=annotateLinealpha, linestyle=annotateLinestyle)
            
            ax.annotate(city_name, xy=(lineXmax, city_lat + 0.0), #xycoords='data',
                        xytext=(lineXmax + 1000, city_lat + 0.0), #textcoords='offset points',
                        size=annotateFontsize, rotation=annotateRotateLat, ha='left', va=va,
#                        arrowprops=arrow_props,
                        bbox=bbox_props
                        )
        return do_annotation_lat
        
    for (city_name, city_lon, city_lat) in cities:
        annotations_lat += [get_do_annotation_lat(city_name, city_lat)]
        
    def axisYFormatterFunLat(x, pos=0):
        return '%2d%s' % (x, '$^{\circ}$')
                
    def axisXFormatterFunLat(x, pos=0):
        return '%1.1F' % (float(x) / 10000.)
    
    node_lats = get_hist_from_file(csvName, csvColumnLat, annotations=annotations_lat,
                                   csvFloats=(csvColumnLat),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='horizontal', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisYLabel=r'Latitude',
                                   axisXLabel=r'Node Count $(\times 10^4)$',
                                   axisXLim=(axisXmin, axisXmax),
                                   axisXFormatterFun=axisXFormatterFunLat,
                                   axisYFormatterFun=axisYFormatterFunLat)
    
    imgFile = '/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/Romania_map_contour_ale_06r.png'
    do_img_from_file = get_img_from_file(imgFile, annotations=[])

    show_plots([[node_lons, None],
                [do_img_from_file, node_lats]])
    
def gis_nodes_by_lon(): 
    csvName = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvColumnLon = "raw_nodes_by_lon"
    
    axisYmin = 0.0
    axisYmax = 40000.0
    axisFontsize = 12
    
    annotateRotateLon = 'vertical'
    annotateFontsize = 10
    annotateLinewidth = 3
    annotateLinecolor = 'red'
    annotateLinealpha = 0.8
    annotateLinestyle = '-'
    
    lineYmin = 0.0
    lineYmax = 37000.0
    
    boxStyle = "round,pad=0.3"
    boxFacecolor = '0.9'
    boxEdgecolor = '0.0'
    boxAlpha = 1.0
    boxLinewidth = 0.1
    
    arrowStyle = 'wedge,tail_width=1.'
    arrowFacecolor = '0.9'
    arrowEdgecolor = '0.0'
    arrowAlpha = 1.0
    
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)
    arrow_props = dict(arrowstyle=arrowStyle,
                       fc=arrowFacecolor, ec=arrowEdgecolor, alpha=arrowAlpha,
                       patchA=None)
            
    annotations_lon = []
    
    def get_do_annotation_lon(city_name, city_lon):
        def do_annotation_lon(ax):
            ha = 'center'
            if city_name == 'Iasi':
                ha = 'right'
            if city_name == 'Constanta':
                ha = 'left'
            ax.axvline(x=city_lon, ymin=lineYmin / axisYmax, ymax=lineYmax / axisYmax,
                       linewidth=annotateLinewidth, color=annotateLinecolor,
                       alpha=annotateLinealpha, linestyle=annotateLinestyle)
            
            ax.annotate(city_name, xy=(city_lon + 0.0, lineYmax), #xycoords='data',
                        xytext=(city_lon + 0.0, lineYmax + 1000), #textcoords='offset points',
                        size=annotateFontsize, rotation=annotateRotateLon, ha=ha, va='bottom',
#                        arrowprops=arrow_props,
                        bbox=bbox_props
                        )
        return do_annotation_lon
        
    for (city_name, city_lon, _) in cities:
        annotations_lon += [get_do_annotation_lon(city_name, city_lon)]
    
    def axisXFormatterFun(x, pos=0):
        return '%2d%s' % (x, '$^{\circ}$')            
    
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisXLabel=r'Longitude', axisYLabel=r'Node Count',
                                   axisYLim=(axisYmin, axisYmax),
                                   axisXFormatterFun=axisXFormatterFun)

    show_plots([[node_lons]],
               show=False)
    
def gis_nodes_by_lon_ptn(): 
    csvName = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvColumnLon = "raw_nodes_by_lon"
    
    axisYmin = 0.0
    axisYmax = 40000.0
    axisFontsize = 12
    
    annotateRotateLon = 'vertical'
    annotateFontsize = 10
    annotateLinewidth = 3
    annotateLinecolor = 'black'
    annotateLinealpha = 1.0
    annotateLinestyle = '-'
    
    lineYmin = 0.0
    lineYmax = 37000.0
    
    boxStyle = "round,pad=0.3"
    boxFacecolor = '0.9'
    boxEdgecolor = '0.0'
    boxAlpha = 1.0
    boxLinewidth = 0.1
    
    arrowStyle = 'wedge,tail_width=1.'
    arrowFacecolor = '0.9'
    arrowEdgecolor = '0.0'
    arrowAlpha = 1.0
    
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)
    arrow_props = dict(arrowstyle=arrowStyle,
                       fc=arrowFacecolor, ec=arrowEdgecolor, alpha=arrowAlpha,
                       patchA=None)        
    
    partition_alpha = 0.3
    
    annotations_lon = []
    
    def get_do_annotation_lon_ptn(lon_start, lon_end, color):
        def do_annotation_lon_ptn(ax):
            ax.axvspan(lon_start, lon_end, facecolor=color, alpha=partition_alpha)
            
        return do_annotation_lon_ptn
    
    colors = ['red', 'cyan', 'magenta', 'orange']
    
    csvDict = csv_to_dict(csvName, (csvColumnLon), floats=(csvColumnLon))
    minLon = min([lon for lon in csvDict[csvColumnLon]])
    maxLon = max([lon for lon in csvDict[csvColumnLon]])
    
#    rangeLon = maxLon - minLon
#    pSize = float(rangeLon) / float(len(colors))
#    pBoundaries = [(p * pSize + minLon, (p + 1) * pSize + minLon, colors[p]) 
#                   for p in range(len(colors))]

    pBoundaries = [(minLon, 25.54991),
                   (25.54991, maxLon)]
    
#    pBoundaries = [(minLon, 23.6699606),
#                   (23.6699606, 25.54991),
#                   (25.54991, 26.2199546),
#                   (26.2199546, maxLon)]
        
    for ((lon_start, lon_end), color) in zip(pBoundaries, colors):
        annotations_lon += [get_do_annotation_lon_ptn(lon_start, lon_end, color)]
    
    def get_do_annotation_lon(city_name, city_lon):
        def do_annotation_lon(ax):
            ha = 'center'
            if city_name == 'Iasi':
                ha = 'right'
            if city_name == 'Constanta':
                ha = 'left'
            ax.axvline(x=city_lon, ymin=lineYmin / axisYmax, ymax=lineYmax / axisYmax,
                       linewidth=annotateLinewidth, color=annotateLinecolor,
                       alpha=annotateLinealpha, linestyle=annotateLinestyle)
            
            ax.annotate(city_name, xy=(city_lon + 0.0, lineYmax), #xycoords='data',
                        xytext=(city_lon + 0.0, lineYmax + 1000), #textcoords='offset points',
                        size=annotateFontsize, rotation=annotateRotateLon, ha=ha, va='bottom',
#                        arrowprops=arrow_props,
                        bbox=bbox_props
                        )
        return do_annotation_lon
        
    for (city_name, city_lon, _) in cities:
        annotations_lon += [get_do_annotation_lon(city_name, city_lon)]
    
    def axisXFormatterFun(x, pos=0):
        return '%2d%s' % (x, '$^{\circ}$')            

    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisXLabel=r'Longitude', axisYLabel=r'Node Count',
                                   axisYLim=(axisYmin, axisYmax),
                                   axisXFormatterFun=axisXFormatterFun)

    show_plots([[node_lons]])

def gis_deg_stats_all_together(): 
    csvNameRaw = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvNameHist = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_hist.csv"
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    csvColumnDegRaw = "raw_deg"
    csvColumnDegInRaw = "raw_deg_in"
    csvColumnDegOutRaw = "raw_deg_out"
    
    axisXmin = None
    axisXmax = None
    axisFontsize = 12
    barBinCount = 15
    legendAlpha = 0.8

#    axisXmin = 0
#    axisXmax = 10
#    axisFontsize = 12
#    barBinCount = 14

    do_gis_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                       [(csvColumnDegHist, 'blue', None) ], [r'GIS Degree Distribution', ],
                                       csvInts=(csvColumnDegNum, csvColumnDegHist),
                                       annotations=[],
                                       barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                       barAlign='center', barOrientation='vertical', barWidth=1.0,
                                       axisGrid=True, axisFontSize=12, axisColor='k',
                                       axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                       legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                       legendFancybox=False, legendPos='upper right',
                                       myShareAxis='do_gis_deg_bar'
                                       )
        
    do_gis_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ], [r'GIS In-Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          shareAxisX='do_gis_deg_bar'
                                          )

    do_gis_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegOutHist, 'blue', None) ], [r'GIS Out-Degree Distribution', ],
                                            csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=1.0,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisXLabel='Degree', axisYLabel='Node Count',
                                            axisXLim=(axisXmin, axisXmax),
                                            legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                            legendFancybox=False, legendPos='upper right',
                                            shareAxisX='do_gis_deg_bar'
                                            )
    
#    do_gis_deg_hist = get_hist_from_file(csvNameRaw, csvColumnDegRaw, annotations=[],
#                                         barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
#                                         barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=0.5,
#                                         barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
#                                         axisColor='k', axisXLabel=None, axisYLabel=r'Node Count',
#                                         axisName='GIS Degree Distribution', axisXLim=(axisXmin, axisXmax),
#                                         myShareAxis='do_gis_deg_hist')
#
#    do_gis_deg_in_hist = get_hist_from_file(csvNameRaw, csvColumnDegInRaw, annotations=[],
#                                            barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
#                                            barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=1,
#                                            barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
#                                            axisColor='k', axisXLabel=None, axisYLabel=r'Node Count',
#                                            axisName='GIS In-Degree Distribution', axisXLim=(axisXmin, axisXmax),
#                                            myShareAxis='do_gis_deg_in_hist', shareAxisX='do_gis_deg_hist')
#
#    do_gis_deg_out_hist = get_hist_from_file(csvNameRaw, csvColumnDegOutRaw, annotations=[],
#                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
#                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=1,
#                                             barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
#                                             axisColor='k', axisXLabel=r'Degree', axisYLabel=r'Node Count',
#                                             axisName='GIS Out-Degree Distribution', axisXLim=(axisXmin, axisXmax),
#                                             myShareAxis='do_gis_deg_out_hist', shareAxisX='do_gis_deg_hist')

    show_plots([[do_gis_deg_bar],
                [do_gis_deg_in_bar],
                [do_gis_deg_out_bar]],
                show=False,
                figWSpace=0.2, figHSpace=0.3)
    
#    show_plots([[do_gis_deg_hist],
#                [do_gis_deg_in_hist],
#                [do_gis_deg_out_hist]], show=False)

def gis_deg_stats_all_separate(): 
    csvNameRaw = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvNameHist = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_hist.csv"
    csvColumnDegRaw = "raw_deg"
    csvColumnDegInRaw = "raw_deg_in"
    csvColumnDegOutRaw = "raw_deg_out"
    
    axisFontsize = 12
    barBinCount = 15
    legendAlpha = 0.8
        
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    
    do_gis_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                       [(csvColumnDegHist, 'blue', None) ], [r'GIS Degree Distribution', ],
                                       csvInts=(csvColumnDegNum, csvColumnDegHist),
                                       annotations=[],
                                       barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                       barAlign='center', barOrientation='vertical', barWidth=1.0,
                                       axisGrid=True, axisFontSize=12, axisColor='k',
                                       axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 15),
                                       legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                       legendFancybox=False, legendPos='upper right'
                                       )
        
    do_gis_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ], [r'GIS In-Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 8),
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right'
                                          )

    do_gis_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegOutHist, 'blue', None) ], [r'GIS Out-Degree Distribution', ],
                                            csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=1.0,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 8),
                                            legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                            legendFancybox=False, legendPos='upper right'
                                            )
    
#    do_gis_deg_hist = get_hist_from_file(csvNameRaw, csvColumnDegRaw, annotations=[],
#                                         barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
#                                         barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=None, barLog=False,
#                                         barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
#                                         axisColor='k', axisXLabel='Degree', axisYLabel='Node Count',
#                                         axisName='GIS Degree Distribution', axisXLim=(axisXmin, axisXmax))

#    do_gis_deg_in_hist = get_hist_from_file(csvNameRaw, csvColumnDegInRaw, annotations=[],
#                                            barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
#                                            barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=None,
#                                            barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
#                                            axisColor='k', axisXLabel='Degree', axisYLabel='Node Count',
#                                            axisName='GIS In-Degree Distribution')

#    do_gis_deg_out_hist = get_hist_from_file(csvNameRaw, csvColumnDegOutRaw, annotations=[],
#                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
#                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=None,
#                                             barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
#                                             axisColor='k', axisXLabel='Degree', axisYLabel='Node Count',
#                                             axisName='GIS Out-Degree Distribution')

    show_plots([[do_gis_deg_bar]], fileName="output1.pdf", show=False)
    show_plots([[do_gis_deg_in_bar]], fileName="output2.pdf", show=False)
    show_plots([[do_gis_deg_out_bar]], fileName="output3.pdf", show=False)
    
#    show_plots([[do_gis_deg_hist]], fileName="output.pdf", show=False)
#    show_plots([[do_gis_deg_in_hist]], fileName="output.pdf", show=False)
#    show_plots([[do_gis_deg_out_hist]], fileName="output.pdf", show=False)



def fstree_deg_stats_all_together(): 
    csvNameHist = dropboxDir + "Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_tree_hist.csv"
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"

    axisXmin = None
    axisXmax = None
    axisFontsize = 12
    
    legendAlpha = 0.8
    
    def axisXFormatterFun(x):
        if int(x) % 2 == 0:
            return x
        else:
            return ''
    
    do_fstree_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegHist, 'blue', None) ], [r'FS-Tree Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                          axisXFormatterFun=axisXFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis='do_gis_deg_bar'
                                       )
        
    do_fstree_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ], [r'FS-Tree In-Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                          axisXFormatterFun=axisXFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          shareAxisX='do_gis_deg_bar'
                                          )

    do_fstree_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                              [(csvColumnDegOutHist, 'blue', None) ], [r'FS-Tree Out-Degree Distribution', ],
                                              csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                              annotations=[],
                                              barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                              barAlign='center', barOrientation='vertical', barWidth=1.0,
                                              axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                              axisXLabel='Degree', axisYLabel='Node Count',
                                              axisXLim=(axisXmin, axisXmax),
                                              axisXFormatterFun=axisXFormatterFun,
                                              legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                              legendFancybox=False, legendPos='upper right',
                                              shareAxisX='do_gis_deg_bar'
                                              )
    
    show_plots([[do_fstree_deg_bar],
                [do_fstree_deg_in_bar],
                [do_fstree_deg_out_bar]],
                show=False,
                figWSpace=0.2, figHSpace=0.3)
    
def fstree_deg_stats_all_separate(): 
    csvNameHist = dropboxDir + "Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv"
    
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    
    axisFontsize = 12
        
    legendAlpha = 0.8
        
    def axisXFormatterFun(x):
        if int(x) % 2 == 0:
            return x
        else:
            return ''
        
    do_fstree_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegHist, 'blue', None) ], [r'FS-Tree Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 38),
                                          axisXFormatterFun=axisXFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right'
                                          )
        
    do_fstree_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                             [(csvColumnDegInHist, 'blue', None) ], [r'FS-Tree In-Degree Distribution', ],
                                             csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                             annotations=[],
                                             barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                             barAlign='center', barOrientation='vertical', barWidth=1.0,
                                             axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                             axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 8),
                                             axisXFormatterFun=axisXFormatterFun,
                                             legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                             legendFancybox=False, legendPos='upper right'
                                             )

    do_fstree_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                              [(csvColumnDegOutHist, 'blue', None) ], [r'FS-Tree Out-Degree Distribution', ],
                                              csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                              annotations=[],
                                              barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                              barAlign='center', barOrientation='vertical', barWidth=1.0,
                                              axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                              axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 34),
                                              axisXFormatterFun=axisXFormatterFun,
                                              legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                              legendFancybox=False, legendPos='upper right'
                                              )
    
    show_plots([[do_fstree_deg_bar]], fileName="output1.pdf", show=False)
    show_plots([[do_fstree_deg_in_bar]], fileName="output2.pdf", show=False)
    show_plots([[do_fstree_deg_out_bar]], fileName="output3.pdf", show=False)

def fstree_nodes_at_level(): 
    csvNameHist = dropboxDir + "Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv"
    
    csvColumnTreeLevel = "tree_level"
    csvColumnTreeLevelNodes = "tree_level_nodes"
    
    axisFontsize = 12
    
    legendAlpha = 0.8
        
    def axisYFormatterFun(x):
        if int(x) % 2 == 0:
            return x
        else:
            return ''
    do_fstree_levels_barh = get_barh_from_file(csvNameHist, csvColumnTreeLevel,
                                               [(csvColumnTreeLevelNodes, 'blue') ],
                                               [r'FS-Tree Nodes at Tree Level', ],
                                               csvInts=(csvColumnTreeLevel, csvColumnTreeLevelNodes),
                                               annotations=[],
                                               barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                               barAlign='center', barOrientation='horizontal', barWidth=1.0,
                                               axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                               axisYLabel='Tree Level', axisXLabel='Node Count',
                                               axisXLim=(None, None), axisYLim=(None, None),
                                               axisReverseY=True,
#                                               axisYFormatterFun=axisYFormatterFun,
                                               legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                               legendFancybox=False, legendPos='upper right'
                                              )
            
    show_plots([[do_fstree_levels_barh]],
               fileName="output.pdf",
               show=False)

def fstree_nodes_at_level_annotated(levelAlpha=0.3): 

    csvNameHist = dropboxDir + "Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv"
    
    csvColumnTreeLevel = "tree_level"
    csvColumnTreeLevelNodes = "tree_level_nodes"
    
    axisFontsize = 12
    
    legendAlpha = 0.8
    
    annotations_level_shading = []
    
    def get_do_annotation_level_shading(level_start, level_end, color):
        def do_annotation_level_shading(ax):
            ax.axhspan(level_start, level_end, facecolor=color, alpha=levelAlpha)
            
        return do_annotation_level_shading
    
#    0 reference node
#    1 reference organisiations
#    2 organisations
#    3 user
#    4 user root
#    5 ... folder files and other stuff

    shading = ['cyan', 'magenta', 'green', 'orange', 'gray', 'yellow']
    shadingBoundaries = [(0.1, 10), # 1-3 Orgs
                         (10, 12), # 4-5 Users
                         (12, 15.9)] # 6-15 Folders & Files
    
    for ((level_start, level_end), color) in zip(shadingBoundaries, shading):
        annotations_level_shading += [get_do_annotation_level_shading(level_start, level_end, color)]
        
    annotateRotate = 'horizontal'
    annotateFontsize = 10
    boxStyle = "round,pad=0.5"
    boxFacecolor = '0.9'
    boxEdgecolor = '0.0'
    boxAlpha = 1.0    
    boxLinewidth = 0.5
        
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)
    
    def get_do_annotation_level_line(level, value):
        def do_annotation_level_line(ax):            
            ax.annotate(value, xy=(205000, level), xytext=(210000, level),
                        size=annotateFontsize, rotation=annotateRotate,
                        ha='right', va='center',
                        bbox=bbox_props)

        return do_annotation_level_line

    for (level, value) in [(5.5, 'Files \& Folders\n250,000 Nodes'),
                           (11, 'Users\n5 Nodes'),
                           (14, 'Organisations\n5 Nodes')]:
        annotations_level_shading += [get_do_annotation_level_line(level, value)]
        
    def axisYFormatterFun(x):
        if int(x) % 2 == 0:
            return x
        else:
            return ''

    do_fstree_levels_barh = get_barh_from_file(csvNameHist, csvColumnTreeLevel,
                                               [(csvColumnTreeLevelNodes, 'blue') ],
                                               [r'FS-Tree Nodes at Tree Level', ],
                                               csvInts=(csvColumnTreeLevel, csvColumnTreeLevelNodes),
                                               annotations=annotations_level_shading,
                                               barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                               barAlign='center', barOrientation='horizontal',
                                               barHeight=1.0, barLog=False, barReverse=True,
                                               axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                               axisYLabel='Tree Level', axisXLabel='Node Count',
                                               axisXLim=(0, 220000), axisYLim=(None, None),
#                                               axisYFormatterFun=axisYFormatterFun,
                                               legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                               legendFancybox=False, legendPos='upper right'
                                              )
            
    show_plots([[do_fstree_levels_barh]],
               fileName="output.pdf",
               show=False)



def twitter_deg_stats_all_together(): 
    csvNameRaw = dropboxDir + "Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_raw.csv"
    csvNameHistDeg = dropboxDir + "Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_hist.csv"
    csvNameHistStats = dropboxDir + "Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_stats_hist.csv"
    
    csvColumnDegRaw = "raw_deg_256" 
    csvColumnDegInRaw = "raw_deg_in_256"
    csvColumnDegOutRaw = "raw_deg_out_256"

    axisXmin = None
    axisXmax = None
    
    barBinCount = 100
    barRWidth = None #0.5
    axisFontsize = 12
    legendAlpha = 0.8
    
    do_twitter_deg_hist = get_hist_from_file(csvNameRaw, csvColumnDegRaw, annotations=[],
                                             csvInts=(csvColumnDegRaw),
                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=barRWidth,
                                             barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisXLabel='', axisYLabel=r'Node Count',
                                             axisName='Twitter Degree Distribution', axisXLim=(axisXmin, axisXmax),
                                             legendAlpha=legendAlpha,
                                             myShareAxis='do_twitter_deg_hist'
                                             )

    do_twitter_deg_in_hist = get_hist_from_file(csvNameRaw, csvColumnDegInRaw, annotations=[],
                                                csvInts=(csvColumnDegInRaw),
                                                barBinCount=(1400. / 2000.) * barBinCount, barFacecolor='blue',
                                                barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                                barRWidth=barRWidth, barOrientation='vertical', barLog=True,
                                                axisGrid=True, axisFontSize=axisFontsize,
                                                axisColor='k', axisXLabel='', axisYLabel=r'Node Count',
                                                axisName='Twitter In-Degree Distribution', axisXLim=(axisXmin, axisXmax),
                                                legendAlpha=legendAlpha,
                                                shareAxisX='do_twitter_deg_hist'
                                                )

    do_twitter_deg_out_hist = get_hist_from_file(csvNameRaw, csvColumnDegOutRaw, annotations=[],
                                             csvInts=(csvColumnDegOutRaw),
                                             barBinCount=(700. / 2000.) * barBinCount, barFacecolor='blue',
                                             barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                             barRWidth=1, barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisXLabel=r'Degree', axisYLabel=r'Node Count',
                                             axisName='Twitter Out-Degree Distribution', axisXLim=(axisXmin, axisXmax),
                                             legendAlpha=legendAlpha,
                                             shareAxisX='do_twitter_deg_hist'
                                             )

    show_plots([
                [do_twitter_deg_hist],
                [do_twitter_deg_in_hist],
                [do_twitter_deg_out_hist]],
                show=False,
                figWSpace=0.2, figHSpace=0.3)

def twitter_deg_stats_all_separate(): 
    csvNameRaw = dropboxDir + "Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_raw.csv"
    csvNameHistDeg = dropboxDir + "Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_hist.csv"
    
    csvColumnDegRaw = "raw_deg_256" 
    csvColumnDegInRaw = "raw_deg_in_256"
    csvColumnDegOutRaw = "raw_deg_out_256"
    
    csvColumnDegNum = "deg_256"
    csvColumnDegHist = "hist_deg_256"

    axisXmin = None
    axisXmax = None
    
    barBinCount = 100
    barRWidth = None #0.5
    axisFontsize = 12
    legendAlpha = 0.8 
    
#    do_twitter_deg_bar = get_bar_from_file(csvNameHistDeg, csvColumnDegNum,
#                                           [(csvColumnDegHist, 'blue',None) ], [r'Twitter Degree Distribution', ],
#                                           csvInts=(csvColumnDegNum, csvColumnDegHist),
#                                           annotations=[],
#                                           barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
#                                           barAlign='center', barOrientation='vertical', barWidth=1.0,
#                                           barLog=True,
#                                           axisGrid=True, axisFontSize=12, axisColor='k',
#                                           axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
#                                           legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
#                                           legendFancybox=False, legendPos='upper right'
#                                           )
    
    do_twitter_deg_hist = get_hist_from_file(csvNameRaw, csvColumnDegRaw, annotations=[],
                                             csvInts=(csvColumnDegRaw),
                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=barRWidth,
                                             barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisXLabel=r'Degree', axisYLabel=r'Node Count',
                                             axisName='Twitter Degree Distribution', axisXLim=(axisXmin, axisXmax),
                                             legendAlpha=legendAlpha)

    do_twitter_deg_in_hist = get_hist_from_file(csvNameRaw, csvColumnDegInRaw, annotations=[],
                                                csvInts=(csvColumnDegInRaw),
                                                barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                                barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=barRWidth,
                                                barOrientation='vertical', barLog=True,
                                                axisGrid=True, axisFontSize=axisFontsize,
                                                axisColor='k', axisXLabel=r'Degree', axisYLabel=r'Node Count',
                                                axisName='Twitter In-Degree Distribution', axisXLim=(axisXmin, axisXmax),
                                                legendAlpha=legendAlpha)

    do_twitter_deg_out_hist = get_hist_from_file(csvNameRaw, csvColumnDegOutRaw, annotations=[],
                                             csvInts=(csvColumnDegOutRaw),
                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=1,
                                             barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisXLabel=r'Degree', axisYLabel=r'Node Count',
                                             axisName='Twitter Out-Degree Distribution', axisXLim=(axisXmin, axisXmax),
                                             legendAlpha=legendAlpha)

#    show_plots([[do_twitter_deg_bar]],
#                show=False,
#                fileName="output0.pdf")
    
    show_plots([[do_twitter_deg_hist]],
                show=False,
                fileName="output1.pdf")

    show_plots([[do_twitter_deg_in_hist]],
                show=False,
                fileName="output2.pdf")
    
    show_plots([[do_twitter_deg_out_hist]],
                show=False,
                fileName="output3.pdf")



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

def gis_long_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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

def gis_long_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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

def gis_short_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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

def gis_short_perc_gtraf_2():
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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
    csvFolder = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/InitialPartitioning_Balance/"
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
    csvFolder = dropboxDir + "/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
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
    csvFolder = dropboxDir + "/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
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
    csvFolder = dropboxDir + "/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
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
    csvFolder = dropboxDir + "/Neo_Thesis/Notes/evaluation results/Twitter/InitialPartitioning/"
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
