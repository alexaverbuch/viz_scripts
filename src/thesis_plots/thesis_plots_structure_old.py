import math
from matplotlib import rc
from matplotlib_scripts.matplotlib_scripts import *

fontsizeLabels = r'\LARGE '
fontsizeTicks = r'\Large '
fontsizeLegend = r'\Large '
axisTickFontSize = 16

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
        return '%s%2d%s' % (fontsizeTicks, x, '$^{\circ}$')            

    def axisYFormatterFunLon(x, pos=0):
        return '%s%1.1F' % (fontsizeTicks, float(x) / 10000.)            
        
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisTickFontSize=axisTickFontSize,
                                   axisXLabel=fontsizeLabels + r'Longitude',
                                   axisYLabel=fontsizeLabels + r'Vertex Count $(\times 10^4)$',
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
        return '%s%2d%s' % (fontsizeTicks, x, '$^{\circ}$')
                
    def axisXFormatterFunLat(x, pos=0):
        return '%s%1.1F' % (fontsizeTicks, float(x) / 10000.)
    
    node_lats = get_hist_from_file(csvName, csvColumnLat, annotations=annotations_lat,
                                   csvFloats=(csvColumnLat),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='horizontal', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisTickFontSize=axisTickFontSize,
                                   axisYLabel=fontsizeLabels + r'Latitude',
                                   axisXLabel=fontsizeLabels + r'Vertex Count $(\times 10^4)$',
                                   axisXLim=(axisXmin, axisXmax),
                                   axisXFormatterFun=axisXFormatterFunLat,
                                   axisYFormatterFun=axisYFormatterFunLat)
    
    imgFile = '/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/Romania_map_contour_ale_06r.png'
    do_img_from_file = get_img_from_file(imgFile, annotations=[])

    show_plots([[node_lons, None],
                [do_img_from_file, node_lats]],
                show=False,
                fileName='gis_density_map_lon_lat.pdf',
                figWSpace=0.25, figHSpace=0.25)
    
def gis_nodes_by_lon(): 
    csvName = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
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
        return '%s%2d%s' % (fontsizeTicks, x, '$^{\circ}$')            
    
    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisTickFontSize=axisTickFontSize,
                                   axisXLabel=fontsizeLabels + r'Longitude',
                                   axisYLabel=fontsizeLabels + r'Vertex Count',
                                   axisYLim=(axisYmin, axisYmax),
                                   axisXFormatterFun=axisXFormatterFun)

    show_plots([[node_lons]],
               show=False,
               fileName='gis_density_lon.pdf')

#def gis_nodes_by_lon(): 
#    csvName = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
#    csvColumnLon = "raw_nodes_by_lon"
#    
#    axisYmin = 0.0
#    axisYmax = 40000.0
#    axisFontsize = 12
#    
#    annotateRotateLon = 'vertical'
#    annotateFontsize = 10
#    annotateLinewidth = 3
#    annotateLinecolor = 'red'
#    annotateLinealpha = 0.8
#    annotateLinestyle = '-'
#    
#    lineYmin = 0.0
#    lineYmax = 37000.0
#    
#    boxStyle = "round,pad=0.3"
#    boxFacecolor = '0.9'
#    boxEdgecolor = '0.0'
#    boxAlpha = 1.0
#    boxLinewidth = 0.1
#    
#    arrowStyle = 'wedge,tail_width=1.'
#    arrowFacecolor = '0.9'
#    arrowEdgecolor = '0.0'
#    arrowAlpha = 1.0
#    
#    bbox_props = dict(boxstyle=boxStyle,
#                      fc=boxFacecolor, ec=boxEdgecolor,
#                      alpha=boxAlpha, lw=boxLinewidth)
#    arrow_props = dict(arrowstyle=arrowStyle,
#                       fc=arrowFacecolor, ec=arrowEdgecolor, alpha=arrowAlpha,
#                       patchA=None)
#            
#    annotations_lon = []
#    
#    def get_do_annotation_lon(city_name, city_lon):
#        def do_annotation_lon(ax):
#            ha = 'center'
#            if city_name == 'Iasi':
#                ha = 'right'
#            if city_name == 'Constanta':
#                ha = 'left'
#            ax.axvline(x=city_lon, ymin=lineYmin / axisYmax, ymax=lineYmax / axisYmax,
#                       linewidth=annotateLinewidth, color=annotateLinecolor,
#                       alpha=annotateLinealpha, linestyle=annotateLinestyle)
#            
#            ax.annotate(city_name, xy=(city_lon + 0.0, lineYmax), #xycoords='data',
#                        xytext=(city_lon + 0.0, lineYmax + 1000), #textcoords='offset points',
#                        size=annotateFontsize, rotation=annotateRotateLon, ha=ha, va='bottom',
##                        arrowprops=arrow_props,
#                        bbox=bbox_props
#                        )
#        return do_annotation_lon
#        
#    for (city_name, city_lon, _) in cities:
#        annotations_lon += [get_do_annotation_lon(city_name, city_lon)]
#    
#    def axisXFormatterFun(x, pos=0):
#        return '%2d%s' % (x, '$^{\circ}$')            
#    
#    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
#                                   csvFloats=(csvColumnLon),
#                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
#                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
#                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
#                                   axisColor='k', axisXLabel=r'Longitude', axisYLabel=r'Node Count',
#                                   axisYLim=(axisYmin, axisYmax),
#                                   axisXFormatterFun=axisXFormatterFun)
#
#    show_plots([[node_lons]],
#               show=False)
    
