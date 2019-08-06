from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from service.action import get_text_weather_date
from service.normalization import text_to_date
from service.weather_api import get_weather_api


# class WeatherForm(FormAction):
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#
#         return ["address", "date-time"]
#
#     def name(self) -> Text:
#         return "action_report_weather"
#
#     def submit(self,
#                dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         address = tracker.get_slot('address')
#         date_time = tracker.get_slot('date-time')
#
#         date_time_number = text_date_to_number_date(date_time)
#
#         if isinstance(date_time_number, str):  # parse date_time failed
#             msg = "暂不支持查询 {} 的天气".format([address, date_time_number])
#             return [SlotSet("matches", msg)]
#             # print(msg)
#             # dispatcher.utter_message(msg)
#         else:
#             weather_data = get_text_weather_date(address, date_time,
#                                                  date_time_number)
#             return [SlotSet("matches", "{}".format(weather_data))]
#             # print(weather_data)
#             # dispatcher.utter_message(weather_data)
#
#         # utter submit template
#         # dispatcher.utter_template('utter_submit', tracker)
#         # return []


class ActionReportWeather(Action):
    def __init__(self):
        self.weather_api = get_weather_api('seniverse')

    def name(self) -> Text:
        return "action_report_weather"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        address = tracker.get_slot('address')
        date_time = tracker.get_slot('date-time')

        date_object = text_to_date(date_time)

        if not date_object:  # parse date_time failed
            msg = "暂不支持查询 {} 的天气".format([address, date_time])
            return [SlotSet("matches", msg)]
            # print(msg)
            # dispatcher.utter_message(msg)
        else:
            try:
                weather_data = self.weather_api.get_text_by_city_and_day(address, date_object)
            except Exception as e:
                weather_data = str(e)

            return [SlotSet("matches", "{}".format(weather_data))]
            # print(weather_data)
            # dispatcher.utter_message(weather_data)

        # utter submit template
        # dispatcher.utter_template('utter_submit', tracker)
        # return []
