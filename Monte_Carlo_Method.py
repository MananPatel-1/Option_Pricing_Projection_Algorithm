import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

r = 0.06
sigma = 0.3
T = 1.0
S0 = 100

I = 100000
M = 100

dt = T / M

S = np.zeros((M + 1, I))
S[0] = S0
for t in range(1, M + 1):
    S[t] = S[t - 1] * np.exp(
        (r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * npr.standard_normal(I)
    )
# Binomial Distribution
# plt.figure(figsize=(10, 8))
# plt.hist(S[-1], bins=100)
# plt.xlabel("S(T)")
# plt.ylabel("frequency")
# plt.show()


def BS_Call_MC(S, X, r, sigma, T, t, I):
    data = np.zeros((I, 2))
    z = np.random.normal(0, 1, [1, I])
    ST = S * np.exp((T - t) * (r - 0.5 * sigma ** 2) + sigma * np.sqrt(T - t) * z)
    data[:, 1] = ST - X
    average = np.sum(np.amax(data, axis=1)) / float(I)
    return np.exp(-r * (T - t)) * average


print("Monte Carlo:", BS_Call_MC(100, 95, 0.06, 0.3, 1, 0.999, 100000))
