import os, glob
from igraph import *
from time import *

# Assume .EXT files are named as: "description.cluster_count.time_step.EXT"
def rename_to_seq(directory, ext="gml"):
    for filePath in glob.glob(os.path.join(directory, '*.' + ext)):
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
         
        old = os.path.join(os.path.dirname(filePath), os.path.basename(filePath))
        new = os.path.join(os.path.dirname(filePath), newFileName + fileExtension)
        print "old: ", old
        print "new: ", new
        os.rename(old, new)        

# Assume .GML files are named as: "description.cluster_count.time_step.GML"
def viz_results_seq(directory, colored=False, coords=False):
    layout = False
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
        imgFilePath = os.path.join(os.path.dirname(filePath), newFileName)
        layout = viz_result(filePath, imgFilePath, default_layout=layout, colored=colored, coords=coords)

def viz_results(directory, colored=False, coords=False):
    layout = False 
    for filePath in glob.glob(os.path.join(directory, '*.gml')):
        file = os.path.basename(filePath)
        fileName = os.path.splitext(file)[0]
        fileExtension = os.path.splitext(file)[1]
        print "found .gml file:", file
        print "file name:", fileName 
        print "file extension:", fileExtension                         
        imgFilePath = os.path.join(os.path.dirname(filePath), fileName)
        layout = viz_result(filePath, imgFilePath, default_layout=layout, colored=colored, coords=coords)

def viz_result(gmlFile, imgFile, imgLayout="fr", default_layout=False, colored=False, coords=False):
    elapsedTime = time()
    
    print "loading ", gmlFile, "..."    
    g = Graph.Read_GML(gmlFile)
    print timeToStr(time() - elapsedTime)
    elapsedTime = time()

    print "configuring visual style..."
    #color_dict = {-1: "black", 0: "blue", 1: "red", 2: "green", 3: "pink", 4: "yellow", 5: "chocolate", 6: "dark orange", 7: "gray", 8: "maroon", 9: "purple", 10: "aqua", 11: "brown", 12: "dark cyan", 13: "dark green", 14: "dark magenta", 15: "fuchsia"}
    color_dict = {-1: "#000000", 0: "#0000ff", 1: "#ff0000", 2: "#00ff00", 3: "#ffc0cb", 4: "#ffff00", 5: "#d2691e", 6: "#ff8c00", 7: "#a9a9a9", 8: "#b03060", 9: "#9370db", 10: "#00ffff", 11: "#a52a2a", 12: "#008b8b", 13: "#006400", 14: "#8b008b", 15: "#ff00ff"}
    
    visual_style = {}
    
    print "\tvertex sizes..."
    visual_style["vertex_size"] = [5] * g.vcount()
    print "\t", timeToStr(time() - elapsedTime)
    elapsedTime = time()
    
    print "\tvertex labels..."
    visual_style["vertex_label"] = [""] * g.vcount()
    print "\t", timeToStr(time() - elapsedTime)
    elapsedTime = time()
    
    print "\tvertex colors..."
    if colored == True:        
        visual_style["vertex_color"] = [color_dict[color] for color in g.vs["color"]]
    else:
