from mycroft import MycroftSkill, intent_file_handler


class Mindexpression(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mindexpression.intent')
    def handle_mindexpression(self, message):
        self.speak_dialog('mindexpression')


def create_skill():
    return Mindexpression()

