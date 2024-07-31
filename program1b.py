import matplotlib.pyplot as plt
import numpy as np

# Scatter Plot
def scatter_plot():
    # Sample data for scatter plot
    x = np.random.rand(50)
    y = np.random.rand(50)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', alpha=0.5)
    plt.title('Anshu Kumar Gupta 1BI21CS020 Scatter Plot Example')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(True)
    plt.show()

# Bubble Plot
def bubble_plot():
    # Sample data for bubble plot
    x = np.random.rand(50)
    y = np.random.rand(50)
    sizes = np.random.rand(50) * 1000  # Bubble sizes
    colors = np.random.rand(50)  # Bubble colors

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')
    plt.title('Anshu Kumar Gupta 1BI21CS020 Bubble Plot Example')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.colorbar(label='Color Scale')
    plt.grid(True)
    plt.show()

# Run the plots
scatter_plot()
bubble_plot()
