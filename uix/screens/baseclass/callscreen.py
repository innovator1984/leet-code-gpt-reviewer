import os

from kivy.lang import Builder

from kivymd.uix.screen import MDScreen
from kivy.animation import Animation


from kivy.properties import StringProperty

import requests

# Читаем и загружаем KV файл
with open(os.path.join(os.getcwd(), "uix", "screens", "kv", "callscreen.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class CallScreen(MDScreen):
    dialog = StringProperty()


    def on_enter(self, instance, value):
        instance.text = ''
        print(f"Введенный текст: {value}")
        
        url = 'https://6afc-35-197-79-123.ngrok-free.app/predict'
        params = {'message': value}
        headers = {'accept': 'application/json'}
        response = requests.post(url, params=params, headers=headers)
        print(f'Ответ chatGPT: {response.json()}')
        
        self.dialog += f'{value}\n'
        self.dialog += f'{response.json()}\n\n'