"""
CP1404 Prac 8
By Emoke Bohuss
Convert miles to km app
"""
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILE_TO_KM_CONVERSION = 1.60934


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
        """Handle calculation, output result to label widget."""
        try:
            result = float(value) * MILE_TO_KM_CONVERSION
            self.kms_text = f"{result:.5f}"
        except ValueError:
            self.kms_text = '0.0'

    def handle_increment(self, value, increment):
        """Increment number of miles by 1 or -1, depending on button pressed."""
        try:
            self.root.ids.input_number.text = str(float(value) + increment)
        except ValueError:
            self.root.ids.input_number.text = str(0.0 + increment)


ConvertMilesKm().run()
