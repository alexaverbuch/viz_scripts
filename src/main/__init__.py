from sys import *
from igraph_scripts import *
from matplotlib_example_scripts import *
from matplotlib_scripts import *

#dir = "/home/alex/workspace/graph_gen_utils/var"
#viz_results(dir, colored=True, coords=True, imgW=500, imgH=500, vLabel=False, vSize=50, eWidth=10, eWidthMulti="weight")
 
#gis_local_op_global_traffic_2('')
#gis_local_op_global_traffic_2('')
csvDir = "/home/alex/Dropbox/Neo_Thesis/Notes/evaluation results/GIS/CSV Versions/GIS2 GOp/"
csvName = csvDir + "GIS2_GOp_GTraf.csv"

#line_from_file_separate_sym(csvName,
#                          [[('Index', '2hard (sorted)', 'r', '', 'yLabel1', 'Title1')],
#                           [('Index', 'Global/Local (sorted)', 'g', 'xLabel3', 'yLabel3', 'Title3')],
#                           [('Index', '2hard (sorted)', 'r', '', 'yLabel1', 'Title1')]],
#                           fileName="output.pdf")

#line_from_file(csvName,
#               'Index',
#               [('2hard (sorted)', 'r', 'yLabel1'),
#                ('2rand (sorted)', 'b', 'xLabel2')],
#                fileName="output.pdf",
#                title='Title Goes Here',
#                xLabel='xLabel',
#                yLabel='yLabel',)

#csvName = "/home/alex/workspace/viz_scripts/src/main/test.txt"
#column = 'column1'
column = '2didic (sorted)'
hist_from_file(csvName, column, binCount=100)

#example_histogram()
