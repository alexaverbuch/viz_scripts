import math
from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

defFigWidth = 10.0
defFigHeight = 9.0
defFigLeftSpace = 0.12
defFigBottomSpace = 0.11
defFigRightSpace = 0.98
defFigTopSpace = 0.96
defAxisGrid = False
defBarAlpha = 1.0

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
    csvName = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvColumnLon = "raw_nodes_by_lon"
    csvColumnLat = "raw_nodes_by_lat"
    
    barRWidth=None
            
    axisYmin = 0.0
    axisYmax = 40000.0
    axisFontsize = 10
    
    annotateRotateLon = 'vertical'
    annotateFontsize = 8
    annotateLinewidth = 3
    annotateLinecolor = 'red'#'black'
    annotateLinealpha = 0.6
    annotateLinestyle = '-'
    
    lineYmin = 0.0
    lineYmax = 37000.0
    
    boxStyle = "round,pad=0.2"
    boxFacecolor = '0.9'
    boxEdgecolor = '0.0'
    boxAlpha = 1.0
    boxLinewidth = 0.1
    
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)

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
        return '%1.1f' % (float(x) / 10000.)
            
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='blue',
                                   barHisttype='bar', barAlpha=defBarAlpha, barAlign='mid',
                                   barOrientation='vertical', barRWidth=barRWidth, 
                                   axisGrid=defAxisGrid, 
                                   axisFontSize=axisFontsize, axisColor='k',
                                   axisXLabel=r'Longitude',
                                   axisYLabel=r'Vertex Count $(\times 10^4)$',
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
        return '%1.1f' % (float(x) / 10000.)
    
    node_lats = get_hist_from_file(csvName, csvColumnLat, annotations=annotations_lat,
                                   csvFloats=(csvColumnLat),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='blue',
                                   barHisttype='bar', barAlpha=defBarAlpha, barAlign='mid',
                                   barOrientation='horizontal', barRWidth=barRWidth, 
                                   axisGrid=defAxisGrid, 
                                   axisFontSize=axisFontsize, axisColor='k',
                                   axisYLabel=r'Latitude',
                                   axisXLabel=r'Vertex Count $(\times 10^4)$',
                                   axisXLim=(axisXmin, axisXmax),
                                   axisXFormatterFun=axisXFormatterFunLat,
                                   axisYFormatterFun=axisYFormatterFunLat)
    
    imgFile = '/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/Romania_map_contour_ale_06r.png'
    do_img_from_file = get_img_from_file(imgFile, annotations=[])

    figWidth = 13.0
    figHeight = 11.0
    figLeftSpace = 0.10
    figBottomSpace = 0.11
    figRightSpace = 0.90
    figTopSpace = 0.88

    figSize = (figWidth / 2.54, figHeight / 2.54)
    
    show_plots([[node_lons, None],
                [do_img_from_file, node_lats]],
                show=False,
                fileName='gis_density_map_lon_lat.pdf',
                figWSpace=0.25,
                figHSpace=0.22,
                figLeftSpace=figLeftSpace,
                figRightSpace=figRightSpace,
                figBottomSpace=figBottomSpace,
                figTopSpace=figTopSpace,
                figSize=figSize)
    
def gis_nodes_by_lon(): 
    csvName = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvColumnLon = "raw_nodes_by_lon"
    
    axisYmin = 0.0
    axisYmax = 40000.0
    axisFontsize = 10
    
    annotateRotateLon = 'vertical'
    annotateFontsize = 8
    annotateLinewidth = 3
    annotateLinecolor = 'red'
    annotateLinealpha = 0.8
    annotateLinestyle = '-'
    
    lineYmin = 0.0
    lineYmax = 37000.0
    
    boxStyle = "round,pad=0.2"
    boxFacecolor = '0.9'
    boxEdgecolor = '0.0'
    boxAlpha = 1.0
    boxLinewidth = 0.1
    
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)
            
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
    
    def axisYFormatterFun(x, pos=0):
        return '%1.1f' % (float(x) / 10000.)
    
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=defBarAlpha, barAlign='mid',
                                   barOrientation='vertical', axisGrid=defAxisGrid, axisFontSize=axisFontsize,
                                   axisColor='k',
                                   axisXLabel=r'Longitude',
                                   axisYLabel=r'Vertices $(\times 10^4)$',
                                   axisYLim=(axisYmin, axisYmax),
                                   axisXFormatterFun=axisXFormatterFun,
                                   axisYFormatterFun=axisYFormatterFun)

    figWidth = 8.0
    figHeight = 7.0
    figLeftSpace = 0.15
    figBottomSpace = 0.13
    figRightSpace = 0.95
    figTopSpace = 0.80

    figSize = (figWidth / 2.54, figHeight / 2.54)
    
    show_plots([[node_lons]],
               show=False,
               fileName='gis_density_lon.pdf',
               figWSpace=0.20,
               figHSpace=0.20,
               figLeftSpace=figLeftSpace,
               figRightSpace=figRightSpace,
               figBottomSpace=figBottomSpace,
               figTopSpace=figTopSpace,
               figSize=figSize)
    
