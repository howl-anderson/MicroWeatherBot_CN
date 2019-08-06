import datetime
import os

from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

from service.weather_api.base import WeatherAPIBase
from service.weather_api.condition import Condition


class YahooWeatherAPI(WeatherAPIBase):
    DEFAULT_APP_ID = os.getenv('YAHOO_APP_ID', '')
    DEFAULT_API_KEY = os.getenv('YAHOO_API_KEY', '')
    DEFAULT_API_SECRET = os.getenv('YAHOO_API_SECRET', '')

    def __init__(self, app_id=None, api_key=None, api_secret=None):
        super(YahooWeatherAPI, self).__init__()

        self.app_id = app_id if app_id else self.DEFAULT_APP_ID
        self.api_key = api_key if api_key else self.DEFAULT_API_KEY
        self.api_secret = api_secret if api_secret else self.DEFAULT_API_SECRET

        self.data = YahooWeather(
            APP_ID=self.app_id,
            api_key=self.api_key,
            api_secret=self.api_secret
        )

    def get_weather_by_city(self, city, *args, **kwargs):
        self.data.get_yahoo_weather_by_city("tehran", Unit.celsius)
        return self._forecasts_to_condition(self.data.forecasts)

    @staticmethod
    def _forecasts_to_condition(forecasts):
        forecast_data = {
            i.date.date(): Condition(i.date.date(), i.text, i.low, i.high)
            for i in forecasts}
        return forecast_data

    def get_weather_by_location(self, lat, long, *args, **kwargs):
        self.data.get_yahoo_weather_by_location(lat, long)
        return self._forecasts_to_condition(self.data.forecasts)

    def forecast_to_text(self, condition: Condition):
        msg_tpl = "Weather of {date}：condition {condition}；tempeture range {temp_low}-{temp_high} degree"
        msg = msg_tpl.format(
            date=condition.date,
            condition=condition.condition,
            temp_low=condition.low_temperature,
            temp_high=condition.high_temperature
        )
        return msg


if __name__ == "__main__":
    APP_ID = 'sJXMrh4i'
    consumer_key = 'dj0yJmk9dkhYUlZnMkJjcWM2JmQ9WVdrOWMwcFlUWEpvTkdrbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWE5'
    consumer_secret = 'd9bb6c4495d902332e235e498595046cb2c33c02'
    yw = YahooWeatherAPI(APP_ID, consumer_key, consumer_secret)
    result = yw.get_text_by_city_and_day('shanghai', datetime.datetime.now().date())
    print(result)
