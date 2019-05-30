#my stuff
from snakeObj import *
from policy_gradients_torch import Agent
from utils import plotLearningNoEpsilons

#Libary stuff
from graphics import *
import tensorflow as tf
import gym
import numpy as np

def main():


    score_history = []
    n_episodes = 2500
    action = agent.choose_action(observation)

    user_quit = False
    #while user_quit == False:
    for i in range(n_episodes)
        win = GraphWin("Snake Game", WIDTH(), HEIGHT())
        game = GameObj(win)
        try:
            while(game.logic(win.checkKey()) == True):
                time.sleep(.4)#this is the game speed!
            user_quit = game.playAgain() #asks if the user whats to play again but it is not down yet
        except:
            print("some error but the user probably clicked the exit button")

        win.close()

main()


