import tkinter as tk


window=tk.Tk()
window.title("Which Franciscan steorotype are you?")


questions = [
    {'label': 'What sport do you play?', 'buttons': ['ultimate frisbee', 'volleyball', 'soccer', 'no intramurals for me']},
    {'label': 'Choose a Household', 'buttons': ['AMDG', 'Fishers', 'DDM', 'Stella']},
    {'label': 'Favorite Professor?', 'buttons': ['Scott Hahn', 'Dr. Reinhard', 'Dr. Kuebler', 'Dr. Knox']},
    {'label': 'What is your major?', 'buttons': ['theocat', 'nursing', 'business', 'psych']},
    {'label': 'Favorite Mass time?', 'buttons': ['6:30 AM', '10:00 AM', 'Noon', '8:00 PM']},
    {'label': 'Favorite Caf meal?', 'buttons': ['pizza', 'stir fry', 'cereal and ice cream', 'chicken and rice']},
    {'label': 'What is your favorite place to study?', 'buttons': ['CTT', 'Library', 'JC', 'Dorm']},
    {'label': 'What do you do in your free time?', 'buttons': ['Reading outside', 'Go on a walk with my Franny significant other', 'Always studying', 'I am a JC rat']},
    {'label': 'How often do you go to Latin mass?', 'buttons': ['every other month', 'every single day', 'never', 'when my friends go']},
    {'label': 'What are you doing this summer?', 'buttons': ['Mission Trip!!', 'Working at Summer Camp', 'Getting an internship/working', 'I do not know yet']},
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


i=0

def one_point():
    global i
    i=+1

def two_point():
    global i
    i=+2

def three_point():
    global i
    i=+3

def four_point():
    global i
    i=+4


list1=["no intramurals for me", "Fishers", "Scott Hahn", "theocat", "6:30 AM", "cereal and ice cream", "Dorm","Go on a walk with my Franny significant other", "every single day", "Mission Trip!!" ]
list2=["DDM", "ultimate frisbee", "Dr. Reinhard", "psych", "10:00 AM", "stir fry", "Library", "Reading outside", "every other month", "Working at Summer Camp"]
list3=["soccer", "Stella", "Dr. Kuebler", "nursing", "Noon", "chicken and rice", "CTT", "Always studying", "when my friends go", "Getting an internship/working" ]
list4=["AMDG", "volleyball", "Dr. Knox", "Business", "8:00 PM", "JC", "pizza", "I am a JC rat", "never", "I do not know yet"] 

def fun(x):
    if x in list1:
        one_point()
    elif x in list2:
        two_point()
    elif x in list3:
        three_point()
    elif x in list4: 
        four_point()
    

def create_question(question):
    label=tk.Label(master=content_frame,text=question["label"], width=40, height=5)
    label.pack(pady=2)

    button_frame=tk.Frame(master=content_frame)
    button_frame.pack(fill=tk.X, padx=10, pady=5)


    for button_text in question["buttons"]:
        button=tk.Button(master=button_frame, text=button_text, height=5, width=15, command=lambda: fun(button_text))
        button.pack(side=tk.LEFT, padx=5)

        
for x in questions:
    create_question(x)

content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()




if 10<=i<15:
    window=tk.Tk()
    window.title("You are...")
    window.mainloop()

if 15<=i<20:
    pass

if 20<=i<25:
    pass

if 25<=i<30:
    pass

if 30<=i<35:
    pass

if 35<=i<40:
    pass