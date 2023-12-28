import numpy as np
import matplotlib.pyplot as plt
rolls=np.random.randint(1,7,20)
print(rolls)
empirical_prob=[np.sum(rolls==i)/20 for i in range(1,7)]
print(empirical_prob)

outcome_counts = np.bincount(rolls)[1:]
probabilities = outcome_counts /len(rolls)

labels = [str(i) for i in range(1, 7)]
x = np.arange(len(labels))

plt.bar(x, probabilities, tick_label=labels)
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title('Probability Distribution of a Fair Six-sided Die')
plt.show()