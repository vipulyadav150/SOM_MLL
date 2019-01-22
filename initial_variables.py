from fetch_training_data import *
import random
def initialize_variables(patterns):
    MAX_CLUSTERS = 200
    VEC_LEN = len(random.choice(patterns))
    INPUT_PATTERNS = len(patterns)
    INPUT_TESTS = 202
    MIN_ALPHA = 0.0011
    MAX_ITERATIONS = 10
    SIGMA = 1
    INITIAL_LEARNING_RATE = 0.5
    INITIAL_RADIUS = 0.5
    print(len(patterns))
    return (
            MAX_CLUSTERS,
            VEC_LEN,
            INPUT_PATTERNS,
            INPUT_TESTS,
            MIN_ALPHA,
            MAX_ITERATIONS,
            SIGMA,
            INITIAL_LEARNING_RATE,
            INITIAL_RADIUS
            )
