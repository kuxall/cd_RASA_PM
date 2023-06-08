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


class ActionExtractAccountDetails(Action):
    def name(self) -> Text:
        return "action_extract_account_details"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        account_number = tracker.get_slot("account_number")

        account_details = {
            "00000000009876543210": {
                "name": "Ram Prasad",
                "balance": 5000
            },
            "00000098980987650909": {
                "name": "Balen Shah",
                "balance": 10000
            }
        }

        if account_number in account_details:
            account = account_details[account_number]
            account_name = account["name"]
            account_balance = account["balance"]

            dispatcher.utter_message(text="I have extracted your account details.")
            dispatcher.utter_message(text=f"Account Holder: {account_name}")
            dispatcher.utter_message(text=f"Account Balance: ${account_balance}")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find your account details.")

        return []


class ActionStoreAccountDetails(Action):
    def name(self) -> Text:
        return "action_store_account_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        account_balance = 500

        dispatcher.utter_message(text="Sure! Let me check your account balance.")
        dispatcher.utter_message(text=f"Your current account balance is ${account_balance}.")
        return []


class ActionTransactionHistory(Action):
    def name(self) -> Text:
        return "action_transaction_history"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        account_number = tracker.get_slot("account_number")
        name = tracker.get_slot("name")

        # Replace this with your logic to check the account balance
        account_balance = check_account_balance(account_number, name)  # Implement this function

        if account_balance is not None:
            message = f"Dear {name}, your account {account_number} has a balance of Rs. {account_balance}."
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Account not found.")

        return []
