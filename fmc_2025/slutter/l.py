import random

# Original flag characters
original_flag = list('o1me0T3}h_hTuvar_M4vdCFF3__{l3TY')

flags = list()
# Function to brute-force the seed
def brute_force_seed(start_time, end_time):
    for seed in range(start_time, end_time + 1):
        random.seed(seed)
        shuffled_flag = original_flag.copy()
        random.shuffle(shuffled_flag)
        shuffled_flag = ''.join(shuffled_flag)
        if shuffled_flag[:6] == "FMCTF{}" and shuffled_flag[-1] == '}' :
            print(f"Seed: {seed}, Flag: {shuffled_flag}")
            flags.append(shuffled_flag)

# Estimate the time range when the script was executed
# Replace these with the approximate time range (in Unix timestamp format)
start_time = 100000000  # Example: Replace with the lower bound of the time range
end_time = 1742077713    # Example: Replace with the upper bound of the time range

# Run the brute-force
brute_force_seed(start_time, end_time)
print(flags)