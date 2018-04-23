coin_weights = [1/8, 1/4, 1/2, 1, 1.5, 2, 4, 7]

def find_coins(weight):
    results = []
    for i in range(12):
        for s in itertools.combinations_with_replacement(range(len(coin_weights)), i):
            weight_sum = sum(coin_weights[int(item)] for item in s)
            if weight_sum == weight:
                results.append(s)
    return results
