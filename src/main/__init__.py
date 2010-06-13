from sys import *
from igraph_scripts import *
from matplotlib_example_scripts import *
from matplotlib_scripts import *
from thesis_plots import *

#********************************************
#********************igraph******************
#********************************************

#gmlFile = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/SampleTrees/sampleTree_2932N_5257R.gml"
#imgFile = "/home/alex/Desktop/sampleTree_2932N_5257R"
##viz_result(gmlFile, imgFile, colored=False, coords=True, vSize=5, eWidth=2, imgFormat="pdf")
#
#black = "#000000"
#blue = "#0000ff"
#red = "#ff0000"
#green = "#00ff00"
#viz_result(gmlFile, imgFile, imgLayout="fr", imgFormat="pdf", colored=False,
#           imgW=1000, imgH=1000, vSize=10, eWidth=1,
#           vColor=blue, eColor=red)

#********************************************
#******************matplotlib****************
#********************************************

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
#show_plots([[get_bar_from_file]])
#show_plots([[get_hist_from_file],
#            [get_line_from_file],
#            [get_bar_from_file]])

#********************************************
#******************TEMP**********************
#********************************************

#gis_deg_stats_all_together()
#gis_deg_stats_all_separate()
#tree_deg_stats_all_together()
#fstree_deg_stats_all_separate()
#fstree_nodes_at_level()
fstree_nodes_at_level_annotated(levelAlpha=0.3)
