from sys import *
from igraph_scripts import *
from matplotlib_example_scripts import *
from matplotlib_scripts import *
from thesis_plots import *

#********************************************
#********************igraph******************
#********************************************

#gmlFile = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/FSTree/SampleTrees/sampleDB_742N_1327R.gml"
#imgFile = "/home/alex/Desktop/sampleDB_742N_1327R"
#
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

#********************************************
#******************TEMP**********************
#********************************************
#gis_nodes_by_lon_lat()
#gis_nodes_by_lon()
#gis_nodes_by_lon_ptn()
#gis_deg_stats_all_together()
#gis_deg_stats_all_separate()
#tree_deg_stats_all_together()
#fstree_deg_stats_all_separate()
#fstree_nodes_at_level()
#fstree_nodes_at_level_annotated(levelAlpha=0.3)
#twitter_deg_stats_all_together()
#twitter_deg_stats_all_separate()
#fstree_load_balance_2()
#fstree_load_balance_4()
#fstree_count_gtraf_2()
#fstree_count_gtraf_4()
#fstree_count_perc_gtraf_2()
#fstree_count_perc_gtraf_4()
#fstree_search_gtraf_2()
#fstree_search_gtraf_4()
#fstree_search_perc_gtraf_2()
#fstree_search_perc_gtraf_4()
#gis_load_balance_2()
#gis_load_balance_4()
#gis_global_gtraf_2()
#gis_global_gtraf_4()
#gis_global_perc_gtraf_2()
#gis_global_perc_gtraf_4()
#gis_local_gtraf_2()
#gis_local_gtraf_4()
#gis_local_perc_gtraf_2()
gis_local_perc_gtraf_4()

#********************************************
#******************FOR MARTIN****************
#********************************************

#csvName = "/home/alex/Desktop/ReadWrite_didic4_mix_trffAdd4"
#columnX = "id"
#columnY1 = "Chart_0_numNodes"
#columnY2 = "Chart_1_numNodes"
#columnY3 = "Chart_2_numNodes"
#columnY4 = "Chart_3_numNodes"
#columnY1 = "Chart_0_numRelas"
#columnY2 = "Chart_1_numRelas"
#columnY3 = "Chart_2_numRelas"
#columnY4 = "Chart_3_numRelas"
#columnY1 = "Chart_0_traffic"
#columnY2 = "Chart_1_traffic"
#columnY3 = "Chart_2_traffic"
#columnY4 = "Chart_3_traffic"
#                        
#get_line_from_file = get_line_from_file(csvName, columnX,
#                                        [(columnY1, 'r', "chart 0"),
#                                         (columnY2, 'b', "chart 1"),
#                                         (columnY3, 'g', "chart 2"),
#                                         (columnY4, 'k', "chart 3")],
#                                         axisXLabel='id', axisTitle='Number of Traffic')
#show_plots([[get_line_from_file]],
#           show=False)

#csvNameRaw = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_raw.csv"
#csvNameHistDeg = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_deg_hist.csv"
#csvNameHistStats = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Structure/structure_twitter_stats_hist.csv"
#
#csvColumnDegNum = "deg_256"
#csvColumnDegHist = "hist_deg_256"
#csvColumnDegInHist = "hist_deg_in_256"
#csvColumnDegOutHist = "hist_deg_out_256"
#
#csvColumnDegRaw = "raw_deg_256" 
#csvColumnDegInRaw = "raw_deg_in_256"
#csvColumnDegInRaw = "raw_deg_out_256"
#
##get_line_from_file = get_line_from_file(csvNameHistDeg, csvColumnDegNum,
##                                        [(csvColumnDegHist, 'r', "chart 0")],
##                                        csvInts=(csvColumnDegNum, csvColumnDegHist),
##                                        axisXLabel='id', axisTitle='Number of Traffic',
##                                        axisXScale='linear', axisYScale='log')
#
#get_hist_from_file = get_hist_from_file(csvNameRaw, csvColumnDegRaw, barBinCount=100,
#                                        axisXLabel='', axisTitle='',
#                                        csvInts=(csvColumnDegRaw), barLog=True)
#
#show_plots([[get_hist_from_file]],
#           show=False)