def gis_nodes_by_lon_ptn(): 
    csvName = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_raw.csv"
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
        return '%s%2d%s' % (fontsizeTicks, x, '$^{\circ}$')            

    node_lons = get_hist_from_file(csvName, csvColumnLon, annotations=annotations_lon,
                                   csvFloats=(csvColumnLon),
                                   barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                                   barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                   barOrientation='vertical', axisGrid=True, axisFontSize=axisFontsize,
                                   axisColor='k', axisTickFontSize=axisTickFontSize,
                                   axisXLabel=fontsizeLabels + r'Longitude',
                                   axisYLabel=fontsizeLabels + r'Vertex Count',
                                   axisYLim=(axisYmin, axisYmax),
                                   axisXFormatterFun=axisXFormatterFun)

    show_plots([[node_lons]],
               show=False,
               fileName='gis_partition2_lon_balanced.pdf')

def gis_deg_stats_all_together(): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_hist.csv"
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    
    axisXmin = None
    axisXmax = None
    legendAlpha = 0.8

    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)            

    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '%s$10^%d$' % (fontsizeTicks, math.ceil(math.log(x, 10)))

    do_gis_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                       [(csvColumnDegHist, 'blue', None) ],
                                       [fontsizeLegend + r'GIS Degree', ],
                                       csvInts=(csvColumnDegNum, csvColumnDegHist),
                                       annotations=[],
                                       barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barLog=True,
                                       barAlign='center', barOrientation='vertical', barWidth=1.0,
                                       axisGrid=True, axisFontSize=12, axisColor='k',
                                       axisYLabel=fontsizeLabels + r'Vertices',
                                       axisXLim=(axisXmin, axisXmax), axisTickFontSize=axisTickFontSize,
                                       axisXFormatterFun=axisXFormatterFun,
                                       axisYFormatterFun=axisYFormatterFun,
                                       legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                       legendColor='w', legendFancybox=False, legendPos='upper right',
                                       myShareAxis='do_gis_deg_bar'
                                       )
        
    do_gis_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ],
                                          [fontsizeLegend + r'GIS In-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barLog=True,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisYLabel=fontsizeLabels + r'Vertices',
                                          axisXLim=(axisXmin, axisXmax), axisTickFontSize=axisTickFontSize,
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                          legendColor='w', legendFancybox=False, legendPos='upper right',
                                          shareAxisX='do_gis_deg_bar'
                                          )

    do_gis_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegOutHist, 'blue', None) ],
                                          [fontsizeLegend + r'GIS Out-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barLog=True,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Degree',
                                          axisYLabel=fontsizeLabels + r'Vertices',
                                          axisXLim=(axisXmin, axisXmax), axisTickFontSize=axisTickFontSize,
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False,
                                          legendColor='w', legendFancybox=False, legendPos='upper right',
                                          shareAxisX='do_gis_deg_bar'
                                          )
    
    show_plots([[do_gis_deg_bar],
                [do_gis_deg_in_bar],
                [do_gis_deg_out_bar]],
                show=False,
                figWSpace=0.2, figHSpace=0.35,
                fileName='gis_degree_dist_all.pdf')
    
