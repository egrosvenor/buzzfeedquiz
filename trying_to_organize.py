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



a=0
b=0
c=0
d=0


def twoPDP():
    global a
    a+=2

def twoFOP():
    global b
    b+=2

def twofloater():
    global d
    d+=2

def twoAMDG():
    global c
    c+=2

def onePDP():
    global a
    a+=1

def oneFOP():
    global b
    b+=1

def onefloater():
    global c
    c+=1

def oneAMDG():
    global d
    d+=1


list1=["no intramurals for me", "Fishers", "Scott Hahn", "theocat", "6:30 AM", "stir fry", "Dorm","Go on a walk with \n my Franny significant other", "every single day", "Working at Summer Camp" ]
list2=["DDM", "ultimate frisbee", "Dr. Reinhard", "psych", "10:00 AM", "cereal and ice crea", "Library", "Library", "Reading outside", "every other month", "Mission Trip!!"]
list3=["soccer", "Stella", "Dr. Kuebler", "nursing", "Noon", "chicken and rice", "CTT", "Always studying", "when my friends go", "Getting an \n internship/working" ]
list4=["AMDG", "volleyball", "Dr. Knox", "Business", "8:00 PM", "JC", "pizza", "I am a JC rat", "never", "I do not know yet"] 

list5=["DDM", "Dr. Reinhard", "Library", "Reading outside", "Mission Trip!!", "ultimate frisbee", "psych", "Noon", "chicken and rice", "every other month"]
list6=["Fishers", "Scott Hahn", "theocat", "6:30 AM", "Dorm", "Go on a walk with \n my Franny significant other", "every single day", "Always studying", "volleyball", "I do not know yet"]
list7=["no intramurals for me", "Working at Summer Camp", "AMDG", "Dr. Knox", "Business", "8:00 PM", "JC", "pizza", "I am a JC rat", "never" ]
list8=["stir fry", "cereal and ice creal", "soccer",  "Stella", "Dr. Kuebler", "nursing", "CTT", "Getting an \n internship/working", "10:00 AM", "when my friends go"]

def fun(x):
    global a, b, c, d
    if x in list1:
        twoPDP()
        
    elif x in list2:
        twoFOP()
        
    elif x in list3:
        twofloater()
        
    elif x in list4: 
        twoAMDG()
        
def fun2(x):
    global a, b, c, d
    if x in list5:
        onePDP()
        
    elif x in list6:
        oneFOP()
        
    elif x in list7:
        onefloater()
        
    elif x in list8:
        oneAMDG() 
      
    print(f'PDP: {a}, FOP: {b}, Floater: {c}, AMDG: {d}')



for x in questions:
    Label=tk.Label(master=content_frame, text=x, height=5)
    Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    Frame=tk.Frame(master=content_frame)
    Frame.pack(fill=tk.X, side=tk.TOP)

    for e in questions[x]:
        button=tk.Button(master=Frame, text=e, height=7, width=16, command=lambda x=e: (fun(x), fun2(x)))
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


submit=tk.Button(master=content_frame, text="Sumbit Answers")
submit.pack()


content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()
