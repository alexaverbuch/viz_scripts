from sys import *
from igraph_scripts import *
from matplotlib_example_scripts import *
from matplotlib_scripts import *

gmlFile = "/media/disk/alex/Neo4j/romania-gis-DIDIC2-GID-NAME-COORDS-BICYCLE.basic.gml"
imgFile = "romania-gis-bicycle"
viz_result(gmlFile, imgFile, colored=False, coords=True, vSize=10, eWidth=2)
 
##dropboxDir = "/media/disk/alex/Dropbox/"
#dropboxDir = "/home/alex/Dropbox/"
#csvDir = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/CSV Versions/GIS2 GOp/"
#csvName = csvDir + "GIS2_GOp_GTraf.csv"
#columnX = 'Index'
#columnY1 = '2rand (sorted)'
#columnY2 = '2didic (sorted)' 
#columnY3 = '2hard (sorted)'
#
#tempCsvName = "test.txt"
#tempColumnX = 'xaxis'
#tempColumnY1 = 'column1'
#tempColumnY2 = 'column2'
#
#
#get_hist_from_file = get_hist_from_file(csvName, columnY1, barBinCount=100,
#                                        axisXLabel='', axisTitle='')
#
#get_line_from_file = get_line_from_file(csvName, columnX,
#                                        [(columnY1, 'r', 'yLabel1'),
#                                         (columnY2, 'b', 'yLabel2')],
#                                        axisXLabel='', axisTitle='')
#
#get_bar_from_file = get_bar_from_file(tempCsvName, tempColumnX,
#                                      [(tempColumnY1, 'b'), (tempColumnY2, 'g')],
#                                      ['Col 1', 'Col 2'],
#                                      axisTitle='')
#
##show_plot(get_bar_from_file)
#show_plots([[get_hist_from_file],
#            [get_line_from_file],
#            [get_bar_from_file]])                          
