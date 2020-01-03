import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


num_trials = 1000000

true_average = np.random.beta(81, 219, num_trials)
hits = np.random.binomial(300, true_average, num_trials)

simulation = pd.DataFrame(data={"true_average": true_average, "hits":hits})

#plt.figure()
#plt.hist(true_average)
#plt.show()