def gis_nodes_by_lon_ptn(): 
    csvName = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
    csvColumnLon = "raw_nodes_by_lon"
    
    axisYmin = 0.0
    axisYmax = 40000.0
    axisFontsize = 10
    
    annotateRotateLon = 'vertical'
    annotateFontsize = 8
    annotateLinewidth = 1.5
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
    
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)
    
    partition_alpha = 0.3
    
    annotations_lon2 = []
    annotations_lon4 = []
    
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
#    pBoundaries2 = [(p * pSize + minLon, (p + 1) * pSize + minLon, colors[p]) 
#                   for p in range(len(colors))]

    pBoundaries2 = [(minLon, 25.54991),
                   (25.54991, maxLon)]
    
    for ((lon_start, lon_end), color) in zip(pBoundaries2, colors):
        annotations_lon2 += [get_do_annotation_lon_ptn(lon_start, lon_end, color)]
    
    def get_do_annotation_lon(city_name, city_lon):
        def do_annotation_lon2(ax):
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
        return do_annotation_lon2
        
    for (city_name, city_lon, _) in cities:
        annotations_lon2 += [get_do_annotation_lon(city_name, city_lon)]
    
    def axisXFormatterFun(x, pos=0):
        return '%2d%s' % (x, '$^{\circ}$')            

    def axisYFormatterFun(x, pos=0):
        return '%1.1f' % (float(x) / 10000.)
    
    node_lons2 = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon2,
                                    csvFloats=(csvColumnLon),
                                    barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                    barHisttype='bar', barAlpha=defBarAlpha, barAlign='mid',
                                    barOrientation='vertical', axisGrid=defAxisGrid, axisFontSize=axisFontsize,
                                    axisColor='k', axisXLabel='',
                                    axisYLabel=r'Vertices $(\times 10^4)$',
                                    axisYLim=(axisYmin, axisYmax),
                                    axisXFormatterFun=axisXFormatterFun,
                                    axisYFormatterFun=axisYFormatterFun)

    pBoundaries4 = [(minLon, 23.6699606),
                   (23.6699606, 25.54991),
                   (25.54991, 26.2199546),
                   (26.2199546, maxLon)]
        
    for ((lon_start, lon_end), color) in zip(pBoundaries4, colors):
        annotations_lon4 += [get_do_annotation_lon_ptn(lon_start, lon_end, color)]
            
    for (city_name, city_lon, _) in cities:
        annotations_lon4 += [get_do_annotation_lon(city_name, city_lon)]
    
    node_lons4 = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon4,
                                    csvFloats=(csvColumnLon),
                                    barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                    barHisttype='bar', barAlpha=defBarAlpha, barAlign='mid',
                                    barOrientation='vertical', axisGrid=defAxisGrid, axisFontSize=axisFontsize,
                                    axisColor='k',
                                    axisXLabel=r'Longitude',
                                    axisYLabel=r'Vertices $(\times 10^4)$',
                                    axisYLim=(axisYmin, axisYmax),
                                    axisXFormatterFun=axisXFormatterFun,
                                    axisYFormatterFun=axisYFormatterFun)

    figWidth = 10.0
    figHeight = 10.0
    figLeftSpace = 0.12
    figBottomSpace = 0.10
    figRightSpace = 0.95
    figTopSpace = 0.86

    figSize = (figWidth / 2.54, figHeight / 2.54)
    
    show_plots([[node_lons2],
                [node_lons4]],
               show=False,
               fileName='gis_partition_lon_balanced.pdf',
               figWSpace=0.20,
               figHSpace=0.65,
               figLeftSpace=figLeftSpace,
               figRightSpace=figRightSpace,
               figBottomSpace=figBottomSpace,
               figTopSpace=figTopSpace,
               figSize=figSize)