#        visual_style["vertex_color"] = ["#000000"] * g.vcount()
        visual_style["vertex_color"] = ["#00ff00"] * g.vcount()
    print "\t", timeToStr(time() - elapsedTime)
    elapsedTime = time()
        
    print "\tedge colors..."
    if colored == True:        
        visual_style["edge_color"] = [color_dict[color] for color in g.es["color"]]
    else:
        visual_style["edge_color"] = ["#ff0000"] * g.vcount()
    print "\t", timeToStr(time() - elapsedTime)
    elapsedTime = time()
          
    print "\tedge width..."
    visual_style["edge_width"] = 2
    print "\t", timeToStr(time() - elapsedTime)
    elapsedTime = time()
    
    if default_layout == False:
        if coords == True:
            print "\tlayout from coords..."

            print "\t\tget lat_coord bounds..."
            min_lat_coord = 180;
            max_lat_coord = 0;                        
            for a_lat_coord in g.vs["lat"]:
                if a_lat_coord < min_lat_coord and a_lat_coord != 0 :
                    min_lat_coord = a_lat_coord
                if a_lat_coord > max_lat_coord and a_lat_coord != 0 :
                    max_lat_coord = a_lat_coord
            med_lat_coord = max_lat_coord - ((max_lat_coord - min_lat_coord) / 2)
            print "\t\tlat: median %d, min %d, max %d" % (med_lat_coord, min_lat_coord, max_lat_coord)             
                    
            print "\t\tget lon_coord bounds..."
            min_lon_coord = 180;
            max_lon_coord = 0;                        
            for a_lon_coord in g.vs["lon"]:
                if a_lon_coord < min_lon_coord and a_lon_coord != 0 :
                    min_lon_coord = a_lon_coord
                if a_lon_coord > max_lon_coord and a_lon_coord != 0 :
                    max_lon_coord = a_lon_coord
            med_lon_coord = max_lon_coord - ((max_lon_coord - min_lon_coord) / 2)
            print "\t\tlon: median %d, min %d, max %d" % (med_lon_coord, min_lon_coord, max_lon_coord)             
                    
            print "\t\tget lat_coords..."
#            lat_coords = [lat_coord for lat_coord in g.vs["lat"]]
            lat_coords = [fixCoordY(lat_coord, med_lat_coord) for lat_coord in g.vs["lat"]]
            print "\t\t", timeToStr(time() - elapsedTime)
            
            elapsedTime = time()
            
            print "\t\tget lon_coords..."
#            lon_coords = [lon_coord for lon_coord in g.vs["lon"]]
            lon_coords = [fixCoordX(lon_coord, med_lon_coord) for lon_coord in g.vs["lon"]]
            print "\t\t", timeToStr(time() - elapsedTime)
            elapsedTime = time()
            
            print "\t\tcombine lat_coords & lon_coords..."
            def combine(x, y): return [x, y]            
            default_layout = map(combine, lon_coords, lat_coords)
            print "\t\t", timeToStr(time() - elapsedTime)
            elapsedTime = time()
            
#            default_layout = [[g.vs["lon"][index], g.vs["lat"][index]] for index in range(len(g.vs["lat"]))]                    
        else:        
            print "\tlayout from algorithm..."
            #large graph = "lgl"
            #forced directed = "fr"     
            #distributed recursive (large graph) = "drl"     
            #forced directed = "grid_fr"
            #circular = "circle"
            default_layout = g.layout(imgLayout)
            print "\t", timeToStr(time() - elapsedTime)
            elapsedTime = time()
    else:
        print "\treuse previous layout..."        
    visual_style["layout"] = default_layout
    
    print "\twindow size..."
    visual_style["bbox"] = (10000, 10000)
    print "\t", timeToStr(time() - elapsedTime)
    elapsedTime = time()
    
    print "\twindow margin..."
    visual_style["margin"] = 10
    print "\t", timeToStr(time() - elapsedTime)
    elapsedTime = time()
    
    print "configuring visual style complete"
    
    print "saving png:" + imgFile + ".png..."
    plot(g, imgFile + ".png", **visual_style)
    print timeToStr(time() - elapsedTime)
    elapsedTime = time()
    
#    print "saving svg:" + imgFile + ".svg..."
#    plot(g, imgFile + ".svg", **visual_style)
#    print timeToStr(time() - elapsedTime)
#    elapsedTime = time()
    
    print "done"
    print "---"
    return default_layout

def fixCoordX(coord, default):
    if coord == 0:
        coord = default
    return coord

def fixCoordY(coord, default):
    if coord == 0:
        coord = default
    return coord

def timeToStr(elapsedTime=0.0):
    s = elapsedTime % 60
    m = elapsedTime / 60
    h = (elapsedTime / 60) / 60
    return "%d(h):%02d(m):%02d(s)" % (h, m, s)
