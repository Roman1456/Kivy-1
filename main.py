from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direktion = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direktion = self.direktion
        self.screen.manager.current = self.goal



class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = 'Це напис ')
        box = BoxLayout()
        box_button = BoxLayout(orientation = 'vertical', paddding = 8 , spacing = 8)
        box_button.add_widget(ScrButton(self, direction= '',goal = '1'))
        box_button.add_widget(ScrButton(self, direction='', goal= '2'))
        box_button.add_widget(ScrButton(self, direction='', goal= '3'))
        box_button.add_widget(ScrButton(self, direction='', goal= '4'))

app = MyApp()
app.run()
