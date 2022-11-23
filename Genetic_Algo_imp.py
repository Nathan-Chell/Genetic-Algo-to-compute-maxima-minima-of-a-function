#Implimentation of a genetic algo

from random import randint

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


if __name__ == '__main__':
    main()
