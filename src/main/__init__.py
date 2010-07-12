from sys import *
from igraph_scripts import igraph_scripts
from matplotlib_scripts.matplotlib_scripts import *
from matplotlib_scripts.matplotlib_example_scripts import *
from thesis_plots import thesis_plots_static
from thesis_plots import thesis_plots_insert
from thesis_plots import thesis_plots_dynamic
from thesis_plots import thesis_plots_didic_stress
from thesis_plots import thesis_plots_structure

#************************************************************************************************************************************
#********************igraph**********************************************************************************************************
#************************************************************************************************************************************

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
#
#gmlFileGISSmall = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Sample Trees/gisSample_1282n_2481r.gml"
#imgFileGISSmall = "sampleGISSmall_1000_v1282[6,blue]_e2481[2,black]"
#gmlFileGISMedium = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Sample Trees/gisSample_2519n_5035r.gml"
#imgFileGISMedium = "sampleGISMedium_1000_v2519[6,blue]_e5035[2,black]"
#gmlFileGISLarge = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/Sample Trees/gisSample_5001n_10417r.gml"
#imgFileGISLarge = "sampleGISBig_1000_v5001[6,blue]_e10417[2,black]"
#
#gmlFileTwitterStart = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Sample/sampleTwitterSRT_1283n_1340r.gml"
#imgFileTwitterStart = "sampleTwitterStart_1000_v1283[10,blue]_e1340[2,black]"
#
#gmlFileTwitterEnd = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/Twitter/Sample/sampleTwitterEND_1241n_1308r.gml"
#imgFileTwitterEnd = "sampleTwitterEnd_1000_v1241[10,blue]_e1308[2,black]"
#
##igraph_scripts.viz_result(gmlFileGISSmall, imgFileGISSmall, imgLayout="fr", imgFormat="pdf", colored=False, coords=True,
##                          imgW=1000, imgH=1000, vSize=10, eWidth=2,
##                          vColor=blue, eColor=black)
##igraph_scripts.viz_result(gmlFileGISMedium, imgFileGISMedium, imgLayout="fr", imgFormat="pdf", colored=False, coords=True,
##                          imgW=1000, imgH=1000, vSize=8, eWidth=2,
##                          vColor=blue, eColor=black)
##igraph_scripts.viz_result(gmlFileGISLarge, imgFileGISLarge, imgLayout="fr", imgFormat="pdf", colored=False, coords=True,
##                          imgW=1000, imgH=1000, vSize=6, eWidth=2,
##                          vColor=blue, eColor=black)
#
#igraph_scripts.viz_result(gmlFileTwitterEnd, imgFileTwitterEnd, imgLayout="fr", imgFormat="pdf", 
#                          colored=False, coords=False, imgW=1000, imgH=1000, vSize=10, eWidth=2,
#                          vColor=blue, eColor=black)
#
#igraph_scripts.viz_result(gmlFileTwitterStart, imgFileTwitterStart, imgLayout="fr", imgFormat="pdf", 
#                          colored=False, coords=False, imgW=1000, imgH=1000, vSize=10, eWidth=2,
#                          vColor=blue, eColor=black)


#************************************************************************************************************************************
#******************matplotlib********************************************************************************************************
#************************************************************************************************************************************

#*************************************************
#******************STRUCTURE**********************
#*************************************************
#thesis_plots_structure.fstree_deg_stats_all_together()
#thesis_plots_structure.gis_deg_stats_all_together()
#thesis_plots_structure.twitter_deg_stats_all_together()
#thesis_plots_structure.gis_nodes_by_lon_lat()
#thesis_plots_structure.gis_nodes_by_lon()
#thesis_plots_structure.gis_nodes_by_lon_ptn()
#thesis_plots_structure.fstree_nodes_at_level_annotated(levelAlpha=0.3)

#**********************************************
#******************STATIC**********************
#**********************************************
#thesis_plots_static.gis_load_balance_all_2()
#thesis_plots_static.gis_load_balance_all_4()
#thesis_plots_static.gis_traf()
#thesis_plots_static.gis_glratio_2()
#thesis_plots_static.gis_glratio_4()

#thesis_plots_static.fstree_load_balance_all_2()
#thesis_plots_static.fstree_load_balance_all_4()
#thesis_plots_static.fstree_traf()
#thesis_plots_static.fstree_glratio_2()
#thesis_plots_static.fstree_glratio_4()

#thesis_plots_static.twitter_load_balance_all_2()
#thesis_plots_static.twitter_load_balance_all_4()
#thesis_plots_static.twitter_traf()
#thesis_plots_static.twitter_glratio_2()
#thesis_plots_static.twitter_glratio_4()

#**********************************************
#******************INSERT**********************
#**********************************************
#thesis_plots_insert.gis_insert_std_all_4()
#thesis_plots_insert.fstree_insert_std_all_4()
#thesis_plots_insert.twitter_insert_std_all_4()

#thesis_plots_insert.gis_insert_comms_all_4()
#thesis_plots_insert.fstree_insert_comms_all_4()
#thesis_plots_insert.twitter_insert_comms_all_4()

#**********************************************
#******************DYNAMIC*********************
#**********************************************
#thesis_plots_dynamic.gis_dynamic_comms_all_4()
#thesis_plots_dynamic.fstree_dynamic_comms_all_4()
#thesis_plots_dynamic.twitter_dynamic_comms_all_4()

#thesis_plots_dynamic.gis_dynamic_std_all_4()
#thesis_plots_dynamic.fstree_dynamic_std_all_4()
#thesis_plots_dynamic.twitter_dynamic_std_all_4()

#**********************************************
#******************DIDIC STRESS****************
#**********************************************
#thesis_plots_didic_stress.gis_stress_std_all_4()
#thesis_plots_didic_stress.fstree_stress_std_all_4()
#thesis_plots_didic_stress.twitter_stress_std_all_4()

#thesis_plots_didic_stress.gis_stress_comms_all_4()
#thesis_plots_didic_stress.fstree_stress_comms_all_4()
#thesis_plots_didic_stress.twitter_stress_comms_all_4()
