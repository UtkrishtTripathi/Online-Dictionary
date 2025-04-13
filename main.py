# Importing Libraries
from tkinter import *
from PyDictionary import PyDictionary
import customtkinter as ctk


# Setting up Window Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Creating a Window
root = ctk.CTk()
root.title('Custom Dictionary')
root.geometry('600x500')

try:
    icon = PhotoImage(file = 'Dictionary_logo.png')
    root.iconphoto(True, icon)
except:
    print("Icon file not found - using default icon")

# lookup functions 
def lookup():
    # Clear the text from the dictionary
    text.delete(1.0, END)
    
    word = entry.get().strip()
    if not word:
        text.insert(END, "Please enter a word to lookup")
        return

    try:
        # lookup the word
        dictionary = PyDictionary()
        definition = dictionary.meaning(word)
        
        if not definition:
            text.insert(END, f"No definition found for '{word}'")
            return
            
        # Finding key and value in definition
        for key, value in definition.items():
            # put the key header in textbox
            text.insert(END, key + '\n\n')
            
            # put Value header in textbox
            for values in value:
                text.insert(END, f' * {values}\n\n')
    except Exception as e:
        text.insert(END, "Failed to connect to dictionary service. Please check your internet connection and try again.")



# Creating Master Frame      
master_frame = ctk.CTkFrame(root , corner_radius = 0 , height = 450 , fg_color="transparent" )  
master_frame.grid(row = 0, column = 1 , padx = 10 , pady = 10)    
 
# Creating Input frame
labelFrame1 = ctk.CTkFrame(master_frame , corner_radius=10)
labelFrame1.pack()

# Inputbox
entry = ctk.CTkEntry(labelFrame1 , width=350 , height = 30 , corner_radius=10 , text_color = 'silver' , font = ("Arial Rounded MT Bold" , 20) )
entry.grid(row = 0, column = 0,padx = 10 , pady = 10)

# Button 
button = ctk.CTkButton(labelFrame1 , corner_radius=8 , height = 30 , width = 180 , text = 'LookUp', command=lookup , font = ("Arial Rounded MT Bold" , 20) )
button.grid(row = 0, column = 1,padx = 10 , pady = 10 )


# TextBox
text = ctk.CTkTextbox(master_frame , corner_radius=10 ,height = 400 , width = 550 , wrap = WORD , text_color = 'silver' , border_width = 0 , font = ("Arial Rounded MT Bold" , 20))
text.pack(pady = 10)

root.mainloop()

#, bg = '#2a2d2e'