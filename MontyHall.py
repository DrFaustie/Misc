# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:28:44 2018

@author: Coal143
"""
import random

# A python simulation of the Monty Hall problem
def MontyHall(NumTrials):
    """ Runs NumTrials trials of the Monty Hall problem, returning chances of
        contestant successfully winning a Car """
    no_switch = 0
    switch = 0
    for x in range(NumTrials):
        choices = ["A", "B", "C"]
        # The contestant makes a random choice of 3, a 33.3% chance
        contestant_choice = random.choice(choices)
        
        car = random.choice(choices)
        goat = []
        
        for choice in choices:
            if car not in choice:
                goat.append(choice)
        
        # The host reveals one of the other panels, a goat and asks if the contestant wants to switch
        if contestant_choice not in goat:
            removed_choice = random.choice(goat)
        else:
            for choice in goat:
                if choice not in contestant_choice:
                    removed_choice = choice
        choices.remove(removed_choice)
        
        # Contestant doesn't switch
        if contestant_choice == car:
            no_switch = no_switch + 1
        # Contestant switches
        for choice in choices:
            if choice not in contestant_choice:
                change_choice = choice
        contestant_choice = change_choice
        if contestant_choice == car:
            switch = switch + 1
        
    # Return % chance that contestant recieves a car
    no_switch_per = percentage(no_switch, NumTrials)
    switch_per = percentage(switch, NumTrials)
    print("If the contestant sticks with his original choice, he has a roughly " + str(no_switch_per) + " chance of winning a car over " + str(NumTrials) + " amount of games")
    print("By contrast, if the contestant switches his choice, he has a roughly " + str(switch_per) + " chance of winning a car over " + str(NumTrials) + " amount of games")

def percentage(part, whole):
  return 100 * float(part)/float(whole)

MontyHall(10)
MontyHall(100)
MontyHall(1000)
MontyHall(10000)
MontyHall(100000)
MontyHall(1000000)