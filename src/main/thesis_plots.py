from matplotlib import rc
from matplotlib_scripts import *

#dropboxDir = "/media/disk/alex/Dropbox/"
dropboxDir = "/home/alex/Dropbox/"

def nodes_by_coords(): 
    csvName = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/Structure/structure_gis.csv"
    csvColumn = "raw_nodes_by_coord"
    x = get_hist_from_file(csvName, csvColumn,
                           barBinCount=100, barFacecolor='blue', barEdgecolor='gray',
                           barHisttype='bar', barAlpha=0.75, barAlign='mid',
                           barOrientation='vertical', axisGrid=True, axisFontSize=12, axisColor='k',
                           axisXLabel='Longitude', axisYLabel='Node Count',
                           axisName='Nodes by Coordinates', axisTitle='',
                           legendFontsize=12, legendAlpha=0.5, legendShadow=False, legendColor='w',
                           legendFancybox=False, legendPos='upper right')
    show_plot(x)
    
