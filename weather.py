import requests
import click

def current_weather(location, api_key='e340cbe5ff69cf83bb8571e479c053d5'):
    url = 'http://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)
    print(response.json()['weather'][0]['description'])
    return response.json()['weather'][0]['description']

@click.command()
@click.argument('location')
def ok(location):
    weather = current_weather(location)
    print("The weather in {} right now: {}.".format(location,weather))
SAMPLE_API_KEY = 'e340cbe5ff69cf83bb8571e479c053d5'

