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
    
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisXLabel=r'Longitude', axisYLabel=r'Node Count',
                                   axisYLim=(axisYmin, axisYmax))

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
        
    node_lats = get_hist_from_file(csvName, csvColumnLat, annotations=annotations_lat,
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='horizontal', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisXLabel=r'Node Count', axisYLabel=r'Latitude',
                                   axisXLim=(axisXmin, axisXmax))
    
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
    
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisXLabel=r'Longitude', axisYLabel=r'Node Count',
                                   axisYLim=(axisYmin, axisYmax))

    show_plots([[node_lons]])
    
def gis_nodes_by_lon_ptn(partitions=['red', 'cyan', 'magenta', 'orange']): 
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
    
    csvDict = csv_to_dict(csvName)
    minLon = min([lon for lon in csvDict[csvColumnLon]])
    maxLon = max([lon for lon in csvDict[csvColumnLon]])
    rangeLon = maxLon - minLon
    pSize = float(rangeLon) / float(len(partitions))
    pBoundaries = [(p * pSize + minLon, (p + 1) * pSize + minLon, partitions[p]) 
                   for p in range(len(partitions))]
    
    for (lon_start, lon_end, color) in pBoundaries:
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
    
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisXLabel=r'Longitude', axisYLabel=r'Node Count',
                                   axisYLim=(axisYmin, axisYmax))

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

#    axisXmin = 0
#    axisXmax = 10
#    axisFontsize = 12
#    barBinCount = 14

    do_gis_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                       [(csvColumnDegHist, 'blue') ], [r'GIS Degree Distribution', ],
                                       csvInts=(csvColumnDegNum, csvColumnDegHist),
                                       annotations=[],
                                       barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                       barAlign='center', barOrientation='vertical', barWidth=1.0,
                                       axisGrid=True, axisFontSize=12, axisColor='k',
                                       axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                       legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                                       legendFancybox=False, legendPos='upper right',
                                       myShareAxis='do_gis_deg_bar'
                                       )
        
    do_gis_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue') ], [r'GIS In-Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                          legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          shareAxisX='do_gis_deg_bar'
                                          )

    do_gis_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegOutHist, 'blue') ], [r'GIS Out-Degree Distribution', ],
                                            csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=1.0,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisXLabel='Degree', axisYLabel='Node Count',
                                            axisXLim=(axisXmin, axisXmax),
                                            legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
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
        
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    
    do_gis_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                       [(csvColumnDegHist, 'blue') ], [r'GIS Degree Distribution', ],
                                       csvInts=(csvColumnDegNum, csvColumnDegHist),
                                       annotations=[],
                                       barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                       barAlign='center', barOrientation='vertical', barWidth=1.0,
                                       axisGrid=True, axisFontSize=12, axisColor='k',
                                       axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 15),
                                       legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                                       legendFancybox=False, legendPos='upper right'
                                       )
        
    do_gis_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue') ], [r'GIS In-Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 8),
                                          legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right'
                                          )

    do_gis_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegOutHist, 'blue') ], [r'GIS Out-Degree Distribution', ],
                                            csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                            annotations=[],
                                            barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                            barAlign='center', barOrientation='vertical', barWidth=1.0,
                                            axisGrid=True, axisFontSize=12, axisColor='k',
                                            axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 8),
                                            legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
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
    
    def axisXFormatterFun(x):
        if int(x) % 2 == 0:
            return x
        else:
            return ''
    
    do_fstree_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegHist, 'blue') ], [r'FS-Tree Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                          axisXFormatterFun=axisXFormatterFun,
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis='do_gis_deg_bar'
                                       )
        
    do_fstree_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue') ], [r'FS-Tree In-Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisYLabel='Node Count', axisXLim=(axisXmin, axisXmax),
                                          axisXFormatterFun=axisXFormatterFun,
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          shareAxisX='do_gis_deg_bar'
                                          )

    do_fstree_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                              [(csvColumnDegOutHist, 'blue') ], [r'FS-Tree Out-Degree Distribution', ],
                                              csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                              annotations=[],
                                              barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                              barAlign='center', barOrientation='vertical', barWidth=1.0,
                                              axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                              axisXLabel='Degree', axisYLabel='Node Count',
                                              axisXLim=(axisXmin, axisXmax),
                                              axisXFormatterFun=axisXFormatterFun,
                                              legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
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
        
    def axisXFormatterFun(x):
        if int(x) % 2 == 0:
            return x
        else:
            return ''
        
    do_fstree_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegHist, 'blue') ], [r'FS-Tree Degree Distribution', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 38),
                                          axisXFormatterFun=axisXFormatterFun,
                                          legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right'
                                          )
        
    do_fstree_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                             [(csvColumnDegInHist, 'blue') ], [r'FS-Tree In-Degree Distribution', ],
                                             csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                             annotations=[],
                                             barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                             barAlign='center', barOrientation='vertical', barWidth=1.0,
                                             axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                             axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 8),
                                             axisXFormatterFun=axisXFormatterFun,
                                             legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                             legendFancybox=False, legendPos='upper right'
                                             )

    do_fstree_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                              [(csvColumnDegOutHist, 'blue') ], [r'FS-Tree Out-Degree Distribution', ],
                                              csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                              annotations=[],
                                              barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                              barAlign='center', barOrientation='vertical', barWidth=1.0,
                                              axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                              axisXLabel='Degree', axisYLabel='Node Count', axisXLim=(0, 34),
                                              axisXFormatterFun=axisXFormatterFun,
                                              legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
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
                                               legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
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
                           (11, 'Users\n10 Nodes'),
                           (14, 'Organisations\n7 Nodes')]:
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
                                               legendFontsize=12, legendAlpha=0.8, legendShadow=False, legendColor='w',
                                               legendFancybox=False, legendPos='upper right'
                                              )
            
    show_plots([[do_fstree_levels_barh]],
               fileName="output.pdf",
               show=False)
