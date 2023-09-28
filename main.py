from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class LayoutAssignment(BoxLayout,GridLayout):
    pass


class GridLayoutExample(GridLayout):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for letter in "abcdefghijklmnopqrstuvwxyz0123456789":
            b = Button(text="Button "+letter, size_hint=(0.16666666666,0.16666666666))
            self.add_widget(b)
class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class WidgetLayoutApp(App):
    pass

WidgetLayoutApp().run()