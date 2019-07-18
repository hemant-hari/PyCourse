# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:28:57 2019

@author: heman
"""

import tkinter as tk

class Display():
    def __init__(self, board0):
        self.window = tk.Tk()
        self.window.resizable(0, 0) # this prevents from resizing the window
        self.window.title("Tic Tac Toe")
        self.gameboard = board0
        self.turn = 1
        # creating another 'Frame' for the button below the 'input_frame'
        btns_frame = tk.Frame(self.window, width = 400, height = 400, bg = "grey")
        btns_frame.pack()
        # second row
        seven = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(0,0))
        eight = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(1,0))
        nine = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(2,0))
        # third row
        four = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(0,1))
        five = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(1,1))
        six = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(2,1))
        # fourth row
        one = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(0,2))
        two = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(1,2))
        three = tk.Button(btns_frame, text = ".", fg = "black", width = 15, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.btn_click(2,2))
        
        self.buttonMatrix = [[seven, eight, nine],
                             [four, five, six],
                             [one, two, three]]
        
        for i in range(3):
            for j in range(3):
                self.buttonMatrix[i][j].grid(row = i, column = j, padx = 1, pady = 1)
        
    def start(self):
        self.window.mainloop()
    
    def update(self):
        for i in range(3):
            for j in range(3):
                self.buttonMatrix[i][j]["text"] = self.gameboard.grid[i][j]
    
    def btn_click(self,x,y):
        if self.turn % 2 == 0:
            self.gameboard.placeX(x,y)
        else:
            self.gameboard.placeO(x,y)
        self.turn += 1
        self.update()
        hasWon, state = self.gameboard.checkWin()
        
        if hasWon:
            print(state + " has won! Well played!")
            self.window.destroy()
        
        if state == "draw":
            print("It's a draw!")
            self.window.destroy()
        

class Board():
    def __init__(self):
        self.state = "running"
        self.grid = [[".",".","."],
                     [".",".","."],
                     [".",".","."]]
    
    def checkValidCoords(self,x,y):
        if self.grid[y][x] != ".":
            return False
        if x > 2 or x < 0:
            return False
        if y > 2 or y < 0:
            return False
        
        return True
        
    def placeX(self,x,y):
        if not self.checkValidCoords(x,y):
            return False
        self.grid[y][x] = "X"
        return True
    
    def placeO(self,x,y):
        if not self.checkValidCoords(x,y):
            return False
        self.grid[y][x] = "O"
        return True
    
    def printGrid(self):
        print("  1 2 3")
        i = 1
        for row in self.grid:
            print(i, end=" ")
            for piece in row:
                if piece == 0:
                    print(".", end = " ")
                else:
                    print(piece, end = " ")
            print(" ")
            i+= 1
    
    def checkWin(self):
        numpieces = 0
        
        for a in range(3):
            for b in range(3):
                if self.grid[a][b] != ".":
                    numpieces += 1
            #Check Rows
            if self.grid[a][0] == self.grid[a][1] == self.grid[a][2]:
                if self.grid[a][0] != ".":
                    return True, self.grid[a][0]
            #Check Columns
            if self.grid[0][a] == self.grid[1][a] == self.grid[2][a]:
                if self.grid[0][a] != ".":
                    return True, self.grid[0][a]
        
        #Check Diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
                if self.grid[1][1] != ".":
                    return True, self.grid[0][0]
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
                if self.grid[1][1] != ".":
                    return True, self.grid[1][1]
        
        if numpieces < 9:
            return False, "running"
        
        return False, "draw"
    
class Oxo():
    def __init__(self):
        self.state = "running"
        self.board = Board()
        self.turn = 1
        self.disp = Display(self.board)
    
    def start(self):
        u_input = input("Put in place to put first piece in format xy (eg: 11, 23, 31): ")
        x = int(u_input[0]) - 1
        y = int(u_input[1]) - 1
        print(x,y)
        if self.board.checkValidCoords(x,y):
            print("valid coords success")
            self.board.placeX(x,y)
            self.turn += 1
            self.board.printGrid()
        while self.state == "running":
            u_input = input("Put in place to put next piece: ")
            x = int(u_input[0]) - 1
            y = int(u_input[1]) - 1
            if self.board.checkValidCoords(x,y):
                if self.turn % 2 == 0:
                    self.board.placeO(x,y)
                else:
                    self.board.placeX(x,y)
                self.board.printGrid()
                self.turn += 1
                x, self.state = self.board.checkWin()
                
        print("################################")
        
        if self.state == "draw":
            print("It's a draw")
            return
        
        print(self.state + " Won!")
        
    def dispStart(self):
        self.disp.start()
                
game = Oxo()

game.dispStart()