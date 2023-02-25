import requests
from mycroft import MycroftSkill, intent_handler
from websocket import create_connection
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

logger = getLogger(__name__)


class Mindexpression(MycroftSkill):
    def __init__(self):
        super(Mindexpression, self).__init__(name="Mindexpression")

    @intent_handler('mindexpression.intent')
    def handle_mindai(self, message):
        self.speak_dialog('mindexpression')

    def initialize(self):
        self.add_event('recognizer_loop:utterance',
                       self.send_to_mind_expression)
        self.url = self.settings.get('url')
        self.api_key = self.settings.get('api_key')

    # def send_message(self, message):
    #     headers = {'Authorization': f'Bearer {self.api_key}'}
    #     data = {'message': message}
    #     response = requests.post(self.url, headers=headers, json=data)
    #     if response.status_code == 200:
    #         return response.json().get('response')
    #     else:
    #         logger.warning(
    #             f'Mind Expression request failed with status code {response.status_code}')
    #         return None

    # def handle(self, message):
    #     response = self.send_message(message.data['utterance'])
    #     if response is not None:
    #         self.speak(response)

    # def send_to_mind_expression(self, message):
    #     try:
    #         ws = create_connection("wss://localhost:8181")
    #         utterance = message.data.get('utterance')
    #         message = {
    #             'type': 'speak',
    #             'data': {'utterance': utterance}
    #         }
    #         ws.send(json.dumps(message))
    #         response = ws.recv()
    #         logger.info("Received response from Mind Expression: " + response)
    #         ws.close()
    #         self.bus.emit(Message("speak", {"utterance": response}))
    #     except:
    #         logger.error("Failed to connect to Mind Expression")

    def stop(self):
        pass


def create_skill():
    return Mindexpression()
