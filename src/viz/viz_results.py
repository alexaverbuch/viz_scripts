import os, glob
from igraph import *

# Assume .gml files are named as: "description.cluster_count.time_step.gml"
def viz_results_seq(directory):
    for filePath in glob.glob(os.path.join(directory, '*.gml')):
        file = os.path.basename(filePath)
        fileName = os.path.splitext(file)[0]
        fileExtension = os.path.splitext(file)[1]
        fileNumber = os.path.splitext(fileName)[1].split(".")[1]
        newFileName = fileNumber.rjust(4, "0")
        print "found .gml file:", file
        print "file name:", fileName 
        print "file extension:", fileExtension 
        print "file number:", fileNumber 
        print "new file name:", newFileName 
        viz_result_colored(filePath, newFileName)        

def viz_results(directory, colored=False): 
    for file in glob.glob(os.path.join(directory, '*.gml')):
        print "found .gml file:", os.path.basename(file)
        viz_result_colored(file, os.path.splitext(file)[0])        

def viz_result_colored(gmlFile, imgFile, imgLayout="fr"):
    print "loading ", gmlFile, "..." 

    g = Graph.Read_GML(gmlFile)
    print "loading complete" 

    print "configuring visual style..."

    #color_dict = {-1: "black", 0: "blue", 1: "red", 2: "green", 3: "pink", 4: "yellow", 5: "chocolate", 6: "dark orange", 7: "gray", 8: "maroon", 9: "purple", 10: "aqua", 11: "brown", 12: "dark cyan", 13: "dark green", 14: "dark magenta", 15: "fuchsia"}
    color_dict = {-1: "#000000", 0: "#0000ff", 1: "#ff0000", 2: "#00ff00", 3: "#ffc0cb", 4: "#ffff00", 5: "#d2691e", 6: "#ff8c00", 7: "#a9a9a9", 8: "#b03060", 9: "#9370db", 10: "#00ffff", 11: "#a52a2a", 12: "#008b8b", 13: "#006400", 14: "#8b008b", 15: "#ff00ff"}
    visual_style = {}
    print "\tvertex sizes..."
    visual_style["vertex_size"] = [5] * g.vcount()
    print "\tvertex labels..."
    visual_style["vertex_label"] = [""] * g.vcount()
    print "\tvertex colors..."
    visual_style["vertex_color"] = [color_dict[color] for color in g.vs["color"]]
    print "\tedge colors..."
    visual_style["edge_color"] = [color_dict[color] for color in g.es["color"]] 
    print "\tedge width..."
    visual_style["edge_width"] = 1
    print "\tlayout..."
    
    #large graph = "lgl"
    #forced directed = "fr"     
    #distributed recursive (large graph) = "drl"     
    #forced directed = "grid_fr"
    #circular = "circle"
    visual_style["layout"] = g.layout(imgLayout)    
    
    print "\twindow size..."
    visual_style["bbox"] = (2000, 2000)
    print "\twindow margin..."
    visual_style["margin"] = 20
    
    print "configuring visual style complete"
    
    print "saving png:" + imgFile + ".png..."
    plot(g, imgFile + ".png", **visual_style)
    
#    print "saving svg:" + imgFile + ".svg..."
#    plot(g, imgFile + ".svg", **visual_style)
    
    print "done"
    print "---"

def viz_result_uncolored(gmlFile, imgFile, imgLayout="fr"):
    print "loading " + gmlFile + "..." 

    g = Graph.Read_GML(gmlFile)
    print "loading complete" 

    print "configuring visual style..."

    visual_style = {}
    print "\tvertex sizes..."
    visual_style["vertex_size"] = [5] * g.vcount()
    print "\tvertex labels..."
    visual_style["vertex_label"] = [""] * g.vcount()
    print "\tvertex colors..."
    visual_style["vertex_color"] = ["#000000"] * g.vcount()
    print "\tedge colors..."
    visual_style["edge_color"] = ["#ff0000"] * g.vcount()
    print "\tedge width..."
    visual_style["edge_width"] = 1
    print "\tlayout..."
    
    #large graph = "lgl"
    #forced directed = "fr"     
    #distributed recursive (large graph) = "drl"     
    #forced directed = "grid_fr"
    #circular = "circle"
    visual_style["layout"] = g.layout(imgLayout)    
    
    print "\twindow size..."
    visual_style["bbox"] = (2000, 2000)
    print "\twindow margin..."
    visual_style["margin"] = 20
    
    print "configuring visual style complete"
    
    print "saving png:" + imgFile + ".png..."
    plot(g, imgFile + ".png", **visual_style)
    
#    print "saving svg:" + imgFile + ".svg..."
#    plot(g, imgFile + ".svg", **visual_style)
    
    print "done"
    print "---"
