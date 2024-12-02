import tkinter as tk

questions={
    'What sport do you play?' : ['ultimate frisbee', 'volleyball', 'soccer', 'no intramurals for me'],
    'Choose a Household': ['AMDG', 'Fishers', 'DDM', 'Stella'],
    'Favorite Professor?': ['Scott Hahn', 'Dr. Reinhard', 'Dr. Kuebler', 'Dr. Knox'],
    'What is your major?':['theocat', 'nursing', 'business', 'psych'],
    'Favorite Mass time?': ['6:30 AM', '10:00 AM', 'Noon', '8:00 PM'],
    'Favorite Caf meal?': ['pizza', 'stir fry', 'cereal and ice cream', 'chicken and rice'],
    'What is your favorite place to study?': ['CTT', 'Library', 'JC', 'Dorm'],
    'What do you do in your free time?' : ['Reading outside', 'Go on a walk with \n my Franny significant other', 'Always studying', 'I am a JC rat'],
    'How often do you go to Latin mass?': ['every other month', 'every single day', 'never', 'when my friends go'],
    'What are you doing this summer?': ['Mission Trip!!', 'Working at Summer Camp', 'Getting an \n internship/working', 'I do not know yet']
}




window=tk.Tk()
window.title("Which Franciscan steorotype are you?")

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
    i+=1

def two_point():
    global i
    i+=2

def three_point():
    global i
    i+=3

def four_point():
    global i
    i+=4

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
    print(f"Your score is {i}")


for x in questions:
    Label=tk.Label(master=content_frame, text=x, height=5)
    Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    Frame=tk.Frame(master=content_frame)
    Frame.pack(fill=tk.X, side=tk.TOP)

    for b in questions[x]:
        button=tk.Button(master=Frame, text=b, height=7, width=16, command=lambda x=b: fun(x))
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)





content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()
