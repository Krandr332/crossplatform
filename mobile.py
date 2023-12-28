# mobile.py

from kivy.uix.popup import Popup

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import random

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDLabel:
        text: 'TV Plot Generator'
        halign: 'center'
        font_size: '24sp'

    MDRaisedButton:
        text: 'Generate Plot'
        on_release: app.generate_plot()
        pos_hint: {'center_x': 0.5}
'''

class TVPlotGeneratorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def generate_plot(self):
        plot = self._generate_plot()
        plot_text = f"{plot['plot_type']} {plot['character_type']}{plot['character']} {plot['success']}{plot['activity']}{plot['resolution']}"

        self.show_popup('Generated Plot', plot_text)

    def show_popup(self, title, text):
        content = MDBoxLayout(orientation='vertical')
        content.add_widget(MDLabel(text=text))
        popup = self.create_popup(title, content)
        popup.open()

    def create_popup(self, title, content):
        return Popup(title=title, content=content, size_hint=(None, None), size=(400, 400))

    def _choose_option(self, options):
        option_index = random.randint(0, len(options) - 1)
        return options[option_index]

    def _generate_plot(self):
        plot_type = self._choose_option(["PROGRAM", "REPORT", "SPECIAL", "SERIES", "STORY"])
        character_type = self._choose_option(["SWINGING", "BRILLIANT", "SALTY", "HILARIOUS", "SENSITIVE", "DODDERING", "HENPECKED", "DEDICATED", "THOUGHTFUL", "HEAVY"])
        character = self._choose_option(['GIRL COWHAND', 'LITTLE BOY', 'SCIENTIST', 'LAWYER', 'TOWN MARSHALL', 'DENTIST', 'BUS DRIVER', 'JUNGLE MAN', 'SECRET AGENT', 'COLLIE'])
        success = self._choose_option(['A WHIZ', 'A FLOP', 'MEDIOCRE', 'A SUCCESS', 'A DISASTER'])
        activity = self._choose_option(['SOLVING CRIMES', 'ROPING COWS', 'COOKING HEALTH FOOD', 'PITCHING WOO', 'PROTECTING ECOLOGY', 'HELPING CHILDREN', 'TWO-FISTED DRINKING', 'FIGHTING FIRES', 'HERDING ELEPHANTS', 'WINNING RACES'])
        resolution = self._choose_option(['RECOVERS THE JEWELS', 'FOILS THE SPIES', 'DESTROYS THE CITY', 'FINDS LOVE', 'SAVES THE ANIMALS', 'CONFESSES', 'DISCOVERS THE SECRET', 'STOPS THE FLOOD', 'HELPS THE DOG', 'MAKES THE SACRIFICE'])

        return {
            'plot_type': plot_type,
            'character_type': character_type,
            'character': character,
            'success': success,
            'activity': activity,
            'resolution': resolution
        }

if __name__ == '__main__':
    TVPlotGeneratorApp().run()
