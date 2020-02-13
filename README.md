The problem is a genetic algorithm that finds the best combination
of boxes without exceeding the maximum weight.

First we start with a random population by choosing a sub-combination
of the seven boxes. This is represented as ones and zeros. For example,
if we have a combination consisting of boxes 1, 3, and 4, then it would
be represented as [1, 0, 1, 1, 0, 0, 0].

Next, we apply a fitness function that recognizes the fittest individuals,
by giving value to boxes with higher importance and lower weight. We keep
50% of the boxes that have a high value of a fitness function, and then
cull the less "fit" boxes by removing them. We then apply a successor 
operation to reproduce the "fit" boxes, and add the children to the population. 
Every so often, we mutate the child with a small probability. We then check to 
see if the fittest child (best combination of boxes) satisfies the solution.
After repeating these steps enough times, the best combination of boxes can 
be found.



Genome for Problem

The genome for this problem consists of a list of binary numbers (0s and 1s)
that represent which objects are in a knapsack in that particular instance. Thus,
each Chromosome object has an attribute genes that stores a list of length 7 holding
binary values that represent which objects are included in that configuration. For
example, if we create an object:

    new = Chromosome([0, 1, 1, 0, 0, 0, 0])
    
this instance's genome is the configuration of 1s and 0s in the list that makes up
the configuration of the Chromosome. This binary representation of the genome represents,
in this instance of a knapsack configuration, that this knapsack is carrying
object 2 and object 3, since there is a 1 at index 2 and 3 (assuming that indices are
shifted up 1 so index 0 doesn't exist). In this way, we can use the binary representation
to store each individual possible knapsack configuration in a genome, and use lists
storing each object's (index) weight and priority value to calculate each 
instance's weight and priority value from this genome. 



Fringe Operations

The first fringe operation is a mutation fringe. With a small probability,
the child will be mutated by having a single gene flipped. For example, if a 
child randomly mutates, our mutation formula will randomly select an index in the
genome where the binary value will be flipped (for example if a 1 is currently there, signifying
that that object is included in the knapsack configuration, it is flipped to a 0,
thus taking the object out of the configuration). 

The second fringe operatoon is a crossover fringe. This is in the
reproductive step of the process. In this fringe function, a random number n
is generated between 1 and 7. Then, two children are created using a crossover
of the two parents' genome. Child 1 has genes 1 to n of parent 1's genes, and
genes n + 1 to 7 of parent 2's genes. Child 2 has the inverse: genes 1 to n of
parent 2's genes and n + 1 to 7 of parent 1's genes. The purposes of this
fringe function is to create two children that have two combinations of
two of the "fitter" Chromosomes in the parent population.



File Specifications

Files:
README
chromosome.py
population.py
main.py

chromosome.py:
This file contains the Chromosome class,  which stores the genome of
each Chromosome instance, as well as the weight and priority value of
each instance. The Chromosome class contains several different function
definitions, the most of which are getter functions and comparison overloaders,
but there are some key functions that perform key functions of the
genetic algorithm that we will go into detail below. I will also provide detail
on four global constants defined at the top of the class that are used
for different key functions as part of the genetic algorithm:

    1. GLOBAL CONSTANTS
        
        a. GLOBAL_WEIGHT: provides the weight value for each
        possible object in the knapsack (genome). For example, in
        the genes [1,0,0,0,0,0,0], we know that the resulting
        knapsack includes object 1, which corresponds to index 0
        in the GLOBAL_WEIGHT list and thus we can find its weight
        at that index (20)
        
        b. GLOBAL_PRIORITY: provides the priority value for each
        possible object in the knapsack (genome). For example, in
        the genes [1,0,0,0,0,0,0], we know that the resulting
        knapsack includes object 1, which corresponds to index 0
        in the GLOBAL_PRIORITY list and thus we can find its priority
        at that index (6)
        
        c. MUTATION_FACTOR: provides the factor that defines how
        likely a mutation is on each child produced. For example,
        if MUTATION_FACTOR is 10000, which it is currently set to
        each mutation occurs at a probability of 1/100000. 


    1. __lt__(self, other), __str__(self): comparison and print
    overloaders that allow Chromosome objects to be compared based
    on their priority and print the genome of the chromosome
    respectively.
    
    2. printChromosome(self): prints out the key attributes of the
    Chromosome when called on a Chromosome object as well as the
    genome
    
    3. getPriority(self), getWeight(self), getGenes(self), getFitness(self):
    are all getter functions that return the respective attribute
    of the Chromosome object
    
    4. calcFitness(self): defines the fitness function that calculates
    the fitness of a Chromosome object based on the weight and priority
    values of the genome. Until the bag is overweight, the priority value
    of the genome is the most important attribute, but once the bag
    begins to become overweight, an increase in weight causes
    the priority of a Chromosome to decrease.
    
    5. mutation(self): defines the mutation fringe operation where,
    when called on a Chromosome object, will in a 1/MUTATION_FACTOR
    probability flip a gene at a randomly determined location in the
    genome.
    
    6. flipGene(self, index): takes in an index and flips the
    binary value at that index in the genes list.
    
    7. crossover(g1, g2, index): takes in two parent genomes
    and returns a child resulting from the crossover of the two parents 
    and the inputted index. For example, Chromosome.crossover(
    [1,1,1,1,1,1,1],[0,0,0,0,0,0,0], 3] would output [1,1,1,0,0,0,0].
    
    8. reproduce(p1, p2): takes in two parent Chromosomes and
    returns a list containing the two children resulting from the
    two parents being crossed over at a randomly generated index
    in the genome. For example, Chromosome.crossover(Chromosome([1,1,1,1,1,1,1])
    ,Chromosome([0,0,0,0,0,0,0]), 3] would output [Chromosome([1,1,1,0,0,0,0]), 
    Chromosome([0,0,0,1,1,1,1])]

    
While the attributes have been heavily tested and can also largely be tested
through running and testing different scenarios with the algorithm, it is possible to
isolate different functions through creating an instance of a Chromosome object
and then manipulating it using one of the functions, thereby testing their functionality.

population.py:
This file contains the Population class, which stores the size of
the population as well as a list of all Chromosomes that are in the population.
The following provide more details on the available functions within this class
and their role in the algorithm

    1. __init__(self, n): Initializes the Population object by 
    setting the size attribute to the desired size passed in and
    then randomly generates size number of Chromosome genomes,
    inserting the resulting Chromosome objects into its
    population attribute, which stores a list of Chromosomes
    in the current population
    
    2. getSize(self): returns the size attribute of the population
    
    3. printPop(self): iterates through the current population of
    Chromosomes, calling printChromosome() on each one
    
    4. getFittestChromosome(self): returns the Chromosome in the
    population with the highest fitness value, as determined by the
    fitness function in the Chromosome class
    
    5. cull(self): Performs the genetic algorithm, taking in the
    old generation (current population), sorting it, and then culling out 
    the least fittest fifty percent. Then, the function checks 
    to make sure that the resulting population is larger than
    one, and then calling the crossover function between pairs of parents
    from the remaining parents (top 50% of the old generation), calling
    the mutation function on each child (which mutates that child 
    1/MUTATION_FACTOR times), and then inserting the resulting child (mutated
    or not) into a list holding the new generation. If there are an 
    even number of parents, this process ends when all parents have 
    produced offspring. If there are an odd number of parents, a child
    is created with the same genome as that parent and the mutation
    function is called on that child before being added to the new
    generation list. Finally, the size attribute of the population is
    updated to reflect the culling and the population attribute is updated
    to be equal to the new generation list. If the resulting population
    has size 1, it can no longer be culled and the function returns true, 
    reflecting that the algorithm has reached the fittest individual within
    its scope. Otherwise, it returns false, reflecting that further culling
    can be done.
    
    
While the attributes have been heavily tested and can also largely be tested
through running and testing different scenarios with the algorithm, it is possible to
isolate different functions through creating an instance of a Population object
and then manipulating it using one of the functions, thereby testing their functionality.

main.py
This file contains both main() and one other function that handles
the running of the genetic algorithm. Details of these both and their
specifications are below

    1. run(populationSize): takes in an integer and creates a new
    Population instance of that size. It then culls that population by
    calling the Population.cull() function until it returns true,
    representing that the population cannot be culled anymore.
    Once it has finished, run then returns the fittest individual,
    representing the fittest possible solution to the knapsack solution
    that the algorithm has been able to find given its scope
    
    2. main(): Takes in the desired size of the population from
    the user, validating it and then calling the run function,
    passing this desired size. Once run finishes, it takes the
    fittest individual and outputs its specifications using the
    printChromosome() function before finishing.
    
In terms of testing the functions in this file, the best way to 
test run is to create populations of large sizes and make sure that
the algorithm will find an strong solution within the weight limit
and at or near the maximal possible priority value within the weight
maximum. Note that, given how the genetic algorithm works, if a small
population size is passed in, the optimal solution may have low priority
or exceed the desired weight maximum as the scope provided is too small
for the crossover and mutation fringe operations to provide their 
functionality. In terms of testing main, the user can try to provide invalid
inputs to verify that the program checks for this and will only accept
an integer greater than 0.
