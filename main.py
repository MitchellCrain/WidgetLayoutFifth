from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation="lr-tb"
    b=Button(text="A", size_hint=(.5,.5))


class StackLayoutExample(StackLayout):
    pass
class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class WidgetLayoutApp(App):
    pass

WidgetLayoutApp().run()