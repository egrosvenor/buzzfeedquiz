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

canvas=tk.Canvas(f1)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar=tk.Scrollbar(f1, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

content_frame=tk.Frame(canvas)

canvas.create_window((0,0), window=content_frame, anchor="nw")

def create_question(question):
    label=tk.Label(master=content_frame,text=question["label"], width=40, height=5)
    label.pack(pady=2)

    button_frame=tk.Frame(master=content_frame)
    button_frame.pack(fill=tk.X, padx=10, pady=5)


    for button_text in question["buttons"]:
        button=tk.Button(master=button_frame, text=button_text, height=5, width=15)
        button.pack(side=tk.LEFT, padx=5)


        
for x in questions:
    create_question(x)

content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()


i=0

def one_point():
    i=+1

def two_point():
    i=+2

def three_point():
    i=+3

def four_point():
    i=+4