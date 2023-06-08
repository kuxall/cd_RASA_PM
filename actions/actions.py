# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        account_number = tracker.get_slot("account_number")

        # Simulating database lookup
        database = {
            "Ram Prasad": {
                "account_number": "00000000001234567890",
                "balance": 1000
            }
        }

        if name in database and account_number == database[name]["account_number"]:
            balance = database[name]["balance"]
            response = f"Dear {name}, your account {account_number} has a balance of Rs. {balance}."
        else:
            response = "Sorry, we couldn't find your account information."

        dispatcher.utter_message(text=response)

        return []
