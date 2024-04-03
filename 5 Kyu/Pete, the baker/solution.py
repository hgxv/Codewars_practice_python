import math

def cakes(recipe, available):
    result = []
    for item in recipe.keys():
        try:
            result.append(math.floor(available[item] / recipe[item]))
        except KeyError:
            return 0
    print(result)
    return min(result)