def gis_deg_stats_all_separate(): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis_hist.csv"

    legendAlpha = 0.8
        
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    
    def axisXFormatterFun(x, pos=0):
        return '%s%s' % (fontsizeTicks, x)
                
    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '%s$10^%d$' % (fontsizeTicks, math.ceil(math.log(x, 10)))
        
    do_gis_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                       [(csvColumnDegHist, 'blue', None) ],
                                       [fontsizeLegend + r'GIS Degree', ],
                                       csvInts=(csvColumnDegNum, csvColumnDegHist),
                                       annotations=[],
                                       barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                       barAlign='center', barOrientation='vertical',
                                       barWidth=1.0, barLog=True,
                                       axisGrid=True, axisFontSize=12, axisColor='k',
                                       axisXLabel=fontsizeLabels + r'Degree',
                                       axisYLabel=fontsizeLabels + r'Vertices',
                                       axisTickFontSize=axisTickFontSize,
                                       axisXLim=(0, 15),
                                       axisXFormatterFun=axisXFormatterFun,
                                       axisYFormatterFun=axisYFormatterFun,
                                       legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                       legendFancybox=False, legendPos='upper right'
                                       )
        
    do_gis_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ],
                                          [fontsizeLegend + r'GIS In-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical',
                                          barWidth=1.0, barLog=True,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Degree',
                                          axisYLabel=fontsizeLabels + r'Vertices',
                                          axisTickFontSize=axisTickFontSize,
                                          axisXLim=(0, 8),
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right'
                                          )

    do_gis_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegOutHist, 'blue', None) ],
                                          [fontsizeLegend + r'GIS Out-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical',
                                          barWidth=1.0, barLog=True,
                                          axisGrid=True, axisFontSize=12, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Degree',
                                          axisYLabel=fontsizeLabels + r'Vertices',
                                          axisTickFontSize=axisTickFontSize,
                                          axisXLim=(0, 8),
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right'
                                          )
    
    show_plots([[do_gis_deg_bar]],
               fileName="gis_degree_dist_one_in_out.pdf",
               show=False)
    show_plots([[do_gis_deg_in_bar]],
               fileName="gis_degree_dist_one_in.pdf",
               show=False)
    show_plots([[do_gis_deg_out_bar]],
               fileName="gis_degree_dist_one_out.pdf",
               show=False)



def fstree_deg_stats_all_together(): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv" 
    
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"

    axisXmin = None
    axisXmax = None
    axisFontsize = 12
    
    legendAlpha = 0.8
    
    def axisXFormatterFun(x, pos=0):
        if int(x) % 2 == 0:
            return '%s%d' % (fontsizeTicks, x)
        else:
            return ''
    
    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '%s$10^%d$' % (fontsizeTicks, math.ceil(math.log(x, 10)))
    
    do_fstree_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegHist, 'blue', None) ],
                                          [fontsizeTicks + r'FS-Tree Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical',
                                          barWidth=1.0, barLog=True,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisYLabel=fontsizeLabels + r'Vertices',
                                          axisXLim=(axisXmin, axisXmax),
                                          axisTickFontSize=axisTickFontSize,
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          myShareAxis='do_gis_deg_bar'
                                       )
        
    do_fstree_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegInHist, 'blue', None) ],
                                          [fontsizeTicks + r'FS-Tree In-Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                          barAlign='center', barOrientation='vertical',
                                          barWidth=1.0, barLog=True,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisYLabel=fontsizeLabels + r'Vertices',
                                          axisXLim=(axisXmin, axisXmax), axisTickFontSize=axisTickFontSize,
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right',
                                          shareAxisX='do_gis_deg_bar'
                                          )

    do_fstree_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                              [(csvColumnDegOutHist, 'blue', None) ],
                                              [fontsizeTicks + r'FS-Tree Out-Degree', ],
                                              csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                              annotations=[],
                                              barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                              barAlign='center', barOrientation='vertical',
                                              barWidth=1.0, barLog=True,
                                              axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                              axisXLabel=fontsizeLabels + r'Degree', axisYLabel=fontsizeLabels + r'Vertices',
                                              axisXLim=(axisXmin, axisXmax), axisTickFontSize=axisTickFontSize,
                                              axisXFormatterFun=axisXFormatterFun,
                                              axisYFormatterFun=axisYFormatterFun,
                                              legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                              legendFancybox=False, legendPos='upper right',
                                              shareAxisX='do_gis_deg_bar'
                                              )
    
    show_plots([[do_fstree_deg_bar],
                [do_fstree_deg_in_bar],
                [do_fstree_deg_out_bar]],
                show=False,
                figWSpace=0.2, figHSpace=0.3,
                fileName='fstree_degree_dist_all.pdf')
    
