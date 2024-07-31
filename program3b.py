import matplotlib.pyplot as plt
import numpy as np

def linear_plot_with_formatting():
    x = np.linspace(0, 10, 100)
    y = 2 * x + 1

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linestyle='--', marker='o', color='r')
    plt.title('ANSHU GUPTA 1BI21CS020 Linear Plot with Line Formatting Example')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(True)
    plt.show()

# Run the formatted linear plot
linear_plot_with_formatting()
