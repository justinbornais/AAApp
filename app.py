from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import webbrowser

def show_relapse_popup():
    relapsePopup = Popup(title="Sorry to see you relapse!",
                        size_hint=(None, None),
                        size=(400, 400))
                        #size=(400, 400),
                        #color=("000000"),
                        #background="images/pure-white-background-85a2a7fd.jpg")
    
    button1 = Button(text="Click for some helpful resources.",
                    size_hint=(0.3, 0.3),
                    pos=(100,100),
                    color=("000000"),
                    background_color=("#ffffff"))
    
    def resources(button1):
        webbrowser.open("https://www.canada.ca/en/health-canada/services/substance-use/get-help/get-help-problematic-substance-use.html")
    
    button1.bind(on_press=resources)
    relapsePopup.add_widget(button1)
    
    relapsePopup.open()

class MainApp(App):
    Window.clearcolor = (1, 1, 1, 1)
    days = 0
    
    def build(self):
        layout = FloatLayout()
        
        label = Label(text='Welcome to Sobriety!',
                      size_hint=(0.8, 0.8),
                      pos=(100, 200),
                      color=("000000"))
        
        layout.add_widget(label)
        
        soberButton = Button(text="Press to join sobriety!",
                        size_hint=(0.3, 0.3),
                        pos_hint={"center_x": 0.2, "y": 0},
                        color=("000000"),
                        background_color=("#ffeec2"))
        
        relapseButton = Button(text="Press if you relapse",
                        size_hint=(0.3, 0.3),
                        pos_hint={"center_x": 0.8, "y": 0},
                        color=("000000"),
                        background_color=("#ffeec2"))
        
        
        def soberButtonFunc(soberButton):
            if soberButton.text == "Press to join sobriety!":
                soberButton.text = "Add one day of sobriety!"
                self.days = 1
                label.text = "Welcome to Sobriety!\nYou are 1 day sober!"
            else:
                self.days += 1
                label.text = f"Welcome to Sobriety!\nYou are {self.days} days sober!"
        
        def relapseButtonFunc(relapseButton):
            self.days = 0
            label.text = "So sorry to see you relapse!"
            soberButton.text = "Press to join sobriety!"
            show_relapse_popup()
        
        soberButton.bind(on_press=soberButtonFunc)
        layout.add_widget(soberButton)
        
        relapseButton.bind(on_press=relapseButtonFunc)
        layout.add_widget(relapseButton)
        
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()