def fstree_deg_stats_all_separate(): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv"
    
    csvColumnDegNum = "deg"
    csvColumnDegHist = "hist_deg"
    csvColumnDegInHist = "hist_deg_in"
    csvColumnDegOutHist = "hist_deg_out"
    
    axisFontsize = 12
        
    legendAlpha = 0.8
        
    def axisXFormatterFun(x, pos=0):
        if int(x) % 2 == 0:
            return '%s%d' % (fontsizeTicks, x)
        else:
            return ''
    
    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '%s$10^%d$' % (fontsizeTicks, math.ceil(math.log(x, 10)))
    
        
    do_fstree_deg_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                          [(csvColumnDegHist, 'blue', None) ],
                                          [fontsizeLegend + r'FS-Tree Degree', ],
                                          csvInts=(csvColumnDegNum, csvColumnDegHist),
                                          annotations=[],
                                          barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barLog=True,
                                          barAlign='center', barOrientation='vertical', barWidth=1.0,
                                          axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                          axisXLabel=fontsizeLabels + r'Degree', axisYLabel=fontsizeLabels + r'Vertices',
                                          axisXLim=(0, 38), axisTickFontSize=axisTickFontSize,
                                          axisXFormatterFun=axisXFormatterFun,
                                          axisYFormatterFun=axisYFormatterFun,
                                          legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                          legendFancybox=False, legendPos='upper right'
                                          )
        
    do_fstree_deg_in_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                             [(csvColumnDegInHist, 'blue', None) ],
                                             [fontsizeLegend + r'FS-Tree In-Degree', ],
                                             csvInts=(csvColumnDegNum, csvColumnDegInHist),
                                             annotations=[],
                                             barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barLog=True,
                                             barAlign='center', barOrientation='vertical', barWidth=1.0,
                                             axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                             axisXLabel=fontsizeLabels + r'Degree', axisYLabel=fontsizeLabels + r'Vertices',
                                             axisXLim=(0, 8), axisTickFontSize=axisTickFontSize,
                                             axisXFormatterFun=axisXFormatterFun,
                                             axisYFormatterFun=axisYFormatterFun,
                                             legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                             legendFancybox=False, legendPos='upper right'
                                             )

    do_fstree_deg_out_bar = get_bar_from_file(csvNameHist, csvColumnDegNum,
                                              [(csvColumnDegOutHist, 'blue', None) ],
                                              [fontsizeLegend + r'FS-Tree Out-Degree', ],
                                              csvInts=(csvColumnDegNum, csvColumnDegOutHist),
                                              annotations=[],
                                              barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barLog=True,
                                              barAlign='center', barOrientation='vertical', barWidth=1.0,
                                              axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                              axisXLabel=fontsizeLabels + r'Degree', axisYLabel=fontsizeLabels + r'Vertices',
                                              axisXLim=(0, 34), axisTickFontSize=axisTickFontSize,
                                              axisXFormatterFun=axisXFormatterFun,
                                              axisYFormatterFun=axisYFormatterFun,
                                              legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                              legendFancybox=False, legendPos='upper right'
                                              )
    
    show_plots([[do_fstree_deg_bar]],
               fileName="fstree_degree_dist_one_in_out.pdf",
               show=False)
    show_plots([[do_fstree_deg_in_bar]],
               fileName="fstree_degree_dist_one_in.pdf",
               show=False)
    show_plots([[do_fstree_deg_out_bar]],
               fileName="fstree_degree_dist_one_out.pdf",
               show=False)

def fstree_nodes_at_level_annotated(levelAlpha=0.3): 
    csvNameHist = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/Structure/structure_fstree_hist.csv"
    
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
    annotateFontsize = 13
    boxStyle = "round,pad=0.4"
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

    for (level, value) in [(5.5, '250,000 Files \& Folders'),
                           (11, ' 5 Users'),
                           (14, '5 Organisations')]:
        annotations_level_shading += [get_do_annotation_level_line(level, value)]
        
    def axisYFormatterFun(x):
        return '%s$%d$' % (fontsizeTicks, x)

#    def axisXFormatterFun(x, pos=0):
#        if x < 1:
#            return ''
#        return '%s$10^%d$' % (fontsizeTicks, math.ceil(math.log(x,10)))
    def axisXFormatterFun(x, pos=0):
        return '%s$%1.1f$' % (fontsizeTicks, x / pow(10, 5))
