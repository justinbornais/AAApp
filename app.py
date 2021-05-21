from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

sober = False
days = 0

class MainApp(App):
    
    days = 0
    
    def build(self):
        layout = FloatLayout()
        
        label = Label(text='Welcome to Sobriety!',
                      size_hint=(0.8, 0.8),
                      pos=(100, 100))
        
        layout.add_widget(label)
        
        soberButton = Button(text="Press to join sobriety!",
                        size_hint=(0.3, 0.3),
                        pos_hint={"center_x": 0.5, "y": 0})
        
        def soberButtonFunc(soberButton):
            if soberButton.text == "Press to join sobriety!":
                soberButton.text = "Add one day of sobriety!"
                self.days = 1
                label.text = "Welcome to Sobriety!\nYou are 1 day sober!"
            else:
                self.days += 1
                label.text = f"Welcome to Sobriety!\nYou are {self.days} days sober!"
        
        soberButton.bind(on_press=soberButtonFunc)
        layout.add_widget(soberButton)
        
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()