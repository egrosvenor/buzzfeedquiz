import tkinter as tk

window=tk.Tk()
window.title("Which Franciscan steorotype are you?")


questions = [
    {'label': 'What sport do you play?', 'buttons': ['ultimate frisbee', 'volleyball', 'soccer', 'no intramurals for me'], 'placement':0},
    {'label': 'Choose a Household', 'buttons': ['AMDG', 'Fishers', 'DDM', 'Stella']},
    {'label': 'Favorite Professor?', 'buttons': ['Scott Hahn', 'Dr. Reinhard', 'Dr. Kuebler', 'Dr. Knox']},
    {'label': 'What is your major?', 'buttons': ['theocat', 'nursing', 'business', 'psych']},
    {'label': 'Favorite Mass time?', 'buttons': ['6:30 AM', '10:00 AM', 'Noon', '8:00 PM']},
    {'label': 'Favorite Caf meal?', 'buttons': ['pizza', 'stir fry', 'cereal and ice cream', 'chicken and rice']},
    {'label': 'What is your favorite place to study?', 'buttons': ['CTT', 'Library', 'JC', 'Dorm']},
    {'label': 'What do you do in your free time?', 'buttons': ['Reading outside', 'Go on a walk with my Franny significant other', 'Always studying', 'I am a JC rat']},
    {'label': 'How often do you go to Latin mass?', 'buttons': ['every other month', 'every single day', 'never', 'when my friends go']},
    {'label': 'Matt Fradd or Jordan Peterson?', 'buttons': ['Matt Fradd', 'Jordan Peterson']},
    {'label': 'What are you doing this summer?', 'buttons': ['Mission Trip!!', 'Working at Summer Camp', 'Getting an internship/working', 'I do not know']},
]

f1=tk.Frame(master=window)

f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

def create_question(question):
    row=0
    col=0
    label=tk.Label(master=f1,text=question["label"], width=50, height=10)
    label.pack(pady=2)
    for button_text in question["buttons"]:
        button=tk.Button(master=f1, text=button_text, height=10)
        button.pack()
        
for x in questions:
    create_question(x)

window.mainloop()

