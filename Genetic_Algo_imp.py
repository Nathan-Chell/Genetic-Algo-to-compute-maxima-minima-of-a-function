#Implimentation of a genetic algo

from copy import deepcopy
from random import randint, random

#Int the function we want to calculate the minima/ maxima of.
def objective(x):
	return x[0]**2.0 + x[1]**2.0

#Initilise a random population.
def starting_pop(n_pop, n_bits, bounds):

    pop = []
    for _ in range(n_pop):
        arr = []
        for __ in range(len(bounds)):
            temp = ""
            for ___ in range(n_bits):
                temp += str(randint(0,1))
            arr.append(temp)
        pop.append(arr)
    return pop

def decode(bounds, n_bits, bitstring):
    decoded = list()
    largest = 2**n_bits
    for i in range(len(bounds)):
        #extracting the substring
        #convert bitstring to string of chars
        chars = ''.join([str(s) for s in bitstring[i]])
        #convert to integer
        integer = int(chars, 2)
        #scale value to correct range
        value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
        decoded.append(value)
    return decoded

def selection(pop, values, k=3):

    #source: https://www.geeksforgeeks.org/tournament-selection-ga/
    #Tournament selection
    rand_pop = randint(0, len(pop) - 1)
    for i in range(0, k):
        selected_pop = randint(0, len(pop) - 1)
        if values[selected_pop] < values[rand_pop]:
            rand_pop = selected_pop
    return pop[rand_pop]

def crossover(pair, r_cross, n_bits):
    #copy values into the children
    c1, c2 = deepcopy(pair[0]), deepcopy(pair[1])

    #if a random float between 0,1 is less than our cross overrate
    #then we change the bits, this results in a 90% crossover with a r_cross of 0.9
    #give enough iterations.
    if random() < r_cross:
        #Select a point in the bitstring to change e.g bit 4 onwards or bit 7 onwards
        point = randint(1, (n_bits-2))

        c1 = pair[0][:point] + pair[1][point:]
        c2 = pair[1][:point] + pair[0][point:]

    #May not always crossover
        #print(len(c1))
    return [c1, c2]

def mutation(cur, r_mut):

    for i in range(len(cur)):
        if random() < r_mut:
            cur[i] = 1 - int(cur[i])

    return cur


def main():

    #Int vars
    #Population size
    n_pop = 100
    #Total iterations
    n_iter = 100
    # crossover rate
    r_cross = 0.9
    # define range for input
    bounds = [[-5.0, 5.0], [-5.0, 5.0]]
    # bits per variable
    n_bits = 16
    # mutation rate
    r_mut = 1.0 / (float(n_bits) * len(bounds))

    pop = starting_pop(n_pop, n_bits, bounds)

    #Track best solutions
    best, best_eval = 0, objective(decode(bounds, n_bits, pop[0]))

    #enumerate generations
    for gen in range(n_iter):
        #decode population
        decoded = [decode(bounds, n_bits, p) for p in pop]

        #determine the values of the current population.
        values = [objective(d) for d in decoded]
        #assign new best_eval
        for i in range(n_pop):
            if values[i] < best_eval:
                best, best_eval = pop[i], values[i]
                print("Found new best in gen: {}, current best_eval: {}, from values: {}".format(gen, values[i], decoded[i]))

        #select parents for new Population
        selected = [selection(pop, values, 3) for _ in range(n_pop)]
        #after selecting the parents we need to alter them to create the new generation

        children = list()
        for i in range(0, n_pop):
            temp = []
            for c in crossover(selected[i], r_cross, n_bits):
                #children.append(mutation(c, r_mut))
                temp.append(c)
            children.append(temp)
        pop = children

    print("Done")
    decoded = decode(bounds, n_bits, best)
    print("Values {}, result in the best score of {}".format(decoded, best_eval))


if __name__ == '__main__':
    main()
