from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('kivy', 'keyboard_game', 'systemanddock')

from kivymd.theming import ThemeManager

# from kivy.core.window import Window
# Window.size = (800, 600)

def get_weight(m):
    nitro = str(10 * m / 1000)
    salt = str(15* m / 1000)
    starts = str(0.5 * m / 1000)
    monosugars = str(5 * m / 1000)
    salting_time = str(round(m / 500 * 2))
    return {'nitro': nitro, 'salt': salt, 'starts': starts, 'monosugars': monosugars, 'salting_time': salting_time}

class Container(BoxLayout):
    text_input = ObjectProperty(None)
    salt = ObjectProperty(None)
    nitro = ObjectProperty(None)
    monosugars = ObjectProperty(None)
    starts = ObjectProperty(None)
    time = ObjectProperty(None)

    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingr = get_weight(mass)

        self.salt.text = ingr.get('salt')
        self.nitro.text = ingr.get('nitro')
        self.monosugars.text = ingr.get('monosugars')
        self.starts.text = ingr.get('starts')
        self.time.text = ingr.get('salting_time')

class MyApp(App):
    theme_cls = ThemeManager()
    title = 'The Coppa Calc'

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()

if __name__ == '__main__':
    MyApp().run()   