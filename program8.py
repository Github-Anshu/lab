import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def correlogram_heatmap():
    data = np.random.rand(10, 12)
    corr = np.corrcoef(data)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('ANSHU GUPTA 1BI21CS020 Correlogram and Heatmap Example')
    plt.show()

# Run the correlogram and heatmap plot
correlogram_heatmap()
