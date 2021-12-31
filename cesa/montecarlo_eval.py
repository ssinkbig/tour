#!/usr/bin/python3

from util import time_usage
# TODO(cesa): Replace with numpy random number generator.
from util import Mersenne
from util import is_power_of_two
# TODO(cesa): Replace with similiar numpy class.
from matrix import Matrix
from pprint import pprint

DEBUG = False
N = 100000
TEAMS = 16
assert is_power_of_two(TEAMS) 

rng = Mersenne()

def random_team_odds():
  team_odds = Matrix(TEAMS,TEAMS)
  for home_team in range(TEAMS):
    for away_team in range(TEAMS):
      if home_team == away_team: continue
      team_odds[home_team][away_team] = round(rng.random_uniform_float(),4)
  return team_odds

def random_pick_home_or_away_emplace(teams):
  home_team_idx = rng.random_int32(len(teams)-1)
  home_team = teams[home_team_idx]
  del teams[home_team_idx]
  away_team_idx = rng.random_int32(len(teams)-1)
  away_team = teams[away_team_idx]
  del teams[away_team_idx]
  return (home_team, away_team) 

def random_brackets():
  brackets = []
  teams =  list(range(TEAMS))
  while len(teams):
    brackets.append(random_pick_home_or_away_emplace(teams))
  return brackets

def play_randomly_and_collect_stats(brackets, team_odds):
  num_wins = [0]*TEAMS
  for i in range(N):
    b = brackets
    winners = []
    while len(b):
      game = b[0]
      home_team, away_team = game
      odds_for_game = team_odds[home_team][away_team]
      winner = (
        home_team if rng.random_uniform_float() < odds_for_game else away_team
      )
      winners.append(winner)
      if len(winners) == 2:
        b.append(random_pick_home_or_away_emplace(winners))
      b = b[1:]
    tournament_winner = winners[0]
    num_wins[tournament_winner] += 1
  for team in range(TEAMS):
    num_wins[team] = float(num_wins[team]) / float(N) 
  num_wins = list(zip(range(TEAMS), num_wins))
  return num_wins 

@time_usage
def monte_carlo_team_tournament():
  # Create tournament, who plays who and when.
  brackets = random_brackets()
  # Random probablity table.
  team_odds = random_team_odds()
  if DEBUG: print('brackets:\n', brackets)
  if DEBUG: print('team_odds:\n', team_odds)
  # Randomly play the tournament N times and report final stats.
  team_win_stats = play_randomly_and_collect_stats(brackets, team_odds)
  print('team_win_stats:')
  pprint(team_win_stats)

if __name__ == "__main__":
  monte_carlo_team_tournament()