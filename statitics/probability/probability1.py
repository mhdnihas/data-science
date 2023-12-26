# import numpy as np
# import matplotlib.pyplot as plt
# rolls=np.random.randint(1,7,200)
# print(rolls)

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 5, 10]

# Create a line plot
plt.plot(x, y, label='Linear Function')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Add a legend
plt.legend()

# Display the plot
plt.show()