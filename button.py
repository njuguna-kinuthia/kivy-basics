import os

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text='Click here'
        self.pos=(100, 100)
        self.size_hint=(.25, .25)

class FunckyLabel(Label):
    def __init__(self, **kwargs):
        super(FunckyLabel, self).__init__(**kwargs)
        self.text='label'
        self.pos=(100, 200)
        self.size_hint(.25, 0.25)


class ButtonApp(App):

    def build(self):
        """
        button = Button(text="click here",
                        pos = (50, 50), # 50 pix on the x & y axis
                        size_hint = (.8, .6)) # sizing relative to screen size
                        """
        return FunkyButton()
    
if __name__ == "__main__":
    ButtonApp().run()