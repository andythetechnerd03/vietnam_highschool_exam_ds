import plotly.express as px
import geopandas as gpd
import pandas as pd
from typing import Tuple

def plot_choropleth(map_file: str, english_data_by_province: pd.Series) -> Tuple[gpd.GeoDataFrame, px.choropleth]:
    """ Plot a choropleth map of Vietnam with data from english_data_by_province

    Args:
        map_file (str): Path to the map file (GeoJSON)
        english_data_by_province (pd.Series): Data to plot on the map

    Returns:
        Tuple[gpd.GeoDataFrame, px.choropleth]: Tuple of GeoDataFrame and Plotly choropleth map
    """
    gdf = gpd.read_file(map_file)
    gdf_merged = gdf.merge(english_data_by_province, left_on="Name", right_index=True)

    fig = px.choropleth(gdf_merged, geojson=gdf_merged.geometry,
                        locations=gdf_merged.index, color="language",
                        hover_name="Name", width=1200, height=900)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # fig.write_image("vietnam_language_score.png")
    fig.show()
    return gdf_merged, fig

def save_plot_to_chart_studio(fig, chart_name: str, api_key: str, username: str) -> None:
    """ Save a plotly figure to Chart Studio

    Args:
        fig (): Plotly chart
        chart_name (str): chart name
        api_key (str): API Key
        username (str): Username
    """
    import chart_studio
    import chart_studio.plotly as py
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    py.plot(fig, filename = chart_name, auto_open=True)
    