import numpy as np
import scipy.stats as st
from pprint import pprint

def confidence_interval_pop(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), st.sem(a)
    h = se * st.t.ppf((1 + confidence) / 2., n-1)

    return float(h)

