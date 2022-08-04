import csv
import plotly.express as px
import pandas as pd


def create_csv(file_name, mode, columns, rows):
    if mode == "write":
        m = "w"
    elif mode == "read":
        m = "r"
    else:
        print("Wrong mode")
        return

    with open(file_name, m, newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        for row in rows:
            writer.writerow(row)

    print("The file successfully created")


def create_plot(file_name):
    df = pd.read_csv(file_name)
    fig = px.bar(df, x="date", y=["min_temp", "max_temp"])
    fig.write_image("plot.png")

create_plot("data.csv")
