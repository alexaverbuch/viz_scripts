from sys import *
from igraph_scripts.igraph_scripts import *
from matplotlib_scripts.matplotlib_scripts import *
from matplotlib_scripts.matplotlib_example_scripts import *
from thesis_plots.thesis_plots_structure import *
from thesis_plots.thesis_plots_static import *
from thesis_plots.thesis_plots_insert import *

#********************************************
#********************igraph******************
#********************************************

#gmlFile = "/home/alex/Desktop/Test/migrator_gis_test.2.100.gml"
#imgFile = "/home/alex/Desktop/Test/migrator_gis_test.2.100"
#
#default_layout = viz_result(gmlFile, imgFile, colored=True,
#                            imgW=500, imgH=500, vSize=20, eWidth=2)
#viz_results("/home/alex/Desktop/Test", default_layout=default_layout,
#            colored=True, coords=False, imgW=500, imgH=500, vSize=20, eWidth=2)

#black = "#000000"
#blue = "#0000ff"
#red = "#ff0000"
#green = "#00ff00"
#viz_result(gmlFile, imgFile, imgLayout="fr", imgFormat="pdf", colored=False,
#           imgW=1000, imgH=1000, vSize=10, eWidth=2,
#           vColor=blue, eColor=black)

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

#*************************************************
#******************STRUCTURE**********************
#*************************************************
#gis_nodes_by_lon_lat()
#gis_nodes_by_lon()
#gis_nodes_by_lon_ptn()
#gis_deg_stats_all_together()
#gis_deg_stats_all_separate()

#fstree_deg_stats_all_together()
#fstree_deg_stats_all_separate()
#fstree_nodes_at_level()
#fstree_nodes_at_level_annotated(levelAlpha=0.3)

#twitter_deg_stats_all_together()
#twitter_deg_stats_all_separate()


#**********************************************
#******************STATIC**********************
#**********************************************
#fstree_search_load_balance_all_2()
#fstree_search_load_balance_all_4()
#
#fstree_search_glratio_2()
#fstree_search_glratio_4()
#
#fstree_traf()


#gis_long5_short95_load_balance_all_2()
#gis_long5_short95_load_balance_all_4()
#
#gis_long5_short95_glratio_2()
#gis_long5_short95_glratio_4()
#
#gis_traf()



#twitter_load_balance_all_2()
#twitter_load_balance_all_4()
#
#twitter_glratio_2()
#twitter_glratio_4()
#
#twitter_traf()

#**********************************************
#******************INSERT**********************
#**********************************************
#fstree_insert_gl_traf_4()
#fstree_insert_std_nodes_4()
#fstree_insert_std_rels_4()
#fstree_insert_std_traf_4()
#fstree_insert_edge_cut_4()

#twitter_insert_gl_traf_4()
#twitter_insert_std_nodes_4()
#twitter_insert_std_rels_4()
#twitter_insert_std_traf_4()
#twitter_insert_edge_cut_4()

#gis_insert_gl_traf_4()
#gis_insert_std_nodes_4()
#gis_insert_std_rels_4()
#gis_insert_std_traf_4()
#gis_insert_edge_cut_4()

#**********************************************
#******************DYNAMIC*********************
#**********************************************

#**********************************************
#******************STUPID**********************
#**********************************************