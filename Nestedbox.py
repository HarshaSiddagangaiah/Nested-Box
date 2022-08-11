import sys

# comparing each box
class nestedbox():
    
    def comp_box(self, boxes):
        for i in range(0,len(boxes)):
            for j in range(i+1,len(boxes)):
                if boxes[i][0] < boxes[j][0]:
                    if boxes[i][1] < boxes[j][1]:
                        if boxes[i][2] < boxes[j][2]:
                            matrix[i][j] = 1
        #print (matrix)
        return matrix    


class bipartate():
    def __init__(self,graph):
         
        self.graph = graph
        self.cols = len(graph)
        self.rows = len(graph[0])

    # maximum bipartate
    def bipartate_maching(self, u, match, visited):
 
        for v in range(self.rows):
            if self.graph[u][v] and visited[v] == False:
                visited[v] = True
                if match[v] == -1 or self.bipartate_maching(match[v],match, visited):
                    match[v] = u
                    return True
        return False
    
    # maximum bipartate maching
    def max_bipartate_maching(self):

        match = [-1] * self.rows        
        result = 0
        for i in range(self.cols):            
            visited = [False] * self.rows            
            if self.bipartate_maching(i, match, visited):
                result += 1
        return result


if __name__=='__main__':

    boxes = []
    nb = nestedbox()

    for i, line in enumerate(sys.stdin):
        if i == 0:
            num_boxes= line.rstrip()
            num = int(num_boxes)
            if num < 1 or num > 50:
                raise Exception("Sorry, this number below zero or above 50")
            #print(num_boxes)
        else:
            box = [int(y) for y in line.split()]
            for i in box:
                if i < 0 or i > 36:
                    raise Exception("Sorry, the box contains l, w, h less than 1 or greater than 36")
            box.sort() # sorting edges inside box
            #print(box)
            boxes.append(box)
    
    cols = int(num_boxes)
    rows = int(num_boxes)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    boxes.sort() #sorting boxes bases on first edge
    #print(boxes)
    
    nb.comp_box(boxes)
    b = bipartate(matrix)
    max_box = int(num_boxes) - b.max_bipartate_maching()
    print ("Smallest number of visible box: %d " % max_box)
 