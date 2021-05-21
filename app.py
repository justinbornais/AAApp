from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window

class MainApp(App):
    Window.clearcolor = (1, 1, 1, 1)
    days = 0
    
    def build(self):
        layout = FloatLayout()
        
        label = Label(text='Welcome to Sobriety!',
                      size_hint=(0.8, 0.8),
                      pos=(100, 80),
                      color=("000000"))
        
        layout.add_widget(label)
        
        soberButton = Button(text="Press to join sobriety!",
                        size_hint=(0.2, 0.2),
                        pos_hint={"center_x": 0.2, "y": 0},
                        color=("000000"),
                        background_color=("#ffeec2"))
        
        relapseButton = Button(text="Press if you relapse",
                        size_hint=(0.2, 0.2),
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
        
        soberButton.bind(on_press=soberButtonFunc)
        layout.add_widget(soberButton)
        
        relapseButton.bind(on_press=relapseButtonFunc)
        layout.add_widget(relapseButton)
        
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()