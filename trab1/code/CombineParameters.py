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
pararansG = []
for pop_size in [10, 30, 50]:
    for cross_ratio in [0.75, 0.85, 0.95]:
        for mut_ratio in [0.10, 0.20]:
            pararansG.append({
                'pop_size': pop_size, 
                'cross_ratio': cross_ratio,
                'mut_ratio': mut_ratio,
                'max_time': 1
            })

def get_parans():
    return pararansSA, pararansG