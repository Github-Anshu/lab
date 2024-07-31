import plotly.graph_objs as go
import numpy as np

def plot_3d():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(title='ANSHU GUPTA 1BI21CS020 3D Surface Plot Example', autosize=False, width=700, height=700)
    fig.show()

# Run the 3D plot
plot_3d()
