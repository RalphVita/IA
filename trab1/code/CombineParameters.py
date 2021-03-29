#Hiperparâmetros

#Simulated Annealing 
pararansSA = []
for t in [500, 100, 50]:
    for alfa in [0.95, 0.85, 0.7]:
        for iter_max in [350, 500]:
            pararansSA.append({
                't': t, 
                'alfa': alfa,
                'iter_max': iter_max,
                'max_time': 1
            })

#Genetic Algorithm
pararansGe = []
for pop_size in [10, 30, 50]:
    for cross_ratio in [0.75, 0.85, 0.95]:
        for mut_ratio in [0.10, 0.20]:
            pararansGe.append({
                'pop_size': pop_size, 
                'cross_ratio': cross_ratio,
                'mut_ratio': mut_ratio,
                'max_time': 1
            })

#Grasp
pararansGr = []
for numIter in [20, 50, 100, 200, 350, 500]:
    for numBest in [5, 10, 15]:
        pararansGr.append({
            'numIter': numIter, 
            'numBest': numBest,
            'max_time': 1
        })

