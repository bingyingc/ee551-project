import random
import sys
import tkinter as tk
from tkinter import messagebox
from turtle import *
from freegames import line


class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.cubes = [
            {'x': '-200.0', 'y': '66.0', 'position': '0', 'item': ''},
            {'x': '-67.0', 'y': '66.0', 'position': '1', 'item': ''},
            {'x': '66.0', 'y': '66.0', 'position': '2', 'item': ''},
            {'x': '-200.0', 'y': '-67.0', 'position': '3', 'item': ''},
            {'x': '-67.0', 'y': '-67.0', 'position': '4', 'item': ''},
            {'x': '66.0', 'y': '-67.0', 'position': '5', 'item': ''},
            {'x': '-200.0', 'y': '-200.0', 'position': '6', 'item': ''},
            {'x': '-67.0', 'y': '-200.0', 'position': '7', 'item': ''},
            {'x': '66.0', 'y': '-200.0', 'position': '8', 'item': ''}]
        self.tmpPosition = 0


    def drawBoard(self):
        # This method prints out the board with current plays adjacent to a board with index.
        setup(410, 410, 370, 0)
        hideturtle()
        tracer(False)
        line(-67, 200, -67, -200)
        line(67, 200, 67, -200)
        line(-200, -67, 200, -67)
        line(-200, 67, 200, 67)
        update()

    def boardFull(self):
        # This method checks if the board is already full and returns True. Returns false otherwise
        for i in range(len(self.cubes)):
            if self.cubes[i]['item'] == "":
                break
            else:
                return True
        return False

    # def cellIsEmpty(self, cell):
    #     if cell == 0 or cell > 9:
    #         return False
    #     else:
    #         return self.board[cell] == " "

    def drawx(self, x, y):
        "Draw X player."
        line(x, y, x + 133, y + 133)
        line(x, y + 133, x + 133, y)
        print('tmpPosition: '+str(self.tmpPosition))
        self.cubes[self.tmpPosition]['item'] = 'x'
        print('self.cubes ' + self.cubes[self.tmpPosition]['item'])

    def drawo(self, x, y):
        "Draw O player."
        up()
        goto(x + 67, y + 5)
        down()
        circle(62)
        self.cubes[self.tmpPosition]['item'] = 'o'

    # def floor(self,value):
    #     "Round value down to grid with square size 133."
    #     return ((value + 200) // 133) * 133 - 200
    #


    def assignMove(self, x, y):
        state = {'player': 0}
        # assigns the cell of the board to the character ch

        x = ((x + 200) // 133) * 133 - 200
        y = ((y + 200) // 133) * 133 - 200
        print("x: " + str(x), "y: " + str(y))  # get x y values
        for i in range(len(self.cubes)):
            print('item '+str(i)+':'+self.cubes[i]['item'])
            if self.cubes[i]['item'] == '':
                if self.cubes[i]['x'] == str(x) and self.cubes[i]['y'] == str(y):
                    print(self.cubes[i]['x'] + ",,," + self.cubes[i]['y'])
                    self.tmpPosition = i
                    break
                else:
                    continue
            else:
                print('Occupied')
                print(messagebox.showwarning(title='Error', message='this cube is occupied'))
                return
        # use x and y to find cell number
        player = state['player']
        if player == 0:
            print('player==0')
            self.drawx(x,y)
        else:
            self.drawo(x,y)
        update()
        state['player'] = not player
        print("****************")
        return

    def whoWon(self):
        # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string.
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

    def isWinner(self, ch):
        # Given a player's letter, this method returns True if that player has won.
        return ((self.cubes[0]['position'] == ch and self.cubes[1]['position'] == ch and self.cubes[2][
            'position'] == ch) or  # across the top
                (self.cubes[3]['position'] == ch and self.cubes[4]['position'] == ch and self.cubes[5][
                    'position'] == ch) or  # across the middle
                (self.cubes[6]['position'] == ch and self.cubes[7]['position'] == ch and self.cubes[8][
                    'position'] == ch) or  # across the bottom
                (self.cubes[0]['position'] == ch and self.cubes[3]['position'] == ch and self.cubes[6][
                    'position'] == ch) or  # down the left side
                (self.cubes[1]['position'] == ch and self.cubes[4]['position'] == ch and self.cubes[7][
                    'position'] == ch) or  # down the middle
                (self.cubes[2]['position'] == ch and self.cubes[5]['position'] == ch and self.cubes[8][
                    'position'] == ch) or  # down the right side
                (self.cubes[0]['position'] == ch and self.cubes[4]['position'] == ch and self.cubes[8][
                    'position'] == ch) or  # diagonal
                (self.cubes[2]['position'] == ch and self.cubes[4]['position'] == ch and self.cubes[6][
                    'position'] == ch))  # diagonal


def UaU():
    myBoard = TicTacToe()
    turn = 'x'
    gameIsOn = True
    myBoard.drawBoard()
    # while gameIsOn:
        # print("It is the turn for", turn, ". ", end="")
    move = "0"
        # myBoard.assignMove(int(move), turn)
    onscreenclick(myBoard.assignMove)
    winner = myBoard.whoWon()

    if winner != '':
        myBoard.drawBoard()
        print(turn, "wins. Congrats!")
        input("Press Enter to continue")
        gameIsOn = False
    elif myBoard.boardFull():
        myBoard.drawBoard()
        print("It's a tie.")
        input("Press Enter to continue")
        gameIsOn = False
    elif turn == "x":
        turn = "o"
    else:
        turn = "x"
    return

print("Welcome to Tic Tac Toe Series")
myGameLoop = True
while myGameLoop:
    UaU()
