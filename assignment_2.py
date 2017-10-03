#Created by: Justin Bronson
#Created on: Sept, 2017.
#Created for: ICS3U
#This program calculates the height of an
# object in mid air using the gravity formula

import ui

def calculate_button_touch_up_inside(sender):
    #calculate circumference
    
    #constant
    GRAVITY = 9.8
    
    #input
    seconds = int(view['seconds_textbox'].text)
    
    #process
    height = 100 - (0.5 * GRAVITY * seconds ** 2)
    
    #output
    view['answer_label'].text = 'The height is: ' + str(height) + ' cm'

view = ui.load_view()
view.present('full_screen')
