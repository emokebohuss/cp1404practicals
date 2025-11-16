"""
CP1404 Prac 8
By Emoke Bohuss
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


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
        return self.root
