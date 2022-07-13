import random
from functools import partial
from itertools import permutations

ARRAY_SIZE = 6


def d6():
    return random.randint(1, 6)


def roll_4d6kh3():
    return sum(sorted((d6() for _ in range(4)))[1:])


def roll_2d6p5():
    return d6() + d6() + 5


def roll_bounded(roll_fn, lower, upper):
    return min(upper, max(lower, roll_fn()))


def random_replace(total_min, total_max, roll):
    array = sorted((roll() for _ in range(ARRAY_SIZE)))
    total = sum(array)
    while not (total_min <= total <= total_max):
        print(f"Generated: {array}, total: {total}")
        idx = random.randint(0, len(array) - 1)
        if total_min > total:
            print(f"Too low, replacing: {array[idx]}")
        else:
            print(f"Too high, replacing: {array[idx]}")
        array[idx] = roll()

        array = sorted(array)
        total = sum(array)

    print(f"Final array: {array}, total: {total}")
    return array


def random_move(ability_min, ability_max, total, roll):
    array = [roll() for _ in range(ARRAY_SIZE - 1)]
    array.append(total - sum(array))
    while True:
        array = sorted(array)
        shortage = ability_min - array[0]
        surplus = array[-1] - ability_max
        if shortage <= 0 and surplus <= 0:
            break

        if surplus > 0:
            array[-1] -= surplus
            array[0] += surplus
            continue

        if shortage > 0:
            array[0] += shortage
            array[-1] -= shortage
            continue

    print(f"Final array: {array}, total: {total}")
    return array


def random_choice(ability_min, ability_max, total):
    valid_scores = tuple(range(ability_min, ability_max + 1))
    valid_arrays = tuple(
        p for p in permutations(valid_scores, 6)
        if sum(p) == total
    )
    array = sorted(random.choice(valid_arrays))
    print(f"Final array: {array}")
    return array


if __name__ == "__main__":
    array = random_replace(73, 73, partial(roll_bounded, roll_4d6kh3, 7, 16))
    permutations_ = tuple(permutations(array, 6))
    for _ in range(5):
        print(random.choice(permutations_))
