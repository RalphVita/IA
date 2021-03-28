import random
import time
import math
from Training import Trainable

class Mutable:
    def Value(self):
        pass
    def GerarVizinho(self):
        pass
    #Compara dois estados
    def Equal(self, other):
        pass
    def Crossover(self, other):
        pass
    def Mutation(self):
        pass

class Genetic(Trainable):
    def __init__(self, state : Mutable,pop_size = 10, cross_ratio = 0.75, mut_ratio = 0.1, max_time = 1, elite_pct = 0.2):
        Trainable.__init__(self, 'Genético')
        self.state = state 
        self.pop_size = pop_size 
        self.cross_ratio = cross_ratio
        self.mut_ratio = mut_ratio
        self.max_time = max_time
        self.elite_pct = elite_pct
        self.solution : Mutable = None


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
        print(cont)
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
            individual = self.state.GerarVizinho()
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
        aux_population = self.roulette_construction(population)
        new_population = self.roulette_run(n, aux_population)
        return new_population

    ### Roleta ###

    # Rodar a roleta
    def roulette_run (self,rounds, roulette):
        if roulette == []:
            return []
        selected = []
        #print(rounds, roulette)
        while len(selected) < rounds:
            r = random.uniform(0,1)
            for state in roulette:
                if r <= state[0]:
                    selected.append(state[1])
                    break
        return selected

    def roulette_construction(self, states):
        aux_states = []
        roulette = []
        #Valores de todos estados
        values = [s.Value() for s in states]
        total_values = sum(values)
        total_values = total_values if total_values != 0 else 1

        #Inverte a porcentagem, dando prioridade aos menores e soma o total
        total_invert = sum(1-values/total_values)

        for state in states:
            value = state.Value()
            if total_invert != 0:
                ratio = (1-value/total_values)/total_invert
            else:
                ratio = 1
            aux_states.append((ratio,state))
    
        acc_value = 0
        for state in aux_states:
            acc_value = acc_value + state[0]
            s = (acc_value,state[1])
            roulette.append(s)
        return roulette

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