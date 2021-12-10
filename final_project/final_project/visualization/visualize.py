import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def covid_time_series(df):
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")

