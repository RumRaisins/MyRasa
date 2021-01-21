# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

from third.weather import get_text_weather_date, text_date_to_number_date

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class WeatherForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "weather_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["date_time", "city"]

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        city = tracker.get_slot('city')
        date_time = tracker.get_slot('date_time')
        date_time_number = text_date_to_number_date(date_time)
        print("1111")
        if isinstance(date_time_number, str):
            dispatcher.utter_message("暂不支持查询 {} 的天气".format([city, date_time]))
        else:
            weather = get_text_weather_date(city, date_time, date_time_number)
            print(weather)
            dispatcher.utter_message(text=weather, image=r"https://i0.hdslb.com/bfs/album/6160f9ad45afa002cc05fa063145ebb5b28cb93c.jpg")
        return []

