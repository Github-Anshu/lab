import matplotlib.pyplot as plt
import numpy as np

def linear_plot():
    x = np.linspace(0, 10, 100)
    y = 2 * x + 1

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('ANSHU GUPTA 1BI21CS020 Linear Plot Example')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(True)
    plt.show()

# Run the linear plot
linear_plot()
