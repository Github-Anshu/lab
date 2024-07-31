import matplotlib.pyplot as plt
import numpy as np

# Histogram Plot
def histogram_plot():
    data = np.random.randn(1000)
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title('ANSHU GUPTA 1BI21CS020 Histogram Plot Example')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Box Plot
def box_plot():
    data = [np.random.randn(100) for _ in range(4)]
    plt.figure(figsize=(10, 6))
    plt.boxplot(data)
    plt.title('ANSHU GUPTA 1BI21CS020 Box Plot Example')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

# Run the plots
histogram_plot()
box_plot()
