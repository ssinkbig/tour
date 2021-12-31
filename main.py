import numpy as np

n = np.int_(input("Input the number of teams: "))






def probability(n):
     if np.log2(n) != np.int_(np.log2(n)):
        raise ValueError("Invalid Input. Please put powers of 2.") #Exception
     table = np.zeros((n, n))
     values = np.triu_indices(n, 1)
     prob = np.random.rand(np.sum(np.arange(n)))
     table[values] = prob
     table[values[1], values[0]] = 1 - prob
     return table

table = probability(n)

def findProb(home, away):
     if home == away:
        raise ValueError("Invalid Input. Please put another value")
     return table[away][home]

 #1st round : A vs B   C vs D   E vs F  G vs H
 #2nd round : [AB] vs [CD]    [EF] vs [GH]
 #3rd round : [ABCD] vs [EFGH]

 #16 Teams
 #A B C D E F G H
gamesPerTeam = np.power(2, n - 1 - np.log2(n))
temp = np.array([])
prev = np.array([])
fin = np.array([])
x = np.int_(np.log2(n))


def main(x, fin):
     if x == 0:
         return fin
     else:
         if fin.size == 0:
             for i in np.arange(n):
                 if(i%2==0):
                     temp = np.append(temp, findProb(i,i+1))
                 else:
                     temp = np.append(temp, findProb(i,i-1))
                 fin = np.append(fin, temp)
                 temp = np.empty(temp)
             return main(x-1, fin)
         else:
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


print(table)

#I did not call main as I know that the code is still unfinished.


if __name__ == "__main__":
    main(x,fin)
