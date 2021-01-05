import random

global population
global mutation_rate

population = []
mutation_rate = 0.2

#initialize population
for i in range(4):
    # create a random chromosome
    a = [0]*6
    for j in range(5):
        a[j] = random.randrange(0,2)
    population.append(a)

# function to perform crossover between two chromosomes
def crossover(a, b):
    if len(a) == len(b):
        cross_point = random.randrange(len(a))
        #print("Crossover point is", end=' ')
        #print(cross_point)
    else:
        print("Error. Chromosomes not the same length.")

    # for i in range(cross_point):
    #     temp = a[i]
    #     a[i] = b[i]
    #     b[i] = temp
    temp = a[cross_point]
    a[cross_point] = b[cross_point]
    b[cross_point] = temp

    return[a, b]

#function to mutate a chromosome
def mutate(a):
    temp = a
    p_none_cumulative = 1 - mutation_rate
    p_none_each = p_none_cumulative ** (1/6)
    for i in range(len(a)):
        if random.random() > p_none_each:
            print('There was a mutation in chromosome', end=' ')
            print(temp, end=' ')
            print('at position', end=' ')
            print(i)
            a[i] = 1 - a[i]
            print('Result is ', end=' ')
            print(a)
            print('')
    return a

def in_position(hand, chromosome): #returns True for check, False for bet
    if hand == 'Q':
        if chromosome[0] == 0:
            return True
        else:
            return False
    if hand == 'K':
        if chromosome[1] == 0:
            return True
        else:
            return False
    if hand == 'A':
        if chromosome[2] == 0:
            return True
        else:
            return False

def out_position(hand, chromosome): #returns True for fold, False for call
    if hand == 'Q':
        if chromosome[3] == 0:
            return True
        else:
            return False
    if hand == 'K':
        if chromosome[4] == 0:
            return True
        else:
            return False
    if hand == 'A':
        if chromosome[5] == 0:
            return True
        else:
            return False

def decide_winner(a_card, b_card):
    if a_card == 'A':
        return True
    elif b_card == 'Q':
        return True
    elif a_card == 'Q':
        return False
    elif b_card == 'A':
        return False

def play_hand(a, b):
    deal = random.sample(['A', 'K', 'Q'], k=2)
    playerA_card = deal[0]
    playerB_card = deal[1]
    rollA = -1 #each players antes 1
    rollB = -1
    # print('Player A is dealt', end=' ')
    # print(playerA_card, end=' ')
    # print('and Player B is dealt', end=' ')
    # print(playerB_card)

    if in_position(playerB_card, b):
        # print('Player B checks.')
        winner = decide_winner(playerA_card, playerB_card)
        if winner:
            rollA += 2
        else:
            rollB += 2
    else:
        # print('Player B bets.')
        if out_position(playerA_card, a):
            # print('Player A folds.')
            winner = False
            rollB += 2
        else:
            # print('Player A calls.')
            rollA -= 1
            rollB -= 1
            winner = decide_winner(playerA_card, playerB_card)
            if winner:
                rollA += 4
            else:
                rollB += 4


    # if winner:
    #     print('Player A wins!')
    # else:
    #     print('Player B wins!')

    return [rollA, rollB]

def heads_up_4_rollz(a, b):
    bankrollA = 0
    bankrollB = 0

    for _ in range(1000):
        result = play_hand(a, b)
        bankrollA += result[0]
        bankrollB += result[1]

    for _ in range(1000):
        result = play_hand(b, a)
        bankrollA += result[1]
        bankrollB += result[0]

    return [bankrollA, bankrollB]

def run_generation(pop):
    global population
    fitness = [0]*len(pop)

    #have each chromosome play each of the others and store cumulative fitness
    for i in range(len(pop)-1):
        results = heads_up_4_rollz(pop[i], pop[i+1])
        fitness[i] += results[0]
        fitness[i+1] += results[1]

    #find two fittest chromosomes
    most_fit = [fitness.index(x) for x in sorted(fitness, reverse=True)[:2]]
    print(pop[most_fit[0]], pop[most_fit[1]])
    #crossover two most  and add to population
    children = crossover(pop[most_fit[0]], pop[most_fit[1]])
    population.append(mutate(children[0]))
    population.append(mutate(children[1]))

#test

for i in range(50):

    if i == 25:
        mutation_rate = 0.02

    print('Generation '+str(i)+' fittest:', end=' ')
    run_generation(population)
