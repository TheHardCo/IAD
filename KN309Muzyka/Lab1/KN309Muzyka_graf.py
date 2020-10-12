import chart_studio.plotly as py
from plotly.offline import iplot
import cufflinks
import plotly.io as pio
import matplotlib.pyplot as plt
import pandas as pd

pio.renderers.default = 'notebook'
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='pearl', offline=True)


def grafics(DataFrame):

    df0 = DataFrame[["Temperature"]].resample("M").mean()
    df0.iplot(
        kind='bar',
        xTitle='Month',
        yTitle='Average Temperature, °F',
        title='Month Average Temperature')

    df = DataFrame.reset_index()
    df0 = df.groupby(pd.Grouper(key="Date", sort=True)).mean()
    df0[["Humidity", "Dew Point"]].iplot(
        y="Humidity",
        mode='lines+markers',
        secondary_y="Dew Point",
        secondary_y_title='Dew Point',
        xTitle='Date',
        yTitle='Humidity',
        title='Humidity & Dew Point')

    d = DataFrame["Wind Speed"]
    plt.bar(d.index, d)
    plt.title("Wind Speed")
    plt.xlabel("Data")
    plt.ylabel("Wind Speed")
    plt.show()