def gis_deg_stats_all_together(): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_hist.csv"
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    
    legendAlpha = 0.8

    def axisXFormatterFun(x, pos=0):
        return '%s' % (x)            

    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '$10^%d$' % (math.ceil(math.log(x, 10)))

    do_gis_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                       [(csvColumnDegHist, 'blue', None) ],
                                       [  r'GIS Degree', ],
                                       csvInts=(csvColumnDegNum, csvColumnDegHist),
                                       annotations=[],
                                       barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha, 
                                       barLog=True,barAlign='center', barOrientation='vertical', 
                                       barWidth=1.0,
                                       axisGrid=defAxisGrid, axisColor='k',
                                       axisYLabel=r'Vertices',
                                       axisXLim=(None, None), axisYLim=(1, None),                                       
                                       axisXFormatterFun=axisXFormatterFun,
                                       axisYFormatterFun=axisYFormatterFun,
                                       legendAlpha=legendAlpha, legendShadow=False,
                                       legendColor='w', legendFancybox=False, legendPos='upper right',
                                       legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                       myShareAxis='do_gis_deg_bar', legendTop = False,
                                       )
        
    do_gis_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ],
                                          [  r'GIS In-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha, 
                                          barLog=True, barAlign='center', barOrientation='vertical', 
                                          barWidth=1.0,
                                          axisGrid=defAxisGrid, axisColor='k',
                                          axisYLabel=r'Vertices',
                                          axisXLim=(None, None), axisYLim=(1, None),
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendAlpha=legendAlpha, legendShadow=False,
                                          legendColor='w', legendFancybox=False, legendPos='upper right',
                                          legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                          legendTop = False,
                                          shareAxisX='do_gis_deg_bar',shareAxisY='do_gis_deg_bar'
                                          )

    do_gis_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegOutHist, 'blue', None) ],
                                          [  r'GIS Out-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha, 
                                          barLog=True, barAlign='center', barOrientation='vertical', 
                                          barWidth=1.0,
                                          axisGrid=defAxisGrid, axisColor='k',
                                          axisXLabel=r'Degree',
                                          axisYLabel=r'Vertices',
                                          axisXLim=(None, None), axisYLim=(1, None),
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendAlpha=legendAlpha, legendShadow=False,
                                          legendColor='w', legendFancybox=False, legendPos='upper right',
                                          legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                          legendTop = False,
                                          shareAxisX='do_gis_deg_bar',shareAxisY='do_gis_deg_bar'
                                          )
    
    figSize = (defFigWidth / 2.54, defFigHeight / 2.54)
    
    show_plots([[do_gis_deg_bar],
                [do_gis_deg_in_bar],
                [do_gis_deg_out_bar]],
                show=False,
                fileName='gis_degree_dist_all.pdf',                
                figWSpace=0.2,
                figHSpace=0.3,
                figLeftSpace=defFigLeftSpace,
                figRightSpace=defFigRightSpace,
                figBottomSpace=defFigBottomSpace,
                figTopSpace=defFigTopSpace,
                figSize=figSize)



def fstree_nodes_at_level_annotated(levelAlpha=0.3): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv"
    
    csvColumnTreeLevel = "tree_level"
    csvColumnTreeLevelNodes = "tree_level_nodes"
    
    axisFontsize = 10
    
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
    shadingBoundaries = [(0.1, 10.5), # 6-15 Folders & Files
                         (10.5, 12.5), # 4-5 Users
                         (12.5, 15.9)] # 1-3 Orgs
    
    for ((level_start, level_end), color) in zip(shadingBoundaries, shading):
        annotations_level_shading += [get_do_annotation_level_shading(level_start, level_end, color)]
        
    annotateRotate = 'horizontal'
    annotateFontsize = 8
    boxStyle = "round,pad=0.3"
    boxFacecolor = '0.9'
    boxEdgecolor = '0.0'
    boxAlpha = 1.0    
    boxLinewidth = 0.5
        
    bbox_props = dict(boxstyle=boxStyle,
                      fc=boxFacecolor, ec=boxEdgecolor,
                      alpha=boxAlpha, lw=boxLinewidth)
    
    def get_do_annotation_level_line(level, value):
        def do_annotation_level_line(ax):            
            ax.annotate(value, xy=(500000, level), xytext=(550000, level),
                        size=annotateFontsize, rotation=annotateRotate,
                        ha='right', va='center',
                        bbox=bbox_props)

        return do_annotation_level_line

    for (level, value) in [(5.5, '250,000 Files \& Folders'),
                           (11.5, ' 5 Users'),
                           (14.0, '5 Organisations')]:
        annotations_level_shading += [get_do_annotation_level_line(level, value)]
        
    def axisYFormatterFun(x):
        return '$%d$' % (x)

