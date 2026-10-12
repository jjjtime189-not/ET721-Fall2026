"""
Joseph Ali-Shaw
Project 2 part 2
This file will test the function Check_win()'s checks for horizontal and diagonal (down-right) victories
"""
#import needed functions (was unable to only import the needed function as it is part of a class.)
import pytest
from main import *
@pytest.mark.parametrize("row,col,player",[(5,0,"X"),(5,1,"X"),(5,2,"X"),(5,3,"X")])
def test_horizontal(row,col,player):
    game = Connect4()
    # Set up 4 'X' chips in a row on the bottom row
    count=0
    for loop in range(4):
        game.board[row][col+count] = player
        count +=1
    # Call the method to check if they win
    assert game.check_win(player) is True
@pytest.mark.parametrize("row,col,player",[(0,0,"X"),(0,1,"X"),(0,2,"X"),(0,3,"X")])
def test_diagonal_down_right_win(row,col,player):
    game = Connect4()
    # Set up 4 'X' chips in a row on the top row
    count=0
    for loop in range(4):
        game.board[row+count][col+count] = player
        count +=1
    # Call the method to check if they win
    assert game.check_win(player) is True
@pytest.mark.parametrize("row,col,player",[(5,0,"X"),(5,1,"X"),(5,2,"X"),(5,3,"X")])
def test_no_win_state(row,col,player):
    game = Connect4()
    # Set up 3 'X' chips in a row
    count=0
    for loop in range(3):
        game.board[row][col+count] = player
        count +=1
    # Call the method to check if they win
    assert game.check_win(player) is False