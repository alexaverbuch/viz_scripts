from sys import *
from viz_results import *

dir = "/media/disk/alex/Neo4j/"
file2 = dir + "romania.ns2"
file4 = dir + "romania.ns4"

#viz_results(dir, coords=True, colored=True, imgW=5000, imgH=5000, default_v_size=5, default_e_size=1)

#viz_result(file2 + ".gml", file2, colored=True, coords=True, imgW=10000, imgH=10000, default_v_size=5, default_e_size=1)
viz_result(file4 + ".gml", file4, colored=True, coords=True, imgW=10000, imgH=10000, default_v_size=5, default_e_size=1)
