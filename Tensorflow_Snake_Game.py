from graphics import *
from snakeObj import *
#import tensorflow as tf
#constants


def main():


    win = GraphWin("Snake Game", WIDTH(), HEIGHT())
    game = GameObj(win)
    try:
        while(game.logic(win.checkKey()) == True):
            time.sleep(.1)#this is the game speed!
        game.playAgain()#asks if the user whats to play again but it is not down yet
    except:
        print("some error but the user probably clicked the exit button")
    
    win.close()

main()


