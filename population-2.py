#    Names:	Nathaniel Mahlum 	(Nathaniel.Mahlum@tufts.edu)
#           Jacob Kroner		(Jacob.Kroner@tufts.edu)
#    Assignment 4: Genetic Algorithms
#  ____________________________________________________________________

from chromosome import Chromosome
from queue import PriorityQueue
import random
import math

class Population:
    
    
    # Initializer for a population of different backpack
    # configurations (Chromosomes)
    def __init__(self, n):
        
        # Desired population size is inputted by the user
        self.size = n
        self.population = []
        
        # The desired number of Chromosomes are then generated randomly and
        # added to the list used to store the population of Chromosomes
        for i in range(n):
            newChromosome = Chromosome([random.randint(0,1) for i in range(7)])
            self.population.append(newChromosome)
    
    # A getter function for the size of the population
    def getSize(self):
        return self.size
    
    # Prints out the specifications of the current population, including
    # the weight, priority and fitness values for each Chromosome in the
    # population as well as their gene configuration
    def printPop(self):
        for i in self.population:
            i.printChromosome()
    
    
    # A getter function for the fittest Chromosome configuration
    # in the current population.
    def getFittestChromosome(self):
        
        # Sort the population to make sure the Chromosome at
        # the front is the fittest
        self.population.sort()
        
        # Return the fittest Chromosome
        return self.population[0]
        
    
    
    # Culls the population
    def cull(self):
        
        # Sorts the population in order from highest
        # fitness to lowest fitness
        self.population.sort()
        
        # Cull the population by 50%, making the remaining the
        # population of parents of the new generation
        parents = self.population[:len(self.population)//2]
        
        # Initialize an empty list that will hold the children
        # from each parent pair
        children = []
        
        # If there is only one parent left, make the population this
        # parent as no more culling or crossover can be done. Return
        # true as the population can't be culled anymore
        if (len(parents) == 1):
            self.population = parents
            self.size = len(self.population)
            return True
        
        # While there are enough pairs to perform crossover,
        # find too parents, use the reproduction function to 
        # get the list of their two children following crossover
        # and then call the mutation function on each, appending
        # the resulting child to the list of children
        while (len(parents) > 1):
            p1 = parents.pop(0)
            p2 = parents.pop(0)
            
            offspring = Chromosome.reproduce(p1, p2)
            
            for i in offspring:
                i.mutation()
                children.append(i)
        
        # If there is a parent left, call the mutation function on
        # it and then append it to the list of children
        if (len(parents) == 1):
            child = parents.pop(0)
            child.mutation()
            children.append(child)
            
        # Make the population equal to the new generation
        # and update the length respectively
        self.population = children
        self.length = len(self.population)
        
        # Return false as there is still more culling to be done
        return False
    
        
        
           
        
        
        


    

    
                    