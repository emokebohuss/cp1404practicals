"""
CP1404 Prac 8
By Emoke Bohuss
Dynamic Labels
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Main program - Kivy app for dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            # add the button to the "id" layout widget
            temp_label.color = (1, 0, 1, 1)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetsApp().run()