#    axisXFormatterFun=None

    do_fstree_levels_barh = get_barh_from_file(csvNameHist, csvColumnTreeLevel,
                                               [(csvColumnTreeLevelNodes, 'blue') ],
                                               [fontsizeLegend + r'FS-Tree Vertices at Tree Level', ],
                                               csvInts=(csvColumnTreeLevel, csvColumnTreeLevelNodes),
                                               annotations=annotations_level_shading,
                                               barEdgecolor='gray', barHisttype='bar', barAlpha=0.9,
                                               barAlign='center', barOrientation='horizontal',
                                               barHeight=1.0, barLog=False, barReverse=True,
                                               axisGrid=True, axisFontSize=axisFontsize, axisColor='k',
                                               axisYLabel=fontsizeLabels + r'Tree Level',
                                               axisXLabel=fontsizeLabels + r'Vertices ($\times 10^5$)',
                                               axisXLim=(0, 220000), axisTickFontSize=axisTickFontSize,
                                               axisYLim=(None, None),
                                               axisXFormatterFun=axisXFormatterFun,
                                               axisYFormatterFun=axisYFormatterFun,
                                               legendFontsize=12, legendAlpha=legendAlpha, legendShadow=False, legendColor='w',
                                               legendFancybox=False, legendPos='upper right'
                                              )
            
    show_plots([[do_fstree_levels_barh]],
               fileName='fstree_nodes_at_levels_annotated.pdf',
               show=False)



def twitter_deg_stats_all_together(): 
    csvNameRaw = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_raw.csv"
    
    csvColumnDegRaw = "raw_deg_256" 
    csvColumnDegInRaw = "raw_deg_in_256"
    csvColumnDegOutRaw = "raw_deg_out_256"

    axisXmin = None
    axisXmax = None
    
    barBinCount = 100
    barRWidth = None #0.5
    axisFontsize = 12
    legendAlpha = 0.8
    
    def axisXFormatterFun(x, pos=0):
        return '%s$%d$' % (fontsizeTicks, x)
    
    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '%s$10^%d$' % (fontsizeTicks, math.ceil(math.log(x, 10)))
    
    do_twitter_deg_hist = get_hist_from_file(csvNameRaw, csvColumnDegRaw, annotations=[],
                                             csvInts=(csvColumnDegRaw),
                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=barRWidth,
                                             barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisTickFontSize=axisTickFontSize, axisXLabel='',
                                             axisYLabel=fontsizeLabels + r'Vertices',
                                             axisName=fontsizeLegend + r'Twitter Degree',
                                             axisXLim=(axisXmin, axisXmax),
                                             axisYFormatterFun=axisYFormatterFun,
                                             axisXFormatterFun=axisXFormatterFun,
                                             legendAlpha=legendAlpha,
                                             myShareAxis='do_twitter_deg_hist'
                                             )

    do_twitter_deg_in_hist = get_hist_from_file(csvNameRaw, csvColumnDegInRaw, annotations=[],
                                                csvInts=(csvColumnDegInRaw),
                                                barBinCount=(1400. / 2000.) * barBinCount, barFacecolor='blue',
                                                barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                                barRWidth=barRWidth, barOrientation='vertical', barLog=True,
                                                axisGrid=True, axisFontSize=axisFontsize,
                                                axisColor='k', axisTickFontSize=axisTickFontSize, axisXLabel='',
                                                axisYLabel=fontsizeLabels + r'Vertices',
                                                axisName=fontsizeLegend + r'Twitter In-Degree',
                                                axisXLim=(axisXmin, axisXmax),
                                                axisYFormatterFun=axisYFormatterFun,
                                                axisXFormatterFun=axisXFormatterFun,
                                                legendAlpha=legendAlpha,
                                                shareAxisX='do_twitter_deg_hist'
                                                )

    do_twitter_deg_out_hist = get_hist_from_file(csvNameRaw, csvColumnDegOutRaw, annotations=[],
                                             csvInts=(csvColumnDegOutRaw),
                                             barBinCount=(700. / 2000.) * barBinCount, barFacecolor='blue',
                                             barEdgecolor='gray', barHisttype='bar', barAlpha=0.9, barAlign='mid',
                                             barRWidth=1, barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisTickFontSize=axisTickFontSize,
                                             axisXLabel=fontsizeLabels + r'Degree',
                                             axisYLabel=fontsizeLabels + r'Vertices',
                                             axisName=fontsizeLegend + r'Twitter Out-Degree',
                                             axisXLim=(axisXmin, axisXmax),
                                             axisYFormatterFun=axisYFormatterFun,
                                             axisXFormatterFun=axisXFormatterFun,
                                             legendAlpha=legendAlpha,
                                             shareAxisX='do_twitter_deg_hist'
                                             )

    show_plots([
                [do_twitter_deg_hist],
                [do_twitter_deg_in_hist],
                [do_twitter_deg_out_hist]],
                show=False,
                figWSpace=0.2, figHSpace=0.3,
                fileName='twitter_degree_dist_all.pdf')

