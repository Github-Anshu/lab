import plotly.express as px

def create_map():
    df = px.data.gapminder().query("year == 2007")
    fig = px.scatter_geo(df, locations="iso_alpha",
                         size="pop", hover_name="country", size_max=60)
    fig.show()

# Run the map plot
create_map()
