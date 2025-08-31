import random

# (a) Probability of rolling a Yahtzee (all 5 dices same)
def estimate_yahtzee(num_trials=100000):
    count = 0
    for _ in range(num_trials):
        dice = [random.randint(1, 6) for _ in range(5)]
        if len(set(dice)) == 1:
            count += 1
    return count / num_trials

# (b) Probability of rolling a large straight (1-2-3-4-5 or 2-3-4-5-6)
def estimate_large_straight(num_trials=100000):
    straights = [{1,2,3,4,5}, {2,3,4,5,6}]
    count = 0
    for _ in range(num_trials):
        dice = [random.randint(1, 6) for _ in range(5)]
        if set(dice) in straights:
            count += 1
    return count / num_trials

# (d) Average number of flips before 5 heads in a row
def estimate_flips_for_5_heads(num_trials=10000):
    total = 0
    for _ in range(num_trials):
        count = heads = 0
        while heads < 5:
            flip = random.choice(['H','T'])
            count += 1
            if flip == 'H':
                heads += 1
            else:
                heads = 0
        total += count
    return total / num_trials