def twitter_deg_stats_all_separate(): 
    csvNameRaw = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_raw.csv"
    
    csvColumnDegRaw = "raw_deg_256" 
    csvColumnDegInRaw = "raw_deg_in_256"
    csvColumnDegOutRaw = "raw_deg_out_256"
    
    axisXmin = None
    axisXmax = None
    
    barBinCount = 100
    barRWidth = None #0.5
    axisFontsize = 12
    legendAlpha = 0.8
    
    def axisXFormatterFun(x, pos=0):
        return '%s$%d$' % (fontsizeTicks, x)
    
    def axisYFormatterFun(x, pos=0):
        if x < 1:
            return ''
        return '%s$10^%d$' % (fontsizeTicks, math.ceil(math.log(x, 10)))
    
    
    do_twitter_deg_hist = get_hist_from_file(csvNameRaw, csvColumnDegRaw, annotations=[],
                                             csvInts=(csvColumnDegRaw),
                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=barRWidth,
                                             barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisTickFontSize=axisTickFontSize,
                                             axisXLabel=fontsizeLabels + r'Degree', 
                                             axisYLabel=fontsizeLabels + r'Vertices',
                                             axisName=fontsizeLegend + r'Twitter Degree',
                                             axisXFormatterFun=axisXFormatterFun, 
                                             axisYFormatterFun=axisYFormatterFun,
                                             axisXLim=(axisXmin, axisXmax),
                                             legendAlpha=legendAlpha)

    do_twitter_deg_in_hist = get_hist_from_file(csvNameRaw, csvColumnDegInRaw, annotations=[],
                                                csvInts=(csvColumnDegInRaw),
                                                barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                                barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=barRWidth,
                                                barOrientation='vertical', barLog=True,
                                                axisGrid=True, axisFontSize=axisFontsize,
                                                axisColor='k', axisTickFontSize=axisTickFontSize, 
                                                axisXLabel=fontsizeLabels + r'Degree', 
                                                axisYLabel=fontsizeLabels + r'Vertices',
                                                axisName=fontsizeLegend + r'Twitter In-Degree', 
                                                axisXFormatterFun=axisXFormatterFun, 
                                                axisYFormatterFun=axisYFormatterFun,
                                                axisXLim=(axisXmin, axisXmax),
                                                legendAlpha=legendAlpha)

    do_twitter_deg_out_hist = get_hist_from_file(csvNameRaw, csvColumnDegOutRaw, annotations=[],
                                             csvInts=(csvColumnDegOutRaw),
                                             barBinCount=barBinCount, barFacecolor='blue', barEdgecolor='gray',
                                             barHisttype='bar', barAlpha=0.9, barAlign='mid', barRWidth=1,
                                             barOrientation='vertical', barLog=True,
                                             axisGrid=True, axisFontSize=axisFontsize,
                                             axisColor='k', axisTickFontSize=axisTickFontSize,
                                             axisXLabel=fontsizeLabels + r'Degree', 
                                             axisYLabel=fontsizeLabels + r'Vertices',
                                             axisName=fontsizeLegend + r'Twitter Out-Degree', 
                                             axisXFormatterFun=axisXFormatterFun, 
                                             axisYFormatterFun=axisYFormatterFun,
                                             axisXLim=(axisXmin, axisXmax),
                                             legendAlpha=legendAlpha)

    show_plots([[do_twitter_deg_hist]],
                show=False,
                fileName='twitter_degree_dist_one_in_out.pdf')

    show_plots([[do_twitter_deg_in_hist]],
                show=False,
                fileName='twitter_degree_dist_one_in.pdf')
    
    show_plots([[do_twitter_deg_out_hist]],
                show=False,
                fileName='twitter_degree_dist_one_out.pdf')

