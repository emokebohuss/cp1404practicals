"""
CP1404 Prac 8
By Emoke Bohuss
Convert miles to km app
"""
from kivy.properties import StringProperty

"""
CP1404/CP5632 Practical week 8
Kivy GUI program to square a number
Emoke Bohuss
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKm(App):
    """ConvertMilesKmApp is a Kivy App for converting miles to km."""
    status_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKm().run()