#    def axisXFormatterFun(x, pos=0):
#        return '$%1.1f$' % (x / pow(10, 5))
    def axisXFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '$10^%d$' % (math.ceil(math.log(x, 10)))

    do_fstree_levels_barh = get_barh_from_file(csvNameHist, csvColumnTreeLevel,
                                               [(csvColumnTreeLevelNodes, 'blue') ],
                                               [  r'FS-Tree Vertices at Tree Level', ],
                                               csvInts=(csvColumnTreeLevel, csvColumnTreeLevelNodes),
                                               annotations=annotations_level_shading,
                                               barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha,
                                               barAlign='center', barOrientation='horizontal',
                                               barHeight=1.0, barLog=True, barReverse=True,
                                               axisGrid=defAxisGrid, axisFontSize=axisFontsize, axisColor='k',
                                               axisYLabel=r'Tree Level',
                                               axisXLabel=r'Vertices',
                                               axisXLim=(1, pow(10,6)),
                                               axisYLim=(None, 16),
                                               axisXFormatterFun=axisXFormatterFun,
                                               axisYFormatterFun=axisYFormatterFun,
                                               legendFontsize=10, legendAlpha=legendAlpha, 
                                               legendShadow=False, legendColor='w',
                                               legendFancybox=False, legendPos=None, legendTop=True,
                                               legendBorderPad=0.4, legendLabelSpace=0.1, legendBorderAxesPad=0.0,
                                              )
            
    figWidth = 9.0
    figHeight = 7.0
    figLeftSpace = 0.13
    figBottomSpace = 0.15
    figRightSpace = 0.95
    figTopSpace = 0.94

    figSize = (figWidth / 2.54, figHeight / 2.54)
    
    show_plots([[do_fstree_levels_barh]],
               fileName='fstree_nodes_at_levels_annotated.pdf',
               show=False,
               figWSpace=0.20,
               figHSpace=0.20,
               figLeftSpace=figLeftSpace,
               figRightSpace=figRightSpace,
               figBottomSpace=figBottomSpace,
               figTopSpace=figTopSpace,
               figSize=figSize)

def fstree_deg_stats_all_together(): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv" 
    
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"

    legendAlpha = 0.8
    
    def axisXFormatterFun(x, pos=0):
        if int(x) % 2 == 0:
            return '%d' % (x)
        else:
            return ''
    
    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '$10^%d$' % (math.ceil(math.log(x, 10)))
    
    do_fstree_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegHist, 'blue', None) ],
                                          [  r'FS-Tree Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha,
                                          barAlign='center', barOrientation='vertical',
                                          barWidth=1.0, barLog=True,
                                          axisGrid=defAxisGrid, axisColor='k',
                                          axisYLabel=r'Vertices',
                                          axisXLim=(None, None),                                           
                                          axisYLim=(None, pow(10,7)),                                           
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                          legendFancybox=False, legendPos='upper right', legendTop = False,
                                          myShareAxis='do_gis_deg_bar'
                                       )
        
    do_fstree_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ],
                                          [  r'FS-Tree In-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha,
                                          barAlign='center', barOrientation='vertical',
                                          barWidth=1.0, barLog=True,
                                          axisGrid=defAxisGrid, axisColor='k',
                                          axisYLabel=r'Vertices',
                                          axisXLim=(None, None),
                                          axisYLim=(None, pow(10,7)),
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                          legendFancybox=False, legendPos='upper right', legendTop = False,
                                          shareAxisX='do_gis_deg_bar',shareAxisY='do_gis_deg_bar'
                                          )

    do_fstree_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                              [(csvColumnDegOutHist, 'blue', None) ],
                                              [ r'FS-Tree Out-Degree' ],
                                              csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                              annotations=[],
                                              barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha,
                                              barAlign='center', barOrientation='vertical',
                                              barWidth=1.0, barLog=False,
                                              axisGrid=defAxisGrid, axisColor='k',
                                              axisXLabel=r'Degree', axisYLabel=r'Vertices',
                                              axisXLim=(None, None),
                                              axisYLim=(None, pow(10,7)),
                                              axisXFormatterFun=axisXFormatterFun,
                                              axisYFormatterFun=axisYFormatterFun,
                                              legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                              legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                              legendFancybox=False, legendPos='upper right', legendTop = False,
                                              shareAxisX='do_gis_deg_bar',shareAxisY='do_gis_deg_bar'
                                              )
    
    figSize = (defFigWidth / 2.54, defFigHeight / 2.54)
    
    show_plots([[do_fstree_deg_bar],
                [do_fstree_deg_in_bar],
                [do_fstree_deg_out_bar]],
                show=False,
                fileName='fstree_degree_dist_all.pdf',
                figWSpace=0.2,
                figHSpace=0.3,
                figLeftSpace=defFigLeftSpace,
                figRightSpace=defFigRightSpace,
                figBottomSpace=defFigBottomSpace,
                figTopSpace=defFigTopSpace,
                figSize=figSize)



