import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import push_notebook

# Matplotlib Annotations
def matplotlib_annotations():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('ANSHU GUPTA 1BI21CS020 Matplotlib Annotations Example')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.annotate('Max', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.grid(True)
    plt.show()

# Bokeh Line Graph with Legends
import numpy as np
from bokeh.plotting import figure, output_notebook, show

# Ensure the notebook output is enabled
output_notebook()

def bokeh_line_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    y2 = np.cos(x)

    p = figure(title='ANSHU GUPTA 1BI21CS020 Bokeh Line Graph with Legends', x_axis_label='X Axis', y_axis_label='Y Axis')
    p.line(x, y, legend_label='Sin(x)', line_width=2)
    p.line(x, y2, legend_label='Cos(x)', line_color='red', line_width=2)
    
    show(p, notebook_handle=True)

# Call the function to display the plot
bokeh_line_graph()
