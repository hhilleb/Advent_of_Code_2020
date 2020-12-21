def read_input():
    foods = []
    all_ingredients = set()
    all_allergens = set()
    with open("inputs/aoc_input_21.txt") as f:
        for line in f:
            ingredients, allergens = line.rstrip().split(" (contains ")
            allergens = allergens[:-1]
            
            foods.append([ingredients.split(" "), allergens.split(", ")])
            all_ingredients = all_ingredients.union(set(foods[-1][0]))
            all_allergens = all_allergens.union(set(foods[-1][1]))
    return foods, all_ingredients, all_allergens

def find_safe_ingredients(foods, all_ingredients, all_allergens):
    allergen_candidates = {}
    safe_ingredients = list()
    for ingredient in all_ingredients:
        potential_allergens = all_allergens.copy()
        for allergen in all_allergens:
            for food in foods:
                if allergen in food[1] and ingredient not in food[0]:
                    # ingredient can't have allergen
                    potential_allergens.remove(allergen)
                    break
        if potential_allergens == set():
            # ingredient can't have a single allergen
            safe_ingredients.append(ingredient)
        allergen_candidates[ingredient] = potential_allergens
    return safe_ingredients, allergen_candidates

def count_ingredients(foods, ingredients):
    count = 0
    for food in foods:
        for ingredient in ingredients:
            count += food[0].count(ingredient)
    return count


def get_matching(safe_ingredients, allergen_candidates):
    for ingredient in safe_ingredients:
        del allergen_candidates[ingredient]
    matching = {}

    while allergen_candidates:
        for ingredient, possible_allergens in allergen_candidates.items():
            if len(possible_allergens) == 1:
                break
        allergen = possible_allergens.pop()
        matching[ingredient] = allergen
        del allergen_candidates[ingredient]

        for ingredient, possible_allergens in allergen_candidates.items():
            if allergen in possible_allergens:
                possible_allergens.remove(allergen)

    return matching


foods, all_ingredients, all_allergens = read_input()
safe_ingredients, allergen_candidates = find_safe_ingredients(foods, all_ingredients, all_allergens)
print("Part 1: " + str(count_ingredients(foods, safe_ingredients)))

matching = get_matching(safe_ingredients, allergen_candidates)
result = list(matching.items())
result.sort(key=lambda x: x[1])
print("Part 2: " + ",".join([i[0] for i in result]))