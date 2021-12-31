#!/usr/bin/python3

import numpy as np

def probability(n):
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

def init_fin(n, table):
    fin = np.array([])
    temp = np.array([])
    for i in np.arange(n):
        if(i%2==0):
            temp = np.append(temp, findProb(table, i,i+1))
        else:
            temp = np.append(temp, findProb(table, i,i-1))

        fin = np.append(fin, temp)
        temp = np.empty(temp)
    return fin

def main():
    # num_teams = np.int_(input("Input the number of teams: "))
    num_teams = 4
    table = probability(num_teams)

    gamesPerTeam = np.power(2, num_teams - 1 - np.log2(num_teams))
    prev = np.array([])

    num_games_in_a_single_tournament = np.int_(np.log2(num_teams))
    fin = init_fin(num_teams, table)
    run_tournament(num_games_in_a_single_tournament,fin, prev)
    print(table)

def run_tournament(x, fin, prev):

     if x == 0:
         return fin

     prev = fin  #prev에 일단 저장 후 fin을 비움
     fin = np.empty(fin)
     for i in np.arange(len(prev)): #각 prev의 index마다. 여기서 index 0 : [A->B,B->A], 1 : [C->D,D->C], 2 : [E->F,F->E], 3: [G->H,H->G]
         tempProb = np._float(0)
         if(i%2 == 0):
             index1 = np._int(0)
             index2 = np._int(0)
             for h in np.arange(prev[i]):
                 for a in np.arange(prev[i+1]):
                    temp = np.append(temp, tempProb)
                 tempProb = 0
         else:
             for h in np.arange(prev[i]):
                 for a in np.arange(prev[i-1]):
                     float += h*a
                     temp = np.append(temp, tempProb)
                 tempProb = 0
         return main(x-1, fin)



#I did not call main as I know that the code is still unfinished.


if __name__ == "__main__":
    main()
