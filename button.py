import os

from kivy.app import App
from kivy.uix.button import Button

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class ButtonApp(App):

    def build(self):
        button = Button(text="click here")
        return button
    
if __name__ == "__main__":
    ButtonApp().run()