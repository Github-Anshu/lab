import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def customize_seaborn_plots():
    sns.set(style="whitegrid")
    data = np.random.randn(100)
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=True, color='skyblue')
    
    sns.despine(left=True)
    plt.title('ANSHU GUPTA 1BI21CS020 Seaborn Plot with Custom Aesthetics')
    plt.show()

# Run the seaborn plot customization
customize_seaborn_plots()
