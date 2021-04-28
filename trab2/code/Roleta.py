import random


### Roleta ###

# Rodar a roleta
def roulette_run (rounds, roulette):
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

def roulette_construction(states):
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