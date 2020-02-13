#    Names:	Nathaniel Mahlum 	(Nathaniel.Mahlum@tufts.edu)
#           Jacob Kroner		(Jacob.Kroner@tufts.edu)
#    Assignment 4: Genetic Algorithms
#  ____________________________________________________________________

import random

GLOBAL_WEIGHT   = [20, 30, 60, 90, 50, 70, 30]
GLOBAL_PRIORITY = [6,  5,  8,  7,  6,  9,  4]
MUTATION_FACTOR = 10000


class Chromosome:


    # Initializes the chromosome to the genes that are entered
    # in the form of a list. Calculates the weight and priority
    # of the chromosome using the global constant values declared
    # at the top. It also uses these values to calculate the 
    # fitness of the chromosome given its weight (overweight ==
    # low fitness)
    def __init__(self, genes):
        
        # Initializes all values
        self.genes = genes
        self.weight = 0
        self.priority = 0
    
        # Calculates weight and priority of Chromosome
        for i in range(len(self.genes)):
            if (self.genes[i]):
                self.weight += GLOBAL_WEIGHT[i]
                self.priority += GLOBAL_PRIORITY[i]
        
        # Calls the fitness function to calculate the fitness
        # of the Chromosome
        self.fitness = self.calcFitness()
    
    # Less than overrider, used when sorting the list
    def __lt__(self, other):
        otherFitness = other.getFitness()
        return otherFitness < self.getFitness()
    
    # Str overrider, used when printing out Chromosomes
    def __str__(self):
        return str(self.genes)
    
    def printChromosome(self):
        print("Weight: " + str(self.weight) + "\t")
        print ("Priority: " + str(self.priority) + "\t")
        print ("Fitness: " + str(self.fitness) + "\t")
        print(str(self.genes))

    # Getter for the priority attribute, returning the priority
    # of the given Chromosome
    def getPriority(self):
        return self.priority
    
    # Getter for the weight attribute, returning the weight
    # of the given Chromosome
    def getWeight(self):
        return self.weight
    
    # Getter for the genes of the Chromosome, returning the binary
    # representation of which objects each backpack is carrying (genes)
    def getGenes(self):
        return self.genes
        
    # Getter for the fitness attribute, returning the fitness of the
    # given Chromosome
    def getFitness(self):
        return (self.fitness)
        
    # Calculates the fitness such that the maximum possible fitness value
    # is 20, where the weight capacity has not been exceeded and the
    # priority value is as high as possible given this. Afterwards,
    # the priority decreases rapidly as the bag gets overweight
    def calcFitness(self):
        if (self.weight <= 120):
            return (self.priority)
        else:
            return ((self.priority - (self.weight / 10)))
    
    # Mutation function that calculates a mutation factor and then,
    # if that randomly generated mutation factor is 1 (thus a 1/MUTATION FACTOR
    # probability), it randomly mutates one gene in the Chromosome by calling
    # the flipGene function on a randomly generated index (gene)
    def mutation(self):
        mutationFactor = random.randint(0,MUTATION_FACTOR)
        if (mutationFactor == 1):
            self.flipGene(random.randint(0,6))
            self.fitness = self.calcFitness()
    
    # flipGene takes in an index and flips the
    # value at that index in the genes list to be the
    # inverse of that value. For example, if there is
    # a 1 at genes[index], flipGene will replace it with
    # a 0, and vice versa if it was a 0
    def flipGene(self, index):
        if (self.genes[index] == 1):
            self.genes[index] = 0
            self.weight -= GLOBAL_WEIGHT[index]
            self.priority -= GLOBAL_PRIORITY[index]
        else:
            self.genes[index] = 1
            self.weight += GLOBAL_WEIGHT[index]
            self.priority += GLOBAL_PRIORITY[index]

    # Performms the crossover necessary for two parents
    # to reproduce. This function takes in two genes (lists)
    # g1 and g2 and an index at which the crossover will occur
    # and return a new list with all values from g1 up to the
    # inserted index and all values from g2 from that index
    # to the end of the list
    def crossover(g1, g2, index):
        c = []
        for i in range(len(g1)):
            if (i < index):
                c.append(g1[i])
            else:
                c.append(g2[i])
        return c
                
        
        
    # Takes in two parent chromosomes and returns their
    # two children resulting from crossover at a randomly
    # generated index
    def reproduce(p1, p2):
        
        g1 = p1.getGenes()
        g2 = p2.getGenes()
        
        index = random.randint(0,7)
        
        c1 = Chromosome(Chromosome.crossover(g1, g2, index))
        c2 = Chromosome(Chromosome.crossover(g2, g1, index))
        
        return ([c1, c2])
