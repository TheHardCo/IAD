import matplotlib.pyplot as plt


def vizualize(df, column):

    if column == "Temperature":
        d = df["Temperature"]
        plt.bar(d.index, d)
        plt.title("Temperature")
        plt.xlabel("Data")
        plt.ylabel("Temperature")
        plt.legend()
        plt.show()

        # plt.plot(df.index, df["Temperature"])
        # plt.title("Temperature")
        # plt.ylabel("Temperature")
        # plt.xlabel('Data')
        # plt.legend()
        # plt.show()

    elif column == "Humidity":
        x = list(df.index.values)
        y = list(df['Humidity'])
        df['Humidity'].plot.area()
        plt.ylabel('Humidity')
        plt.xticks(rotation=90)
        plt.legend()
        plt.show()

    elif column == "Wind Speed":
        d = df["Wind Speed"]
        plt.bar(d.index, d)
        plt.title("Wind Speed")
        plt.xlabel("Data")
        plt.ylabel("Wind Speed")
        plt.legend()
        plt.show()

    elif column == "Pressure":
        x = list(df.index.values)
        y = list(df["Pressure"])
        df["Pressure"].plot.line()
        plt.ylabel("Pressure")
        plt.xticks(rotation=90)
        plt.legend()
        plt.show()
