from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
import numpy as np

# real pwm from etseq code
pwm_p90 = np.array([
    [0.8473,0.9985,1.1451,1.0116,0.6419,0.5465,0.7376,0.6506,1.9924,
     1.0986,0.0000,0.0606,0.3483,0.0000,0.8473,0.9985,1.1451,1.0116,
     0.6419,0.5465,0.7376,0.6506,1.9924,1.0986],  # A
    [0.2719, 0.0000, 0.2007, 0.6061, 0.3054, 0.2364, 0.8329, 0.4274,
     0.3830, 0.0000, 0.1178, 0.0000, 0.0000, 0.1335, 0.2719, 0.0000,
     0.2007, 0.6061, 0.3054, 0.2364, 0.8329, 0.4274, 0.3830, 0.0000],  # T
    [0.3365, 0.0541, 0.0000, 0.1466, 0.0541, 0.1719, 0.3023, 0.7376,
     0.0465, 0.5390, 0.1178, 0.3483, 0.0606, 0.0645, 0.3365, 0.0541,
     0.0000, 0.1466, 0.0541, 0.1719, 0.3023, 0.7376, 0.0465, 0.5390],  # G
    [0.0000, 0.1112, 0.4520, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
     0.0000, 0.4700, 0.4925, 0.0606, 0.0606, 0.0000, 0.0000, 0.1112,
     0.4520, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.4700] # C
    ])

pwm_n10 = np.array([
    [0.20, 0.30, 0.10, 0.40, 0.50, 0.20, 0.25],  # A
    [0.40, 0.35, 0.20, 0.25, 0.20, 0.30, 0.15],  # T
    [0.15, 0.20, 0.30, 0.20, 0.10, 0.25, 0.30],  # G
    [0.25, 0.15, 0.40, 0.15, 0.20, 0.25, 0.30]   # C
])

pwm_diff = np.array([

])

def pwm_score(pwm, seq):
    """Compute PWM score for a sequence, truncating to PWM length."""
    score = 0
    pwm_length = pwm.shape[1]

    # Ensure sequence isn't longer than PWM length
    seq = seq[-pwm_length:]  # Use only the last `pwm_length` bases

    for i, base in enumerate(seq):
        if base == 'A':
            score += pwm[0][i]
        elif base == 'T':
            score += pwm[1][i]
        elif base == 'G':
            score += pwm[2][i]
        elif base == 'C':
            score += pwm[3][i]
    return score

def analyze_sequence(seq):
    """Validates the sequence format, extracts the start region, and computes PWM scores."""
    # Expected format:
    # (10-15 bp start) + (4 bp random) + (GACTC) + (T) + (10-15 bp same as start)

    # Find GACTC motif (cut site)
    motif_pos = seq.find("GACTC")
    if motif_pos == -1 or motif_pos + 6 > len(seq) or seq[motif_pos + 5] != 'T':
        return "Error: GACTCT motif not found in the correct position."

    # Extract different parts of the sequence
    random_region = seq[motif_pos - 4:motif_pos]  # 4bp random
    start_region = seq[:motif_pos - 4]  # 10-15bp before 4bp random region
    cut_site = seq[motif_pos:motif_pos + 5]  # Should be "GACTC"
    single_t = seq[motif_pos + 5]  # Single "T"

    # The end region should match the start region and be the same length
    end_start = motif_pos + 6
    end_region = seq[end_start:end_start + len(start_region)]

    # Validate sequence parts
    if len(start_region) < 10 or len(start_region) > 15:
        return "Error: Start region length incorrect."
    if cut_site != "GACTC":
        return "Error: Incorrect cut site."
    if single_t != "T":
        return "Error: T base is missing."
    if start_region != end_region:
        return "Error: Start and end regions do not match."

    # Compute scores for start region
    p90_score = pwm_score(pwm_p90, start_region)
    n10_score = pwm_score(pwm_n10, start_region)
    difference = p90_score - n10_score

    # Compute melting temperature (Tm)
    start_seq = Seq(start_region)  # Convert start_region to a Seq object
    tm_value = mt.Tm_NN(start_seq, Na=1000, Mg=0, dnac1=50, saltcorr=7)
    #tm_value = mt.Tm_NN(start_seq, Na=21, Mg=3, dnac1=50, saltcorr=7)

    return (f"Valid sequence! Start: {start_region}, Random: {random_region}, Cut Site: {cut_site}, End: {end_region},"
            f" P90: {p90_score}, N10: {n10_score}, Difference: {difference}, Tm: {tm_value:.2f} deg C")

# Example sequence
sequences = [
    "CCTACGACTGAACAGACTCTCCTACGACTG",  # Should be valid
    "CCTACGACTTAACAGACTCTCCTACGACTT",
    "CCTACGACGGAACAGACTCTCCTACGACGG",
    "CCTACGAGTGAACAGACTCTCCTACGAGTG"
]

for seq in sequences:
    print(analyze_sequence(seq))

