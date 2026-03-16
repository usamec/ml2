# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
def generate_regular_sequence(length, gap_length_mean=np.log(40), gap_length_std=0.3,
                           gap_var=3, prob_fn=0.03, prob_fp=0.003):
    pulse_sequence = np.random.uniform(0, 1, size=length) < prob_fp
    gap_length = max(16, min(100, np.random.lognormal(gap_length_mean, gap_length_std)))

    cur_pos = np.random.uniform(0, gap_length * 0.9)
    while cur_pos < length:
        cur_pos_int = np.round(cur_pos).astype(int)
        if cur_pos_int < length:
            if np.random.uniform() > prob_fn:
                pulse_sequence[cur_pos_int] = 1
        cur_pos += gap_length + np.random.uniform(-gap_var, gap_var)
    return pulse_sequence

def generate_irregular_sequence(length, gap_length_mean=np.log(40), gap_length_std=0.3, prob_fn=0.03, prob_fp=0.003):
    pulse_sequence = np.random.uniform(0, 1, size=length) < prob_fp
    gap_length = max(16, min(100, np.random.lognormal(gap_length_mean, gap_length_std)))

    cur_pos = np.random.uniform(0, gap_length * 0.9)
    while cur_pos < length:
        cur_pos_int = np.round(cur_pos).astype(int)
        if cur_pos_int < length and np.random.uniform() > prob_fn:
            pulse_sequence[cur_pos_int] = 1
        gap_length = max(16, min(100, np.random.lognormal(gap_length_mean, gap_length_std)))
        cur_pos += gap_length
    return pulse_sequence
# %%
plt.plot(generate_regular_sequence(1000))
plt.plot(generate_irregular_sequence(1000))
# %%
