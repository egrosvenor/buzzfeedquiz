import tkinter as tk

# use this 
## import tkinter as tk

# border_effects = {
#   "sunken": tk.SUNKEN,
 #   "raised": tk.RAISED,
 #   "groove": tk.GROOVE,
 #   "ridge": tk.RIDGE,
#}

#window = tk.Tk()

#for relief_name, relief in border_effects.items():
   # frame = tk.Frame(master=window, relief=relief, borderwidth=5)
   # frame.pack(side=tk.LEFT)
   # label = tk.Label(master=frame, text=relief_name)
   # label.pack()

#window.mainloop()

questions={
    'What sport do you play?' : ['ultimate frisbee', 'volleyball', 'soccer', 'no intramurals for me'],
    'Choose a Household': ['AMDG', 'Fishers', 'DDM', 'Stella'],
    'Favorite Professor?': ['Scott Hahn', 'Dr. Reinhard', 'Dr. Kuebler', 'Dr. Knox'],
    'What is your major?':['theocat', 'nursing', 'business', 'psych'],
    'Favorite Mass time?': ['6:30 AM', '10:00 AM', 'Noon', '8:00 PM'],
    'Favorite Caf meal?': ['pizza', 'stir fry', 'cereal and ice cream', 'chicken and rice'],
    'What is your favorite place to study?': ['CTT', 'Library', 'JC', 'Dorm'],
    'What do you do in your free time?' : ['Reading outside', 'Go on a walk with my Franny significant other', 'Always studying', 'I am a JC rat'],
    'How often do you go to Latin mass?': ['every other month', 'every single day', 'never', 'when my friends go'],
    'What are you doing this summer?': ['Mission Trip!!', 'Working at Summer Camp', 'Getting an internship/working', 'I do not know yet']
}


window=tk.Tk()
window.title("Which Franciscan steorotype are you?")

for question, answer in questions.items():
    frame = tk.Frame(master=window, text=question, borderwidth=5)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    for x in answer:
        label=tk.Label(master=frame, text=x)
        label.pack()

window.mainloop()
