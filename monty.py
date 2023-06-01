import numpy as np
import random
def monty_hall(switch):
    door_1 = 'goat'
    door_2 = 'goat'
    door_3 = 'car'
    l = [door_1, door_2, door_3]
    my_choice = random.choice(l)
    if my_choice != door_1:
        reveal = door_1
    else:
        reveal = door_2
    if switch:
        l.remove(reveal)
        l.remove(my_choice)
        return l[0]
    else:
        return my_choice
def run_experiment(ntrials, switch):
    a = []
    for i in range(ntrials):
        a.append(monty_hall(switch))
    return a.count('car')/len(a)


p=run_experiment(10000, switch = False)
print(f'Probability of winning the car: {p}')


p=run_experiment(10000, switch = True)
print(f'Probability of winning the car: {p}')

