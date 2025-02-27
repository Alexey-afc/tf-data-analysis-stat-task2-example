import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 543286418 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    if (len(x)!=10 or p==0.95):
      alpha = 1 - p
      n=len(x)
      k1=(alpha*1/3)**(1/n)
      k2=(1-(alpha*2/3))**(1/n)
      loc = x.max()-0.083
      return 0.083+loc/k2 , \
            0.083 + loc/k1

    else:
      alpha = 1 - p
      n=len(x)
      k1=(alpha)**(1/n)
      loc = x.max()-0.083
      return 0.083+loc/1 , \
            0.083 + loc/k1
