import random

# (a) Probability of rolling a Yahtzee (all 5 dices same)
def estimate_yahtzee(num_trials=100000):
    count = 0
    for _ in range(num_trials):
        dice = [random.randint(1, 6) for _ in range(5)]
        if len(set(dice)) == 1:                              # Bug
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

# (c) Average longest run of heads/tails in 200 flips
def estimate_longest_run(num_trials=10000, flips=200):
    def longest_run(seq):
        max_run = run = 1
        for i in range(1, len(seq)):
            if seq[i] == seq[i-1]:
                run += 1
                max_run = max(max_run, run)
            else:
                run = 1
        return max_run
    
    total = 0
    for _ in range(num_trials):
        sequence = [random.choice(['H','T']) for _ in range(flips)]
        total += longest_run(sequence)
    return total / num_trials

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


# (e) Average flips before string s appears
def estimate_flips_for_string(s="HHTTH", num_trials=5000):
    length = len(s)
    total = 0
    for _ in range(num_trials):
        flips = ""
        count = 0
        while True:
            flips += random.choice(['H','T'])
            count += 1
            if flips.endswith(s):
                break
        total += count
    return total / num_trials


if __name__ == "__main__":
    print("Estimated Probability of Yahtzee:", estimate_yahtzee())
    print("Estimated Probability of Large Straight:", estimate_large_straight())
    print("Average Longest Run (200 flips):", estimate_longest_run())
    print("Average Flips before 5 Heads:", estimate_flips_for_5_heads())
    print("Average Flips before HHTTH:", estimate_flips_for_string("HHTTH"))
