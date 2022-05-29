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

        #diagonal top left bottom right
        nodeIDs = []
        fullid = ""
        
        for i in range(1, boardsize + 1):
            nodeIDs.append(str(i) + str(i))
            fullid = fullid + str(i) + str(i)
        temp = w.Winningpath(fullid, nodeIDs)
        self.winningpaths.append(temp)

        #diagonal bottom left top right
        nodeIDs = []
        fullid = ""

        for i in range(1, boardsize + 1):
            nodeIDs.append(str(self.boardsize +1 - i) + str(i))
            fullid = fullid + str(i) + str(i)
        temp = w.Winningpath(fullid, nodeIDs)
        self.winningpaths.append(temp)

        return None

    def haswinner(self):
        
        for path in range (0, len(self.winningpaths)):
            if self.winningpaths[path].state == 1: #winner found
                self.winner = self.winningpaths[path].nodes[0].state
                return True

        return False

    def validmove(self, move):
        if len(move) != 2 or type(int(move)) != int:
            return False
        if not (int(move[0]) > 0 and int(move[0]) <= self.boardsize):
            return False
        if not (int(move[1]) > 0 and int(move[1]) <= self.boardsize):
            return False

        for node in self.nodes:
            if node.ID == move:
                return False

        else:
            return True

    def makemove(self, player):
        if player.mode == "human":
           self.print()
           print(f"enter your move, {player.piece}!")
           invalid = True
           while invalid:
                move = input()
                if self.validmove(move):
                    invalid = False
                    break
                print(f"invalid move! try again, {player.piece}!")

           
           temp = n.Node(player.piece, move)
           self.nodes.append(temp)

           for path in self.winningpaths:
               if temp.ID in path.nodeIDs:
                   path.addnode(temp)

        return None

    def play(self, player):
        
        if self.haswinner() == True:
            print(f"victory for {player.opponent.piece}!")
            return None
        elif len(self.nodes) == self.boardsize**2:
            print("tie game!")
            return None

        else:
            self.makemove(player)
            self.play(player.opponent)

    def searchtoprint(self, ID):
        for node in self.nodes:
            if node.ID == ID:
                return node.state

        return " "

    def print(self):
        type1 = "   #   #   "
        type2 = "###########"
        print(type1)
        print(" " + self.searchtoprint("11") + " " + "#" + " " + self.searchtoprint("12")+ " " + "#" + " " + self.searchtoprint("13") + " ")
        print(type1)
        print(type2)
        print(type1)
        print(" " + self.searchtoprint("21") + " " + "#" + " " + self.searchtoprint("22")+ " " + "#" + " " + self.searchtoprint("23") + " ")
        print(type1)
        print(type2)
        print(type1)
        print(" " + self.searchtoprint("31") + " " + "#" + " " + self.searchtoprint("32")+ " " + "#" + " " + self.searchtoprint("33") + " ")

    def main(self):
        
        self.generatepaths(self.boardsize)
        self.play(player1)

if __name__=='__main__':
    
    player1 = p.Player("human", "X")
    player2 = p.Player("human", "O")
    player1.opponent = player2
    player2.opponent = player1
    game = Game(player1, player2, 3)
    game.main()
