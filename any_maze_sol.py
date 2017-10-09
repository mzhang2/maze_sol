'''
Title: Get out of any maze
Author: Michael Zhang
Date Created: October 4, 2017
'''
# Subroutines
def turn_right():
    repeat 3:
        turn_left()
        
# Code Starts here
think(0)
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    else:
        pause()
        if front_is_clear():
            move()
        else:
            turn_left()
done()