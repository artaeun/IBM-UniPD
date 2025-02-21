# tictactoe.py
from myinput import *

def main() :
   while True :
      # scacchiera vuota
      board = [ ['.']*3, ['.']*3, ['.']*3 ]
      # a chi tocca ?
      player = 'X'
      while not isWinner('X', board) and not isWinner('O', board) \
            and not isFull(board) :
         display(board)
         print("Inserire la mossa del giocatore", player)
         while True :
            row = inputDecimalInteger("Riga (0, 1, 2, dall'alto): ")
            if 0 <= row <= 2 :
               break
         while True :
            column = inputDecimalInteger("Colonna (0, 1, 2, da sinistra): ")
            if 0 <= column <= 2 :
               break
         if board[row][column] == '.' :
            # casella libera
            board[row][column] = player
            if player == 'X' :
               player = 'O'
            else :
               player = 'X'
         else :
            # casella occupata
            print("Mossa errata")
      # partita finita
      display(board)
      if isWinner('X', board) :
         print("Vittoria del giocatore X")
      elif isWinner('O', board) :
         print("Vittoria del giocatore O")
      else :
         print("Pareggio")
      while True :
         s = input("Un'altra partita? (SI o NO) ")
         if s == "SI" or s == "NO" :
            break
      if s == "NO" :
         break

def isFull(b) :
    for i in range(3) :
       for j in range(3) :
          if b[i][j] == '.' :
             return False
    return True

def display(b) :
   print("Situazione")   
   print()
   for i in range(3) :
      for j in range(3) :
         print(b[i][j], end="")
      print()
   print()
      
def isWinner(player, board) :
   # c'è una riga completa?
   for i in range(3) :
      count = 0
      for j in range(3) :
         if board[i][j] == player :
            count += 1
      if count == 3 :
         return True
   # c'è una colonna completa?
   for i in range(3) :
      count = 0
      for j in range(3) :
         if board[j][i] == player :
            count += 1
      if count == 3 :
         return True
   # c'è una diagonale completa?
   count = 0
   for i in range(3) :
      if board[i][i] == player :
         count += 1
   if count == 3 :
      return True
   count = 0
   for i in range(3) :
      if board[i][2-i] == player :
         count += 1
   if count == 3 :
      return True
   return False
    
main()