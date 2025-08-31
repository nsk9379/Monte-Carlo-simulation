import random

# (a) Probability of rolling a Yahtzee (all 5 dice same)
def estimate_yahtzee(num_trials=100000):
    count = 0
    for _ in range(num_trials):
        dice = [random.randint(1, 6) for _ in range(5)]
        if len(set(dice)) == 1:
            count += 1
    return count / num_trials
