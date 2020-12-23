import part_2
import copy
import json

test_cases = [{
    'input': '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)''',
    'expected_parsed_foods': [
        part_2.Food(ingredients={'mxmxvkd', 'kfcds', 'sqjhc', 'nhms'}, allergens={'dairy', 'fish'}),
        part_2.Food(ingredients={'trh', 'fvjkl', 'sbzzf','mxmxvkd'}, allergens={'dairy'}),
        part_2.Food(ingredients={'sqjhc', 'fvjkl'}, allergens={'soy'}),
        part_2.Food(ingredients={'sqjhc', 'mxmxvkd', 'sbzzf'}, allergens={'fish'}),
    ],
    'expected_flattened': part_2.Food(
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
    'expected_result': 'mxmxvkd,sqjhc,fvjkl'
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    foods = part_2.parse_input(test_case['input'])
    assert_equals(foods, test_case['expected_parsed_foods'])

    # Test flatten_all_ingredients_and_allergens()
    flattened = part_2.flatten_all_ingredients_and_allergens(foods)
    assert_equals(flattened, test_case['expected_flattened'])

    common_ingredients_per_alergen = part_2.find_common_ingredients_per_allergen(foods)
    assert_equals(common_ingredients_per_alergen, test_case['expected_common_ingredients_per_alergen'])
    part_2.reduce_common_ingredients_per_allergen(common_ingredients_per_alergen)
    assert_equals(common_ingredients_per_alergen, test_case['expected_reduced_common_ingredients_per_alergen'])
    result = part_2.to_sorted_ingredient_list(common_ingredients_per_alergen)
    assert_equals(result, test_case['expected_result'])

    result = part_2.compute_result(foods)
    assert_equals(result, test_case['expected_result'])

print("")
print("[[[ SUCCESS ]]]")
print("")
