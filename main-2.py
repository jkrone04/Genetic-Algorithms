#    Names:	Nathaniel Mahlum 	(Nathaniel.Mahlum@tufts.edu)
#           Jacob Kroner		(Jacob.Kroner@tufts.edu)
#    Assignment 4: Genetic Algorithms
#  ____________________________________________________________________

from chromosome import Chromosome
from population import Population
from queue import PriorityQueue
import random

# Runs the genetic algorithm on a population of
# chromosomes of the size entered as a parameter
def run (populationSize):
    
    # Initialize population
    p = Population(populationSize)
    done = False
    
    # While the population size has not been
    # culled down to one "fittest" Chromosome,
    # continue to cull
    while (not(done)):
        done = p.cull()
    
    # Return the resulting population containing
    # only the "fittest" Chromosome
    return (p.getFittestChromosome())
    

def main ():
    
    # Get valid user input for population size (greater than 0 and an integer)
    while (True):
        try:
            size = int(input("Please input the size of population you would like to cull from (greater than 0): "))
        except ValueError:
            print ("Invalid Input: Please try again and input an integer!")
            continue
        else:
            if (size < 1):
                print ("Invalid Input: Please try again and input an integer greater than 0!")
                continue
            else:
                
                # If input is valid, run the algorithm on a randomly generated population of this
                # size, getting the result returned from the run function
                fittest = run(int(size))
                break
    
    # Print out the fittest Chromosome returned by the run function
    print ("The resulting Chromosome from your population of size " + str(size) + " has these specifications: ")
    fittest.printChromosome()
            
        

if __name__ == '__main__':
    main()



