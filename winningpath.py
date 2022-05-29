class Winningpath:

    def __init__(self, ID, nodeIDs):

        self.ID = ID
        self.nodeIDs = nodeIDs
        self.nodes = []  
        self.state = 0

    def addnode(self, node):
        nodes.append(node)
        for i in range(0, len(nodes)):
            if nodes[i].ID != nodes[i+1].ID:
                state = -1 #cant win in this winningpath now

        if len(nodes) = len(nodeIDs):
            state = 1 #won the game

        return None

    def nodesneeded():

        needed = []
        for i in range(0, len(ID)-1, 2):
            if (ID[i] + ID[i+1]) not in nodeIDs:
                needed.append(ID[i] + ID[i+1])

        return needed
