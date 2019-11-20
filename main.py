from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

# from kivy.core.window import Window
# Window.size = (800, 600)

class Container(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()   