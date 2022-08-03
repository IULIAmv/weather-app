from create_file import create_csv
from weather import get_forecast_weather

columns, rows = get_forecast_weather("sibiu", False)

create_csv("data.csv", "write", columns, rows)
