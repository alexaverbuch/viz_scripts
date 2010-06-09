from sys import *
from igraph_scripts import *
from matplotlib_example_scripts import *
from matplotlib_scripts import *

#dir = "/home/alex/workspace/graph_gen_utils/var"
#viz_results(dir, colored=True, coords=True, imgW=500, imgH=500, vLabel=False, vSize=50, eWidth=10, eWidthMulti="weight")
 
#gis_local_op_global_traffic_2('')
#gis_local_op_global_traffic_2('')
dropboxDir = "/media/disk/alex/Dropbox/"
csvDir = dropboxDir + "Neo_Thesis/Notes/evaluation results/GIS/CSV Versions/GIS2 GOp/"
csvName = csvDir + "GIS2_GOp_GTraf.csv"

#example_nothing()
#example_bar()

bar_from_file('test.txt',
              'xaxis',
              [('column1', 'b'), ('column2', 'g')],
              ['Col 1', 'Col 2'])

#line_from_file_separate(csvName,
#                          [[('Index', '2hard (sorted)', 'r', '', 'yLabel1', 'Title1')],
#                           [('Index', 'Global/Local (sorted)', 'g', '', 'yLabel2', ''),
#                            ('Index', '2hard (sorted)', 'r', '', 'yLabel1', 'Title1')],
#                           [('Index', '2hard (sorted)', 'r', 'xLabel3', 'yLabel3', 'Title3')]])

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
#column = '2didic (sorted)'
#hist_from_file(csvName, column, binCount=100)

#hist_from_file_separate_sym(csvName,
#                          [[('2hard (sorted)', 100, 'r', 'gray', '', 'yLabel1', 'one', 'Title1')],
#                           [('Global/Local (sorted)', 100, 'g', 'gray', '', 'yLabel2', 'two', '')],
#                           [('2hard (sorted)', 100, 'b', 'gray', 'xLabel3', 'yLabel3', 'three', '')]])


#(vals, valsBins, barFaceColor, barEdgeColor, axisXLabel, axisYLabel, axisTitle)
