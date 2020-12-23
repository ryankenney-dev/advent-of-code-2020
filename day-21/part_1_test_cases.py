import part_1
import copy
import json

test_cases = [{
    'input': '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)''',
    'expected_parsed_foods': [
        part_1.Food(ingredients={'mxmxvkd', 'kfcds', 'sqjhc', 'nhms'}, allergens={'dairy', 'fish'}),
        part_1.Food(ingredients={'trh', 'fvjkl', 'sbzzf','mxmxvkd'}, allergens={'dairy'}),
        part_1.Food(ingredients={'sqjhc', 'fvjkl'}, allergens={'soy'}),
        part_1.Food(ingredients={'sqjhc', 'mxmxvkd', 'sbzzf'}, allergens={'fish'}),
    ],
    'expected_flattened': part_1.Food(
        ingredients={'mxmxvkd', 'kfcds', 'sqjhc', 'nhms', \
            'trh', 'fvjkl', 'sbzzf', \
            'sqjhc', 'fvjkl', \
            'sqjhc', 'mxmxvkd', 'sbzzf'},
        allergens={'dairy', 'fish', \
            'dairy', \
            'soy', \
            'fish'},
    ),
    'expected_common_ingredients_per_alergen': {
        'dairy': {'mxmxvkd'},
        'fish': {'sqjhc', 'mxmxvkd'},
        'soy': {'fvjkl', 'sqjhc'},
    },
    'expected_reduced_common_ingredients_per_alergen': {
        'dairy': {'mxmxvkd'},
        'fish': {'sqjhc'},
        'soy': {'fvjkl'},
    },
    'expected_known_allergen_ingredients': {'mxmxvkd', 'sqjhc', 'fvjkl'},
    'expected_non_allergen_ingredients': {'kfcds', 'nhms', 'sbzzf', 'trh'},
    'expected_count': 5
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    foods = part_1.parse_input(test_case['input'])
    assert_equals(foods, test_case['expected_parsed_foods'])

    # Test flatten_all_ingredients_and_allergens()
    flattened = part_1.flatten_all_ingredients_and_allergens(foods)
    assert_equals(flattened, test_case['expected_flattened'])

    common_ingredients_per_alergen = part_1.find_common_ingredients_per_allergen(foods)
    assert_equals(common_ingredients_per_alergen, test_case['expected_common_ingredients_per_alergen'])
    part_1.reduce_common_ingredients_per_allergen(common_ingredients_per_alergen)
    assert_equals(common_ingredients_per_alergen, test_case['expected_reduced_common_ingredients_per_alergen'])
    known_allergen_ingredients = part_1.common_ingredients_per_allergen_to_known_allergen_ingredients(common_ingredients_per_alergen)
    assert_equals(known_allergen_ingredients, test_case['expected_known_allergen_ingredients'])
    non_allergen_ingredients = part_1.to_non_allergen_ingredients(foods, known_allergen_ingredients)
    assert_equals(non_allergen_ingredients, test_case['expected_non_allergen_ingredients'])
    count = part_1.count_occurences_of_ingredients(foods, non_allergen_ingredients)
    assert_equals(count, test_case['expected_count'])

    count = part_1.compute_result(foods)
    assert_equals(count, test_case['expected_count'])

print("")
print("[[[ SUCCESS ]]]")
print("")
