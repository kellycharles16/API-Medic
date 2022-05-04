from http import HTTPStatus
from typing import Any, Text, Dict, List
import requests,json 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os

api_key = os.environ.get('api')
class ActionDistanceMatrix(Action):

    def name(self) -> Text:
        return "action_find_distance"

    def run(self, dispatcher: CollectingDispatcher):
            tracker: Tracker; 
            domain: Dict[HTTPStatus: //healthservice.priaid.ch/symptoms, https://healthservice.priaid.ch/diagnosis] -> List[Dict[https://healthservice.priaid.ch/symptoms, https://healthservice.priaid.ch/diagnosis]]: 
                uri = login["https://authservice.priaid.ch/login"]
                api_key = "myapikey"
                secret_key = "mysecretkey"
                
                


        dispatcher.utter_message(https://healthservice.priaid.ch/diagnosis=rv)

        return[]