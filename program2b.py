import matplotlib.pyplot as plt

def pie_chart():
    labels = 'A', 'B', 'C', 'D'
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('ANSHU GUPTA 1BI21CS020 Pie Chart Example')
    plt.show()

# Run the pie chart plot
pie_chart()
