import random

# Configuration
NUM_QUEENS = 4
POP_COUNT = 7
MAX_ITERATIONS = 1200

def make_chromosome():
    
    return [random.randint(0, NUM_QUEENS-1) for _ in range(NUM_QUEENS)]

def compute_score(chromo):
    
    score = 0
    
    for row1 in range(NUM_QUEENS):
        for row2 in range(row1 + 1, NUM_QUEENS):
           
            col_conflict = chromo[row1] == chromo[row2]
            diag_conflict = abs(chromo[row1] - chromo[row2]) == abs(row1 - row2)
            if not col_conflict and not diag_conflict:
                score += 1
    return score

def pick_parent(population, scores):
   
    
    ranked = sorted(zip(scores, population), reverse=True)
    ranks = list(range(1, len(population) + 1))
    
    
    total_rank = sum(ranks)
    pick = random.uniform(0, total_rank)
    current = 0
    
    for i, (score, chromo) in enumerate(ranked):
        current += (len(population) - i)  
        if current >= pick:
            return chromo
    return ranked[0][1]  

def combine_parents(p1, p2):
   
    if len(p1) <= 2:
        return p1[:]  
    
    pt1 = random.randint(1, len(p1)//2)
    pt2 = random.randint(len(p1)//2 + 1, len(p1)-1)
    
    
    child = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
    return child

def apply_variation(chromo, current_gen):
    
    mutation_prob = 0.35 * (1 - current_gen/MAX_ITERATIONS)
    
    if random.random() < mutation_prob:
        pos = random.randint(0, len(chromo)-1)
        chromo[pos] = random.randint(0, NUM_QUEENS-1)
    
    return chromo

def run_genetic_algorithm():
    
    print("🔬 N-Queens Genetic Algorithm")
    print(f"Queens: {NUM_QUEENS}, Population: {POP_COUNT}")
    print("-" * 40)
    

    current_pop = [make_chromosome() for _ in range(POP_COUNT)]
    
    best_overall = None
    best_score_overall = -1
    solution_gen = -1
    
    for generation in range(MAX_ITERATIONS):
        
        fitness_values = [compute_score(ind) for ind in current_pop]
        
        
        current_best_idx = fitness_values.index(max(fitness_values))
        current_best = current_pop[current_best_idx]
        current_best_fit = fitness_values[current_best_idx]
        
       
        if current_best_fit > best_score_overall:
            best_score_overall = current_best_fit
            best_overall = current_best[:]
            solution_gen = generation
        
        
        if generation % 150 == 0:
            print(f"Gen {generation:4d}: Best fit = {current_best_fit}")
        
        
        perfect_score = NUM_QUEENS * (NUM_QUEENS - 1) // 2
        if current_best_fit == perfect_score:
            print(f"\nPerfect solution at generation {generation}!")
            print(f"Chromosome: {current_best}")
            best_overall = current_best
            solution_gen = generation
            break
        
       
        new_generation = []
        
        
        sorted_pop = [x for _, x in sorted(zip(fitness_values, current_pop), reverse=True)]
        new_generation.extend(sorted_pop[:3])
        
        
        while len(new_generation) < POP_COUNT:
            parent_a = pick_parent(current_pop, fitness_values)
            parent_b = pick_parent(current_pop, fitness_values)
            
            
            while parent_a == parent_b and len(current_pop) > 1:
                parent_b = pick_parent(current_pop, fitness_values)
            
            offspring = combine_parents(parent_a, parent_b)
            offspring = apply_variation(offspring, generation)
            new_generation.append(offspring)
        
        current_pop = new_generation
    
    
    print("\n" + "=" * 40)
    if best_score_overall == NUM_QUEENS * (NUM_QUEENS - 1) // 2:
        print(f"SUCCESS in {solution_gen} generations!")
        print(f"Solution: {best_overall}")
    else:
        print(f"Best attempt after {MAX_ITERATIONS} generations:")
        print(f"Chromosome: {best_overall}")
        print(f"Fitness: {best_score_overall}/{NUM_QUEENS*(NUM_QUEENS-1)//2}")
    print("=" * 40)


if __name__ == "__main__":
    run_genetic_algorithm()
