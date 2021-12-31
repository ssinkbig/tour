#!/usr/bin/python3

import numpy as np
from pprint import pprint

DEBUG = True

def probability(n):
     np.random.seed(1234)
     if np.log2(n) != np.int_(np.log2(n)):
        raise ValueError("Invalid Input. Please put powers of 2.") #Exception
     table = np.zeros((n, n))
     values = np.triu_indices(n, 1)
     prob = np.random.rand(np.sum(np.arange(n)))
     table[values] = prob
     table[values[1], values[0]] = 1 - prob
     return table

def findProb(table, home, away):
     if home == away:
        raise ValueError("Invalid Input. Please put another value")
     return table[away][home]

def main():
    # num_teams = np.int_(input("Input the number of teams: "))
    num_teams = 4
    table = probability(num_teams)
    if DEBUG:
      print("table:")
      pprint(table)

    num_games_in_a_single_tournament = np.int_(np.log2(num_teams))
    if DEBUG:
      print("num_games_in_a_single_tournament", num_games_in_a_single_tournament)

    result = np.ones(num_teams)
    if DEBUG:
        print('result', result)

    games = []
    result = []
    for home_team in range(0,num_teams, 2):
       away_team = home_team + 1
       games.append((home_team, away_team))
       result.append((0.0, 0.0))

    pprint(games)

    run_tournament(games, result, table)

def game_probablities(table, home, away):
    return table[home][away], table[away][home]

def run_tournament(games, results, table):
    for game_i in range(len(games)):
        game = game[game_i]
        game_probablity = game_probablities(game[0], game[1])
        game_result = results[game_i]
        game_result[0] = game_probablity[0]
        game_result[1] = game_probablity[1]
       
#I did not call main as I know that the code is still unfinished.

if __name__ == "__main__":
    main()
