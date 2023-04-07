import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 543286418 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n=len(x)
    k1=(alpha)**(1/n)
    loc = x.max()-0.083
    return 0.083+loc/1 , \
           0.083 + loc/k1
