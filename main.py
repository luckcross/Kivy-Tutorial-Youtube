from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class Container(BoxLayout):
    text_input = ObjectProperty()
    label_widget = ObjectProperty()

    def change_label_text(self):
        self.label_widget.text = self.text_input.text

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()