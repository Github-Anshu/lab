import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C']
subcategories = ['Subcategory 1', 'Subcategory 2', 'Subcategory 3']
values = [
    [5, 3, 4],  # Values for Subcategory 1
    [6, 2, 5],  # Values for Subcategory 2
    [4, 7, 2]   # Values for Subcategory 3
]

# Stacked Bar Plot
fig, ax = plt.subplots()

# Convert values to numpy array for easier manipulation
values = np.array(values)

# Plot each subcategory
for i in range(len(subcategories)):
    if i == 0:
        ax.bar(categories, values[i], label=subcategories[i])
    else:
        ax.bar(categories, values[i], bottom=np.sum(values[:i], axis=0), label=subcategories[i])

# Adding labels and title
ax.set_ylabel('Values')
ax.set_title('Anshu Gupta 1BI21CS020 Stacked Bar Plot')
ax.legend()

# Display the plot
plt.show()
