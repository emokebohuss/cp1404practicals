"""
CP1404 Prac 8
By Emoke Bohuss
Convert miles to km app
"""
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILE_TO_KM_CONVERSION = 1.609344

class ConvertMilesKm(App):
    """ConvertMilesKmApp is a Kivy App for converting miles to km."""
    kms_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label widget."""
        try:
            result = float(value) * MILE_TO_KM_CONVERSION
            self.kms_text = str(result)
        except ValueError:
            self.kms_text = '0.0'

ConvertMilesKm().run()
