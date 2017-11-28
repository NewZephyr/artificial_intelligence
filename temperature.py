import numpy as np
from matplotlib import use
use("TkAgg")
import consts
from matplotlib import pyplot as plt



X = np.array([400, 900, 390, 1000, 550])
sorted_x = np.sort(X)[:consts.Consts.STOCH_TOP_SCORES_TO_CONSIDER]
best_n = list(map(lambda x: x if x in sorted_x else 0, X))


# def p(x, t):
#     return (0 if x == 0 else np.power(x, -1 / t) / (np.sum(np.power(sorted_x, -1 / t))))
def p(x, t):
    if x == 0:
        return 0
    else:
        return np.power(x, -1 / t) / (np.sum(np.power(sorted_x, -1 / t)))

plt.xlabel("T")
plt.ylabel("P")
plt.title("Probability as a function of the temperature")
t = np.arange(0, 5, 0.05)
y = np.array(best_n)
plt.plot(t,y)

plt.show()




# def p(t,X):
#     sorted_x = np.sort(X)[:consts.Consts.STOCH_TOP_SCORES_TO_CONSIDER]
#     best_n = list(map(lambda x: x if x in sorted_x else 0, X))
#     result = []
#     for i in best_n:
#         result += [0] if i == 0 else [np.power(i, -1 / t) / (np.sum(np.power(sorted_x, -1 / t)))]
#     return result
