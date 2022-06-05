class Winningpath:

    def __init__(self, ID, nodeIDs):

        self.ID = ID
        self.nodeIDs = nodeIDs
        self.nodes = []  
        self.state = 0

    def addnode(self, node):
        self.nodes.append(node)
        for i in range(0, len(self.nodes)- 1):
            if self.nodes[i].state != self.nodes[i+1].state:
                self.state = -1 #cant win in this winningpath now
                return None

        if len(self.nodes) == len(self.nodeIDs):
            self.state = 1 #won the game
            return None

        return None

    def nodesneeded(self):
        
        needed = []
        for i in self.nodeIDs:
            needID = True
            for node in self.nodes:
                if node.ID == i:
                    needID = False
            if needID:
                needed.append(i)

        return needed

    def displayinfo(self):
        print("\n")
        print("path ID: " + self.ID)
        print("nodes currently on path:") 
        for node in self.nodes:
            print("\tID: " + node.ID)
            print("\tstate: " + str(node.state))
        print("path state:" + str(self.state))
        print("nodes needed: " + str(self.nodesneeded()))
