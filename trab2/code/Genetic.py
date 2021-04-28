import random
import time
import math
from Roleta import roulette_construction, roulette_run
from Cluster import Cluster

class IMutable:
    def Crossover(self, other):
        pass
    def Mutation(self):
        pass

class Genetic:
    def __init__(self,k ,pop_size = 10, cross_ratio = 0.75, mut_ratio = 0.2, max_time = 1, elite_pct = 0.05):
        self.k = k
        self.pop_size = pop_size 
        self.cross_ratio = cross_ratio
        self.mut_ratio = mut_ratio
        self.max_time = max_time
        self.elite_pct = elite_pct
        self.solution : IMutable = None

    def fit(self, x_train):
        self.state = Cluster(X = x_train, k = self.k)

        self.Run()

        self.cluster_centers_ = self.solution.centroides

    def Run(self):
        start = time.process_time()
        opt_state = self.state
        opt_value = opt_state.Value()
        population = self.initial_population(self.pop_size)
        conv = self.convergent(population)
        end = 0
        cont = 0
        while not conv and end-start <= self.max_time:
            cont+=1
            
            #val_pop = evaluate_population (pop, items)
            new_pop = self.elitism (population)
            best = new_pop[0]
            val_best = best.Value()

            if (val_best < opt_value):
                opt_state = best
                opt_value = val_best

            selected = self.selection(population, self.pop_size - len(new_pop)) 
            crossed = self.crossover_step(selected)
            mutated = self.mutation_step(crossed)
            population = new_pop + mutated
            conv = self.convergent(population)

            end = time.process_time()
        self.solution = opt_state
        #print(cont, end-start,conv)
        return self.solution

    def convergent(self,population):
        conv = False
        if population != []:
            base = population[0]
            i = 0
            while i < len(population):
                if not base.Equal(population[i]):
                    return False
                i += 1
            return True

    def initial_population(self, n):
        pop = []
        count = 0
        while count < n:
            individual = self.state.NextState()
            pop = pop + [individual]
            count += 1
        return pop

    def elitism (self,population):
        n = math.floor(self.elite_pct*len(population))
        if n < 1:
            n = 1
        elite = sorted (population, key = lambda x: x.Value())[:n]
        return elite

    def selection(self, population,n):
        aux_population = roulette_construction(population)
        new_population = roulette_run(n, aux_population)
        return new_population


    # Etapa de Recombinação
    def crossover_step (self, population):
        new_pop = []
        
        for _ in range (round(len(population)/2)):
            rand = random.uniform(0, 1)
            fst_ind = random.randint(0, len(population) - 1)
            scd_ind = random.randint(0, len(population) - 1)
            parent1 = population[fst_ind] 
            parent2 = population[scd_ind]

            if rand <= self.cross_ratio:
                offspring1, offspring2 = parent1.Crossover(parent2)            
            else:
                offspring1, offspring2 = parent1, parent2
                    
            new_pop = new_pop + [offspring1, offspring2]
            
        return new_pop

    # Etapa de Mutação
    def mutation_step (self, population):
        ind = 0
        for individual in population:
            rand = random.uniform(0, 1)
            if rand <= self.mut_ratio:
                mutated = individual.Mutation()
                population[ind] = mutated           
            ind+=1
            
        return population 