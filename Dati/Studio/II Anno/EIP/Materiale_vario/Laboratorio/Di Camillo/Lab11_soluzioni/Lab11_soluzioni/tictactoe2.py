# tictactoe2.py
from myinput import *

def main() :
   while True :
      # scacchiera vuota
      board = TicTacToeBoard('.')
      # a chi tocca ?
      player = 'X'
      while not board.isWinner('X') and not board.isWinner('O') \
            and not board.isFull() :
         print(board)
         print("Inserire la mossa del giocatore", player)
         while True :
            row = inputDecimalInteger("Riga (0, 1, 2, dall'alto): ")
            if 0 <= row <= 2 :
               break
         while True :
            column = inputDecimalInteger("Colonna (0, 1, 2, da sinistra): ")
            if 0 <= column <= 2 :
               break
         if board.isFree(row, column) :
            # casella libera
            board.setCharInPosition(row, column, player)
            if player == 'X' :
               player = 'O'
            else :
               player = 'X'
         else :
            # casella occupata
            print("Mossa errata")
      # partita finita
      print(board)
      if board.isWinner('X') :
         print("Vittoria del giocatore X")
      elif board.isWinner('O') :
         print("Vittoria del giocatore O")
      else :
         print("Pareggio")
      while True :
         s = input("Un'altra partita? (SI o NO) ")
         if s == "SI" or s == "NO" :
            break
      if s == "NO" :
         break

class TicTacToeBoard :

   def __init__(self, freeChar) :
      self._freeChar = freeChar
      self._board = [ [freeChar]*3, [freeChar]*3, [freeChar]*3 ]

   def isFull(self) :
      for i in range(3) :
         for j in range(3) :
            if self._board[i][j] == self._freeChar :
               return False
      return True
      
   def isFree(self, row, column) :
      return self._board[row][column] == self._freeChar
      
   def setCharInPosition(self, row, column, c) :
      self._board[row][column] = c
      
   def __repr__(self) :
      s = "Situazione\n"
      for i in range(3) :
         for j in range(3) :
            s += self._board[i][j]
         s += "\n"
      return s
      
   def isWinner(self, player) :
      # c'è una riga completa?
      for i in range(3) :
         count = 0
         for j in range(3) :
            if self._board[i][j] == player :
               count += 1
         if count == 3 :
            return True
      # c'è una colonna completa?
      for i in range(3) :
         count = 0
         for j in range(3) :
            if self._board[j][i] == player :
               count += 1
         if count == 3 :
            return True
      # c'è una diagonale completa?
      count = 0
      for i in range(3) :
         if self._board[i][i] == player :
            count += 1
      if count == 3 :
         return True
      count = 0
      for i in range(3) :
         if self._board[i][2-i] == player :
            count += 1
      if count == 3 :
         return True
      return False
    
main()
