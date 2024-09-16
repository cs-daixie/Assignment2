#!/usr/bin/env python͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
import traceback
from isolation import Board, game_as_text
from test_players import RandomPlayer, HumanPlayer, Player
import platform

if platform.system() != 'Windows':
    import resource

from time import time, sleep

def correctOpenEvalFn(yourOpenEvalFn):
    print()
    try:
        sample_board = Board(RandomPlayer(), RandomPlayer())
        # setting up the board as though we've been playing͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
        board_state = [
            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'K2'],
            [' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', 'X'],
            ['X', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' '],
            [' ', ' ', 'K1', ' ', ' ', ' ', 'X', 'X', ' '],
            [' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X'],
            [' ', ' ', ' ', 'X', 'X', ' ', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X']
        ]
        sample_board.set_state(board_state, True)
        #test = sample_board.get_legal_moves()͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
        h = yourOpenEvalFn()
        print('OpenMoveEvalFn Test: This board has a score of %s.' % (h.score(sample_board, sample_board.get_active_player())))
    except NotImplementedError:
        print('OpenMoveEvalFn Test: Not implemented')
    except:
        print('OpenMoveEvalFn Test: ERROR OCCURRED')
        print(traceback.format_exc())

    print()

def beatRandom(yourAgent):

    """Example test you can run
    to make sure your AI does better
    than random."""

    print("")
    try:
        r = RandomPlayer()
        p = yourAgent()
        game = Board(p, r, 9, 9)
        output_b = game.copy()
        winner, move_history, termination = game.play_isolation(time_limit=5000, print_moves=True)
        print("\n", winner, " has won. Reason: ", termination)
        # Uncomment to see game͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
        # print game_as_text(winner, move_history, termination, output_b)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
    except NotImplementedError:
        print('CustomPlayer Test: Not Implemented')
    except:
        print('CustomPlayer Test: ERROR OCCURRED')
        print(traceback.format_exc())
    
    print()


def minimaxTest(yourAgent, minimax_fn):
    """Example test to make sure
    your minimax works, using the
    OpenMoveEvalFunction evaluation function.
    This can be used for debugging your code
    with different model Board states.
    Especially important to check alphabeta
    pruning"""

    # create dummy 9x9 board͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
    print("Now running Minimax test 1.")
    print()
    try:
        def time_left():  # For these testing purposes, let's ignore timeouts
            return 10000

        player = yourAgent() #using as a dummy player to create a board
        sample_board = Board(player, RandomPlayer())
        # setting up the board as though we've been playing͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
        board_state = [
            [' ', ' ', 'K1', 'X', 'X', 'X', ' ', ' ', ' '],
            ['X', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' '],
            [' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', ' '],
            ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', ' ', ' ', 'X', 'K2', ' ', ' '],
            [' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        sample_board.set_state(board_state, True)

        test_pass = True

        expected_depth_scores = [(1, -3), (2, -2), (3, -1), (4, -1), (5, 0)]
        
        for depth, exp_score in expected_depth_scores:
            move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=True)
            if exp_score != score:
                print("Minimax failed for depth: ", depth)
                test_pass = False
            else:
                print("Minimax passed for depth: ", depth)

        if test_pass:
            print()
            print("Now running Minimax test 2.")
            print()
            player = yourAgent()
            sample_board = Board(RandomPlayer(),player)
            # setting up the board as though we've been playing͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏︀͏󠄑͏󠄂͏︍
            board_state = [
                [' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' '],
                ['X', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' '],
                [' ', 'X', 'X', 'X', 'X', ' ', 'X', 'X', ' '],
                [' ', ' ', 'X', ' ', ' ', 'X', 'X', ' ', 'X'],
                [' ', ' ', 'X', 'X', 'X', 'X', 'K2', 'X', 'X'],
                [' ', ' ', ' ', 'K1', 'X', 'X', 'X', 'X', ' '],
                [' ', ' ', ' ', 'X', ' ', 'X', 'X', 'X', 'X'],
                [' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X'],
                [' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ']
            ]
            sample_board.set_state(board_state, p1_turn=True)

            test_pass = True

            expected_depth_scores = [(1, -1), (2, 1), (3, 0), (4, -2), (5, -3)]

            for depth, exp_score in expected_depth_scores:
                move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=False)
          
                if exp_score != score:
                    print("Minimax failed for depth: ", depth)
                    test_pass = False
                else:
                    print("Minimax passed for depth: ", depth)

        if test_pass:
            print("Minimax Test: Runs Successfully!")

        else:
            print("Minimax Test: Failed")

    except NotImplementedError:
        print('Minimax Test: Not implemented')
    except:
        print('Minimax Test: ERROR OCCURRED')
        print(traceback.format_exc())
