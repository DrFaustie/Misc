# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:11:39 2018

@author: Coal1
"""

def Nim(matchsticks,move_limit,k):
    # It is important to understand HOW we reach our conclusions and what our return values mean.
    # Nim() searches the state of the NEXT move
    # Ergo, if we make the next move impossible to win, we win.
    # If we cannot make the next move impossible to win, we lose.

   # If matchsticks == 0, our opponent has found a way to collect the last matchstick during the last move. Mover loses.   
   if matchsticks == 0:
       return False
   # If matchsticks == < 1, our opponent has been forced to make an illegal move, mover wins.
   elif matchsticks < 0:
       return True
   
   # By default we assume the mover can't win, but we change the status if we find a winning move.
   state = False
   for new_k in range(1, move_limit + 1):
       # New move cannot be the same as old move
       if new_k != k:
           if Nim(matchsticks - new_k , move_limit, new_k) == False:
               # Could simply return True here, less clear
               state = True

   return state
                   
        # How many matchsticks left in pile?
        # Which number is banned?
        
        
print(Nim(21,5,0))
#print(Nim(40,4,0))

# We don't consider the whole problem, we consider a subproblem(n,k)
# Suppose we have n sticks, and move k is banned
# If both players play optimally, either the mover has a 100% win strategy, or his opponent has a 100% win strategy.
# If you want to win, select the move that guarantees the next mover loses

# n = 10
# move_list = 5
# k = 5
# new_k = one of [1,2,3,4]
# n will be n - p[new_k]
# k = p[new_k]

# p[n][k] returns True or False
# True == Win | p[n][k]=True if the current mover can win with n sticks left and removing k sticks is banned
# False == Lose | p[n][k]=False if the current mover cannot win with n sticks left and removing k sticks is banned

# for any (n,k)
# search p[n-1][1], p[n-2][2],...,p[n-5][5] (except k)
# if any == 1, p[n][k] = 0
# if all == 0, p[n][k] = 1

# Last move
# n = 1
# if k == 1:
    #p[n][k] = 1
# else:
    #p[n][k] = 0
    
# Bonus Question
# Suppose there are two supercomputers that have all of the entire universe's knowledge downloaded into them.
# They start a game of chess. What are their first moves?