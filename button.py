import os

from kivy.app import App
from kivy.uix.button import Button

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class ButtonApp(App):

    def build(self):
        button = Button(text="click here",
                        pos = (50, 50), # 50 pix on the x & y axis
                        size_hint = (.8, .6)) # sizing relative to screen size
        return button
    
if __name__ == "__main__":
    ButtonApp().run()