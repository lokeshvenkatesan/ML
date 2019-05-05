
# coding: utf-8

# In[1]:


import random
import string
import numpy as np

# calculate fitness
fitness = []
def calc_fitness():
    for word in elements:
        fitness_temp = 0
        for i in range(len(final_word)):
            if final_word[i] == word[i]:
                fitness_temp += 1
        fitness.append(fitness_temp)

# normalize scores
normalized_fitness = []
def norm_fitness():
    total_score = 0
    for score in fitness:
        total_score += score
    for score in fitness:
        normalized_fitness.append(score / total_score)

def get_fittest():
    largest_val = 0
    for i in fitness:
        if i > largest_val: largest_val = i
    return fitness.index(largest_val)
# generate elements
final_word = input("enter word to be evolved to: ")
elements = []
for i in range(500):
    elements.append(''.join(random.choice(string.ascii_lowercase + string.digits + " ") for _ in range(len(final_word))))
generation = 0
for loop in range(250):
    generation += 1
    fitness = []
    normalized_fitness = []
    calc_fitness()
    norm_fitness()
    print("Generation "+ str(generation) + " : " + elements[get_fittest()])
    # reproduction
    parents = np.random.choice(elements, 1000, p=normalized_fitness)
    elements = []
    #reproduction
    for i in range(0, len(parents) - 1 , 2):
        rand = random.randint(0, len(final_word))
        child = parents[i][:rand] + parents[i + 1][rand:]
        #mutation
        for letter_pos in range(len(child)):
            if random.randint(0, 100) < 2:
                list_child = list(child)
                list_child[letter_pos] = ''.join(random.choice(string.ascii_lowercase + string.digits + " ") for _ in range(1))
                child = "".join(list_child)
        elements.append(child)

