
from kivymd.app import MDApp

from uix.screens.baseclass.callscreen import CallScreen


class AIassistent(MDApp):
    def build(self):
        return CallScreen()


AIassistent().run()