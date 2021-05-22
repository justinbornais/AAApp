from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

import time

import webbrowser
import random

# Random quotes about quitting drinking. Make sure quotes and quote_authors are aligned.
quotes = ["You don't have to see the whole staircase, just take the first step.",
        "When you quit drinking, you stop waiting.",
        "Not drinking makes me a lot happier.",
        "The day I became free of alcohol was the day that I fully understood and embraced the truth that I would not be giving anything up by not drinking.",
        "First you take a drink, then the drink takes a drink, then the drink takes you."]
quote_authors = ["Anonymous", "Caroline Knapp", "Naomi Campbell", "Liz Hemingway", "Anonymous"]

# The popup for when the person relapses.
def show_relapse_popup():
    relapsePopup = Popup(title="Sorry to see you relapse!",
                        size_hint=(None, None),
                        size=(400, 400))
    
    button1 = Button(text="Click for some helpful resources.",
                    size_hint=(0.3, 0.3),
                    pos=(0,100),
                    color=("000000"), # Black.
                    background_color=("#ffffff")) # White.
    
    # Local function to link the person to a website about getting rid of drinking.
    def resources(button1):
        webbrowser.open("https://www.canada.ca/en/health-canada/services/substance-use/get-help/get-help-problematic-substance-use.html")
    
    button1.bind(on_press=resources) # Add the function to the button when pressed.
    relapsePopup.add_widget(button1)
    
    relapsePopup.open() # Open the popup.

# Similar setup to the relapse popup but this is for the help popup.
def help_popup():
    relapsePopup = Popup(title="Hang in there! You can do it!",
                        size_hint=(None, None),
                        size=(400, 400))
    
    button1 = Button(text="Click for some helpful resources.",
                    size_hint=(0.3, 0.3),
                    pos=(0,100),
                    color=("000000"),
                    background_color=("#ffffff"))
    
    def resources(button1):
        webbrowser.open("https://www.rethinkingdrinking.niaaa.nih.gov/tools/Interactive-worksheets-and-more/Stay-in-control/Coping-With-Urges-To-drink.aspx")
    
    button1.bind(on_press=resources)
    relapsePopup.add_widget(button1)
    
    relapsePopup.open()

def randomQuote():
    num = random.randint(0, len(quotes) - 1) # Random number between 0 and the last element of the quotes. Automatically updates.
    return (quotes[num] + "\n-" + quote_authors[num])


class MainApp(App):
    Window.clearcolor = (1, 1, 1, 1) # Set to white.
    startDate = float(open("data.txt").read())
    
    def build(self):
        layout = FloatLayout() # Create the initial layout.
        
        quote = Label(text="", # Text is empty as there is no quote.
                    color=("000000"), # Black.
                    halign="left", # Align text to the left.
                    size=(500, 200),
                    pos=(0, 250),
                    font_size="20sp")
        
        quote.text_size = quote.size # Needed to wrap the text. Otherwise it will flow out of the screen.
        
        label = Label(text='Welcome to Sobriety!',
                      size_hint=(0.8, 0.8), # 0.8 of the screen for both x and y.
                      halign="center", # Center the text.
                      pos=(100, 150),
                      font_size="20sp",
                      color=("000000"))
        
        layout.add_widget(label) # Add the title to the layout.
        layout.add_widget(quote) # Add the quote.
        
        soberButton = Button(text="Press to join sobriety!",
                        size_hint=(0.3, 0.3),
                        pos_hint={"center_x": 0.5, "y": 0},
                        color=("000000"),
                        background_color=("#ffeec2"))
        
        relapseButton = Button(text="Press if you relapse",
                        size_hint=(0.3, 0.3),
                        pos_hint={"center_x": 0.8, "y": 0},
                        color=("000000"),
                        background_color=("#ffeec2"),
                        border=(30,30,30,30)
                        )
        
        helpButton = Button(text="Help! I wanna drink!",
                            size_hint=(0.3, 0.3),
                            pos_hint={"center_x": 0.2, "y":0},
                            color=("000000"),
                            background_color=("#ffeec2"))
        
        if self.startDate != 0:
            label.text = f"Welcome to Sobriety!\nYou are {self.startDate} days sober!" # Update label text.
            soberButton.text = "Add one day of sobriety!" # Update the text of the sober button button.
            
            if self.startDate >= 10:
                quote.text = randomQuote() # Generate random quote.
        
        # This is the function for when the sober button is pressed.
        def soberButtonFunc(soberButton):

            # Basically check if the person is sober already.
            if soberButton.text == "Press to join sobriety!":
                f = open("data.txt", "w")
                f.write(str(time.time()))
                f.close()
                soberButton.text = "Add one day of sobriety!"  # Update the text of this button.
                self.startDate = float(open("data.txt").read())

            label.text = f"Welcome to Sobriety!\nYou are {str(self.startDate)} days sober!"  # Update label text.
                
            #if self.startDate % 10 == 0:
            #    quote.text = randomQuote() # Generate random quote every 10 days.
            
            # Save the days to the text file.

        
        def relapseButtonFunc(relapseButton):
            self.startDate = 0 # Reset the number of days.
            label.text = "So sorry to see you relapse!" # Update label to match.
            soberButton.text = "Press to join sobriety!" # Reset the sobriety button text.
            quote.text = "" # Get rid of the quote.
            
            # Save the days to the text file.
            f = open("data.txt", "w")
            f.write(str(0))
            f.close()
            show_relapse_popup() # Call the function to show the relapse popup.
        
        def helpButtonFunc(helpButton):
            label.text = f"Hang in there, you can do this!\nYou're {self.startDate} sober already! Keep it up!" # Update label text to be more encouraging.
            help_popup() # Generate the help popup.
        
        soberButton.bind(on_press=soberButtonFunc) # Add the sober function to the sober button whenever pressed.
        layout.add_widget(soberButton)
        
        relapseButton.bind(on_press=relapseButtonFunc)
        layout.add_widget(relapseButton)
        
        helpButton.bind(on_press=helpButtonFunc)
        layout.add_widget(helpButton)
        
        return layout # Basically returns the entire app setup.

# Just don't touch.
if __name__ == '__main__':
    app = MainApp() # Create the app.
    app.run() # Run the app.