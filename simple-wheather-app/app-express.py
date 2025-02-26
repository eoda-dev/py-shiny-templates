import datetime

import pandas as pd
import plotly.graph_objects as go
import requests
from shiny import reactive, render, ui
from shiny.express import input
from shinywidgets import render_widget

ui.panel_title("Weather App")
ui.input_numeric("lat", "Latitude", value=51.3167)
ui.input_numeric("lon", "Longitude", value=9.5)


@reactive.Calc
def weather_dat():
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=temperature_2m,rain&past_days=3"
        % (input.lat(), input.lon())
    )
    response = requests.get(url)
    data = response.json()["hourly"]
    df = pd.DataFrame(data)
    return df


@render_widget
def plot():
    df = weather_dat()
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["time"], y=df["temperature_2m"], mode="lines", name="Temperature"
        )
    )
    fig.add_trace(go.Bar(x=df["time"], y=df["rain"], name="Rain", yaxis="y2"))
    fig.add_vline(x=datetime.datetime.today())
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        yaxis2=dict(title="Rain (mm)", overlaying="y", side="right"),
        showlegend=False,
    )
    return fig


@render.table(index=True)
def table():
    df = weather_dat()
    df["time"] = pd.to_datetime(df["time"])
    df.set_index("time", inplace=True)
    daily_summary = df.resample("D").agg(
        {"temperature_2m": ["min", "max"], "rain": "sum"}
    )
    daily_summary = daily_summary.T
    daily_summary.index = ["min. T (°C)", "max. T (°C)", "Rain (mm)"]
    daily_summary.columns = [col.strftime("%d.%m") for col in daily_summary.columns]
    return daily_summary
