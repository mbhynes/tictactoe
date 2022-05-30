# tictactoe

A commandline version of tictactoe, written in python. Works on Linux, and most likely on Windows and Mac with python and bash installed.

to play, run:
```
python play.py
```
The default will be a 3x3 board with a human player going first, then the computer. Pieces are X and O respectively. 
Board sizes other than 3x3 are not currently supported and may cause an error, support will be added in the future.

Check
```
python play.py -h
```
for additional options to customize the game.

For example, running:
```
python play.py 3 computer X human O
```
will start a game where a computer player has the first move with their piece being X, followed by a human player with their piece being O.

To play, when prompted for your move, enter the row and column number of the square you want.

11 12 13  

21 22 23  

31 32 33   is what the entry for each square is

for example to go to the middle square, type 22, top left type 11, etc.
   
