import numpy as np
from matplotlib import use
use("TkAgg")
import consts
from matplotlib import pyplot as plt

X = np.array([400, 900, 390, 1000, 550])
sorted_x = np.sort(X)[:consts.Consts.STOCH_TOP_SCORES_TO_CONSIDER]


def p(x_i, t):
    return 0 if x_i == 0 else (x_i**(-1 / t) / (np.sum(np.power(sorted_x, -1 / t))))

plt.title("Probability as a function of the temperature")
plt.xlabel("T")
plt.ylabel("P")
plt.grid(True)
ax = plt.subplot(111)
for x in X:
    p_list = [p(x, t) for t in np.arange(0.01, 5, 0.05)]
    ax.plot(np.arange(0.01, 5, 0.05), p_list, label=x)
ax.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()
