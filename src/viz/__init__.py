from sys import *
from viz_results import *

#dir1 = "/media/disk/alex/Dropbox/Neo_Thesis_Private/2010-04-09 Blog/"
#dir2 = "/media/disk/alex/Dropbox/Neo_Thesis_Private/2010-04-09 Blog/romania gml files/"
#layout = viz_result(dir1 + "romania-basic.gml", dir1 + "romania-basic-coord", colored=False, coords=True)
#viz_results(dir2, default_layout=layout, colored=True, coords=False)

#dir2 = "/media/disk/alex/Dropbox/Neo_Thesis_Private/2010-04-09 Blog/romania gml files/"
#viz_result(dir2 + "romania.2.45.gml", dir2 + "romania.2.45.layout", imgLayout="lgl", colored=True, coords=False)


dir = "/media/disk/alex/Dropbox/Neo_Thesis_Private/Romania Viz/"
file = "romania-balanced2-named-coords_all-all-no_orphoned.basic"
layout = viz_result(dir + file + ".gml", dir + file + "-COLOR-COORD", imgLayout="lgl", colored=True, coords=True)
viz_result(dir + file + ".gml", dir + file + "-COLOR-RECOORD", default_layout=layout, colored=True, coords=False)
