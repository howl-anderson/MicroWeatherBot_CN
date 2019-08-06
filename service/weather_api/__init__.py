from service.weather_api.seniverse import SeniverseWeatherAPI
from service.weather_api.yahoo import YahooWeatherAPI


weather_class_registry = {}


def registry_weather_class(provider, class_):
    weather_class_registry[provider] = class_


def get_weather_class(provider):
    return weather_class_registry[provider]


def get_weather_api(provider='seniverse', *args, **kwargs):
    weather_api_class = get_weather_class(provider)
    weather_api = weather_api_class(*args, **kwargs)

    return weather_api


registry_weather_class('seniverse', SeniverseWeatherAPI)
registry_weather_class('yahoo', YahooWeatherAPI)
