import winningpath as w
import player as p
import node as n
class Game:

    def __init__(self, player1, player2, boardsize):
        self.player1 = player1
        self.player2 = player2
        self.boardsize = boardsize
        self.winner = None
        self.winningpaths = []
        self.nodes = []

    def generatepaths(self, boardsize):
        #horizontal
        for i in range(1, boardsize + 1):
            nodeIDs = []
            fullid = ""
            for j in range(1, boardsize + 1):
                nodeIDs.append(str(i) + str(j))
                fullid = fullid + str(i) + str(j)

            temp = w.Winningpath(fullid, nodeIDs)
            self.winningpaths.append(temp)

        #vertical
        for i in range(1, boardsize + 1):
            nodeIDs = []
            fullid = ""
            for j in range(1, boardsize + 1):
                nodeIDs.append(str(j) + str(i))
                fullid = fullid + str(j) + str(i)

            temp = w.Winningpath(fullid, nodeIDs)
            self.winningpaths.append(temp)

        for i in range(1, boardsize + 1):
            nodeIDs.append(str(i) + str(i))
            fullid = fullid + str(i) + str(i)
        temp = w.Winningpath(fullid, nodeIDs)
        self.winningpaths.append(temp)

        return None

    def haswinner(self):
        
        for path in range (0, len(self.winningpaths)):
            if self.winningpaths[path].state == 1:
                self.winner = self.winningpaths[path].nodes[0].piece
                return True
            else:
                return False
        
    def makemove(self, player):
        if player.mode == "human":
           move = input("enter your move")
           temp = n.Node(player.piece, move)
           Nodes.append(temp)

            for path in self.winningpaths:
                if temp.ID in path.nodeIDs:
                    path.nodes.addnode(temp)

        return None

    def play(self, player):
        
        if self.haswinner() == True:
            print(f"victory for {player.piece}!")
            return None
        else:
            self.makemove(player)
            self.play(player.opponent)

    def main(self, boardsize):
        
        self.generatepaths(boardsize)
        self.play(player1)

if __name__=='__main__':
    
    player1 = p.Player("human", "X")
    player2 = p.Player("human", "O")
    player1.opponent = player2
    player2.opponent = player1
