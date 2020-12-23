import collections
import re
from functools import reduce

def parse_input(input):
    line_regex = re.compile(r'^([^\(]+)\s\(contains\s([^\)]+)\)$')
    lines = input.splitlines()
    foods = []
    for line in lines:
        match = line_regex.match(line)
        if not match:
            raise Exception('Invalid line: %s' % line)
        foods.append(Food(ingredients=set(match.group(1).split(' ')), allergens=set(match.group(2).split(', '))))
    return foods

def compute_result(foods):
    common_ingredients_per_alergen = find_common_ingredients_per_allergen(foods)
    reduce_common_ingredients_per_allergen(common_ingredients_per_alergen)
    return to_sorted_ingredient_list(common_ingredients_per_alergen)

def flatten_all_ingredients_and_allergens(foods):
    return reduce(lambda f1,f2: Food(f1.ingredients.union(f2.ingredients), f1.allergens.union(f2.allergens)), foods)

def get_foods_with_known_allergen(foods, allergen):
    return list(filter(lambda f: allergen in f.allergens, foods))

Food = collections.namedtuple('Food', ['ingredients', 'allergens'])

def find_common_ingredients_per_allergen(foods):
    flattened_food = flatten_all_ingredients_and_allergens(foods)
    all_allergens = flattened_food.allergens
    all_ingredients = flattened_food.ingredients

    result = {}
    for allergen in all_allergens:
        foods_with_allergen = list(filter(lambda f: allergen in f.allergens, foods))
        ingredients_in_common = reduce(lambda i1, i2: i1.intersection(i2), list(map(lambda f: f.ingredients, foods_with_allergen)))
        result[allergen] = ingredients_in_common
    return result

def reduce_common_ingredients_per_allergen(common_ingredients_per_allergen):
    solved_allergens = set()

    def get_next_allergen_to_solve():
        nonlocal common_ingredients_per_allergen
        nonlocal solved_allergens
        for allergen in common_ingredients_per_allergen.keys():
            if allergen in solved_allergens:
                continue
            if len(common_ingredients_per_allergen[allergen]) > 1:
                continue
            return allergen
        return None

    while True:
        allergen = get_next_allergen_to_solve()
        if allergen == None:
            break
        solved_allergens.add(allergen)
        solved_ingredient = list(common_ingredients_per_allergen[allergen])[0]

        for other_allergen, other_ingredients in common_ingredients_per_allergen.items():
            # Do not remove from the one we just solved
            if other_allergen == allergen:
                continue
            other_ingredients.discard(solved_ingredient)

def to_sorted_ingredient_list(common_ingredients_per_allergen):
    allergen_ingredient_pairs = list()
    for allergen, ingredients in common_ingredients_per_allergen.items():
        if len(ingredients) != 1:
            # Nothing in the problem description guarantees that we will be able
            # to reduce to an answer, but it appears we are able to
            raise Exception('We were unable to completely reducde to an answer')
        allergen_ingredient_pairs.append((allergen, list(ingredients)[0]))


    # print(allergen_ingredient_pairs)
    # x = allergen_ingredient_pairs.sort(key=lambda t: t[0])
    # print(x)
    # x = list(map(lambda t: t[1], x))
    # x = ','.join(x)

    return ','.join(list(map(lambda t: t[1], sorted(allergen_ingredient_pairs, key=lambda t: t[0]))))