def twitter_deg_stats_all_together(): 
    csvNameRaw = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_raw.csv"
    
    csvColumnDegRaw = "raw_deg_256" 
    csvColumnDegInRaw = "raw_deg_in_256"
    csvColumnDegOutRaw = "raw_deg_out_256"

    barBinCount = 100
    barRWidth = None #0.5
    legendAlpha = 0.8
    
    def axisXFormatterFun(x, pos=0):
        return '$%d$' % (x)
    
    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '$10^%d$' % (math.ceil(math.log(x, 10)))
    
    do_twitter_deg_hist = get_hist_from_file(csvNameRaw, csvColumnDegRaw, annotations=[],
                                             csvInts=(csvColumnDegRaw),
                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                             barHisttype='bar', barAlpha=defBarAlpha, barAlign='mid', 
                                             barRWidth=barRWidth, barOrientation='vertical', barLog=True,
                                             axisGrid=defAxisGrid, axisColor='k', axisXLabel='',
                                             axisYLabel=r'Vertices', axisName=r'Twitter Degree',
                                             axisXLim=(None, 2050),
                                             axisYFormatterFun=axisYFormatterFun,
                                             axisXFormatterFun=axisXFormatterFun,
                                             legendAlpha=legendAlpha,
                                             legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                             myShareAxis='do_twitter_deg_hist'
                                             )

    do_twitter_deg_in_hist = get_hist_from_file(csvNameRaw, csvColumnDegInRaw, annotations=[],
                                                csvInts=(csvColumnDegInRaw),
                                                barBinCount=(1400. / 2000.) * barBinCount, barFacecolor='blue',
                                                barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha, 
                                                barAlign='mid', barRWidth=barRWidth, barOrientation='vertical', 
                                                barLog=True,
                                                axisGrid=defAxisGrid, axisColor='k', axisXLabel='', axisYLabel=r'Vertices',
                                                axisName=r'Twitter In-Degree', axisXLim=(None, 2050),
                                                axisYFormatterFun=axisYFormatterFun,
                                                axisXFormatterFun=axisXFormatterFun,
                                                legendAlpha=legendAlpha,
                                                legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                                shareAxisX='do_twitter_deg_hist', shareAxisY='do_twitter_deg_hist'
                                                )

    do_twitter_deg_out_hist = get_hist_from_file(csvNameRaw, csvColumnDegOutRaw, annotations=[],
                                             csvInts=(csvColumnDegOutRaw),
                                             barBinCount=(700. / 2000.) * barBinCount, barFacecolor='blue',
                                             barEdgecolor='gray', barHisttype='bar', barAlpha=defBarAlpha, 
                                             barAlign='mid', barRWidth=barRWidth, barOrientation='vertical', 
                                             barLog=True,
                                             axisGrid=defAxisGrid, axisColor='k', axisXLabel=r'Degree',
                                             axisYLabel=r'Vertices', axisName=r'Twitter Out-Degree',
                                             axisXLim=(None, 2050),
                                             axisYFormatterFun=axisYFormatterFun,
                                             axisXFormatterFun=axisXFormatterFun,
                                             legendAlpha=legendAlpha,
                                             legendBorderPad=0.4, legendBorderAxesPad=0.2,
                                             shareAxisX='do_twitter_deg_hist', shareAxisY='do_twitter_deg_hist'
                                             )

    figSize = (defFigWidth / 2.54, defFigHeight / 2.54)
    
    show_plots([[do_twitter_deg_hist],
                [do_twitter_deg_in_hist],
                [do_twitter_deg_out_hist]],
                show=False,
                fileName='twitter_degree_dist_all.pdf',
                figWSpace=0.2,
                figHSpace=0.3,
                figLeftSpace=defFigLeftSpace,
                figRightSpace=defFigRightSpace,
                figBottomSpace=defFigBottomSpace,
                figTopSpace=defFigTopSpace,
                figSize=figSize)
