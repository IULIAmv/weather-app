from _ast import Lambda
from tkinter import font
import requests
import tkinter as tk
from create_file import create_csv

HEIGHT = 900
WIDTH = 800



def format_response(weather):
    """
    :goal: Format the API response.
    :param weather: The API response.
    :type weather: dict
    :return: The message to be shown to the user.
    :rtype: str
    """
    city_name = weather['data'][0]['city_name']
    weather_description = weather['data'][0]['weather']['description']
    country_code = weather['data'][0]['country_code']
    date_time = weather['data'][0]['datetime']
    temperature = weather['data'][0]['temp']

    final_str = f'City: {city_name}\nWeather description: {weather_description}\nCountry code: {country_code}\nDate & time: {date_time}\nTemperature: {temperature}°C\n'
    return final_str


def format_response_forecast(forecast_weather, string=True):
    """
    :goal: Format the API response.
    :param forecast_weather: The API response.
    :type forecast_weather: dict
    :return: The message to be shown to the user.
    :rtype: str
    """
    city_name = forecast_weather['city_name']
    date_time_1 = forecast_weather['data'][0]['datetime']
    max_temp_1 = forecast_weather['data'][0]['max_temp']
    min_temp_1 = forecast_weather['data'][0]['min_temp']
    date_time_2 = forecast_weather['data'][1]['datetime']
    max_temp_2 = forecast_weather['data'][1]['max_temp']
    min_temp_2 = forecast_weather['data'][1]['min_temp']
    date_time_3 = forecast_weather['data'][2]['datetime']
    max_temp_3 = forecast_weather['data'][2]['max_temp']
    min_temp_3 = forecast_weather['data'][2]['min_temp']
    date_time_4 = forecast_weather['data'][3]['datetime']
    max_temp_4 = forecast_weather['data'][3]['max_temp']
    min_temp_4 = forecast_weather['data'][3]['min_temp']
    date_time_5 = forecast_weather['data'][4]['datetime']
    max_temp_5 = forecast_weather['data'][4]['max_temp']
    min_temp_5 = forecast_weather['data'][4]['min_temp']

    columns = ["city", "date", "max_temp", "min_temp"]
    rows = [[city_name, date_time_1, max_temp_1, min_temp_1],[city_name, date_time_2, max_temp_2, min_temp_2],
            [city_name, date_time_3, max_temp_3, min_temp_3],[city_name, date_time_4, max_temp_4, min_temp_4],
            [city_name, date_time_5, max_temp_5, min_temp_5]]
    create_csv("data.csv", "write", columns, rows)

    final_forecast = f"""Forecast for: {city_name}\n
    Date & time: {date_time_1}\nMax.Temperature: {max_temp_1}°C\nMin.Temperature: {min_temp_1}°C
    Date & time: {date_time_2}\nMax.Temperature: {max_temp_2}°C\nMin.Temperature: {min_temp_2}°C
    Date & time: {date_time_3}\nMax.Temperature: {max_temp_3}°C\nMin.Temperature: {min_temp_3}°C
    Date & time: {date_time_4}\nMax.Temperature: {max_temp_4}°C\nMin.Temperature: {min_temp_4}°C
    Date & time: {date_time_5}\nMax.Temperature: {max_temp_5}°C\nMin.Temperature: {min_temp_5}°C"""
    return final_forecast




def get_weather(city):
    """"
    :goal: Gets data from API.
    :param city: The city name entered by the user.
    :type city: str
    :return: None
    """

    api_key = '56fd90d02b8b4cd7b259df1be1513826'
    url = 'https://api.weatherbit.io/v2.0/current'
    params = {'key': api_key, 'city': city}
    response = requests.get(url, params=params)
    try:
        weather = response.json()
    except requests.exceptions.JSONDecodeError:
        label['text'] = f'{city} city not found.'
        return

    label['text'] = format_response(weather)


def get_forecast_weather(city, string=True):
    """"
     :goal: Gets data from API.
     :param city: The city name entered by the user.
     :type city: str
     :return: None
     """

    api_key_forecast = '56fd90d02b8b4cd7b259df1be1513826'
    url_forecast = 'https://api.weatherbit.io/v2.0/forecast/daily'
    params_forecast = {'key': api_key_forecast, 'city': city}
    response = requests.get(url_forecast, params=params_forecast)
    try:
        forecast_weather = response.json()
    except requests.exceptions.JSONDecodeError:
        label['text'] = f'{city} city not found.'
        return

    if string:
        label['text'] = format_response_forecast(forecast_weather)
        return

    columns, rows = format_response_forecast(forecast_weather, string)
    return columns, rows


if __name__ == '__main__':

    #define a pop up window
    root = tk.Tk()
    root.title('About Weather')
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='light blue', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    #define textfield to get city name from the user
    entry_1 = tk.Entry(frame, font=('Courier', 18))
    entry_1.place(relwidth=0.65, relheight=1)


    #define buttons for the user to access data
    button = tk.Button(frame, text='Find weather', font=('Courier', 12), bg='grey', fg='light blue', command=lambda: get_weather(entry_1.get()))
    button.place(relx=0.7, relwidth=0.25,  relheight=1, anchor='ne')

    button_2 = tk.Button(frame, text='Find 5 days forecast', font=('Courier', 8), bg='grey', fg='light blue', command=lambda: get_forecast_weather(entry_1.get()))
    button_2.place(relx=0.7, relwidth=0.25,  relheight=1, anchor='nw')

    #define label in which to display data for the user
    lower_frame = tk.Frame(root, bg='light blue', bd=5)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4, bg='light blue')
    label.place(relwidth=1, relheight=1)

    root.mainloop()
































