from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.messagebus.message import Message
import time

logger = getLogger(__name__)

class Mindexpression(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        super(Mindexpression, self).__init__(name="Mindexpression")

    def initialize(self):
        # Set up the Mind Expression listener
        self.add_event('mind-expression-skill:command', self.handle_command)

    def handle_command(self, message):
        # Get the command from the Mind Expression message
        command = message.data.get('command')

        if command == 'wake_up':
            # Send the wake up command to Mycroft
            self.bus.emit(Message('mycroft.awoken'))

        elif command == 'go_to_sleep':
            # Send the go to sleep command to Mycroft
            self.bus.emit(Message('mycroft.stop'))

        elif command == 'set_volume':
            # Get the volume value from the Mind Expression message
            volume = message.data.get('volume')
            # Set the Mycroft volume to the specified value
            self.bus.emit(Message('mycroft.volume.set', {"percent": volume}))

        elif command == 'play_music':
            # Get the music to play from the Mind Expression message
            music = message.data.get('music')
            # Play the specified music using Mycroft's audio service
            self.bus.emit(Message('mycroft.audio.service.play', {"tracks": [{"uri": music}]}))

        elif command == 'stop_music':
            # Stop the music currently playing
            self.bus.emit(Message('mycroft.audio.service.stop'))

        else:
            logger.warning("Received unknown command from Mind Expression: {}".format(command))

    def stop(self):
        # Clean up the Mind Expression listener
        self.remove_event('mind-expression-skill:command')


def create_skill():
    return Mindexpression()