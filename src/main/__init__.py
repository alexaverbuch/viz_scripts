from sys import *
from igraph_scripts.igraph_scripts import *
from matplotlib_scripts.matplotlib_scripts import *
from matplotlib_scripts.matplotlib_example_scripts import *
from thesis_plots import thesis_plots_structure
from thesis_plots import thesis_plots_static
from thesis_plots import thesis_plots_insert
from thesis_plots import thesis_plots_dynamic
from thesis_plots import thesis_plots_didic_stress

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
#viz_result(gmlFile, imgFile, imgLayout="fr", imgFormat="pdf", colored=False,
#           imgW=1000, imgH=1000, vSize=10, eWidth=2,
#           vColor=blue, eColor=black)

#************************************************************************************************************************************
#******************matplotlib********************************************************************************************************
#************************************************************************************************************************************

#*************************************************
#******************STRUCTURE**********************
#*************************************************
#thesis_plots_structure.gis_nodes_by_lon_lat()
#thesis_plots_structure.gis_nodes_by_lon()
#thesis_plots_structure.gis_nodes_by_lon_ptn()
#thesis_plots_structure.gis_deg_stats_all_together()
#thesis_plots_structure.gis_deg_stats_all_separate()
#
#thesis_plots_structure.fstree_deg_stats_all_together()
#thesis_plots_structure.fstree_deg_stats_all_separate()
#thesis_plots_structure.fstree_nodes_at_level_annotated(levelAlpha=0.3)
#
#thesis_plots_structure.twitter_deg_stats_all_together()
#thesis_plots_structure.twitter_deg_stats_all_separate()

#**********************************************
#******************STATIC**********************
#**********************************************
#thesis_plots_static.fstree_search_load_balance_all_2()
#thesis_plots_static.fstree_search_load_balance_all_4()
#thesis_plots_static.fstree_search_glratio_2()
#thesis_plots_static.fstree_search_glratio_4()
#thesis_plots_static.fstree_traf()

#thesis_plots_static.gis_long5_short95_load_balance_all_2()
#thesis_plots_static.gis_long5_short95_load_balance_all_4()
#thesis_plots_static.gis_long5_short95_glratio_2()
#thesis_plots_static.gis_long5_short95_glratio_4()
#thesis_plots_static.gis_traf()

#thesis_plots_static.twitter_load_balance_all_2()
#thesis_plots_static.twitter_load_balance_all_4()
#thesis_plots_static.twitter_glratio_2()
#thesis_plots_static.twitter_glratio_4()
#thesis_plots_static.twitter_traf()

#**********************************************
#******************INSERT**********************
#**********************************************
#thesis_plots_insert.fstree_insert_gl_traf_4()
#thesis_plots_insert.fstree_insert_std_nodes_4()
#thesis_plots_insert.fstree_insert_std_rels_4()
#thesis_plots_insert.fstree_insert_std_traf_4()
#thesis_plots_insert.fstree_insert_edge_cut_4()

#thesis_plots_insert.twitter_insert_gl_traf_4()
#thesis_plots_insert.twitter_insert_std_nodes_4()
#thesis_plots_insert.twitter_insert_std_rels_4()
#thesis_plots_insert.twitter_insert_std_traf_4()
#thesis_plots_insert.twitter_dynamic_edge_cut_4()

#thesis_plots_insert.gis_insert_gl_traf_4()
#thesis_plots_insert.gis_insert_std_nodes_4()
#thesis_plots_insert.gis_insert_std_rels_4()
#thesis_plots_insert.gis_insert_std_traf_4()
#thesis_plots_insert.gis_insert_edge_cut_4()

#**********************************************
#******************DYNAMIC*********************
#**********************************************
#thesis_plots_dynamic.gis_dynamic_gl_traf_4()
#thesis_plots_dynamic.gis_dynamic_std_nodes_4()
#thesis_plots_dynamic.gis_dynamic_std_rels_4()
#thesis_plots_dynamic.gis_dynamic_std_traf_4()
#thesis_plots_dynamic.gis_dynamic_edge_cut_4()

#thesis_plots_dynamic.fstree_dynamic_gl_traf_4()
#thesis_plots_dynamic.fstree_dynamic_std_nodes_4()
#thesis_plots_dynamic.fstree_dynamic_std_rels_4()
#thesis_plots_dynamic.fstree_dynamic_std_traf_4()
#thesis_plots_dynamic.fstree_dynamic_edge_cut_4()

#thesis_plots_dynamic.twitter_dynamic_gl_traf_4()
#thesis_plots_dynamic.twitter_dynamic_std_nodes_4()
#thesis_plots_dynamic.twitter_dynamic_std_rels_4()
#thesis_plots_dynamic.twitter_dynamic_std_traf_4()
#thesis_plots_dynamic.twitter_dynamic_edge_cut_4()

#**********************************************
#******************DIDIC STRESS****************
#**********************************************
thesis_plots_didic_stress.gis_stress_gl_traf_4()
thesis_plots_didic_stress.gis_stress_std_nodes_4()
thesis_plots_didic_stress.gis_stress_std_rels_4()
thesis_plots_didic_stress.gis_stress_std_traf_4()
thesis_plots_didic_stress.gis_stress_edge_cut_4()

thesis_plots_didic_stress.fstree_stress_gl_traf_4()
thesis_plots_didic_stress.fstree_stress_std_nodes_4()
thesis_plots_didic_stress.fstree_stress_std_rels_4()
thesis_plots_didic_stress.fstree_stress_std_traf_4()
thesis_plots_didic_stress.fstree_stress_edge_cut_4()

thesis_plots_didic_stress.twitter_stress_gl_traf_4()
thesis_plots_didic_stress.twitter_stress_std_nodes_4()
thesis_plots_didic_stress.twitter_stress_std_rels_4()
thesis_plots_didic_stress.twitter_stress_std_traf_4()
thesis_plots_didic_stress.twitter_stress_edge_cut_4()