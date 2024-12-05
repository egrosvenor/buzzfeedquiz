import tkinter as tk
from PIL import Image, ImageTk

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




list1=["no intramurals for me", "Fishers", "Scott Hahn", "theocat", "6:30 AM", "stir fry", "Dorm","Go on a walk with \n my Franny significant other", "every single day", "Working at Summer Camp" ]
list2=["DDM", "ultimate frisbee", "Dr. Reinhard", "psych", "10:00 AM", "cereal and ice crea", "Library", "Library", "Reading outside", "every other month", "Mission Trip!!"]
list3=["soccer", "Stella", "Dr. Kuebler", "nursing", "Noon", "chicken and rice", "CTT", "Always studying", "when my friends go", "Getting an \n internship/working" ]
list4=["AMDG", "volleyball", "Dr. Knox", "Business", "8:00 PM", "JC", "pizza", "I am a JC rat", "never", "I do not know yet"] 

list5=["DDM", "Dr. Reinhard", "Library", "Reading outside", "Mission Trip!!", "ultimate frisbee", "psych", "Noon", "chicken and rice", "every other month"]
list6=["Fishers", "Scott Hahn", "theocat", "6:30 AM", "Dorm", "Go on a walk with \n my Franny significant other", "every single day", "Always studying", "volleyball", "I do not know yet"]
list7=["no intramurals for me", "Working at Summer Camp", "AMDG", "Dr. Knox", "Business", "8:00 PM", "JC", "pizza", "I am a JC rat", "never" ]
list8=["stir fry", "cereal and ice cream", "soccer",  "Stella", "Dr. Kuebler", "nursing", "CTT", "Getting an \n internship/working", "10:00 AM", "when my friends go"]

a=0
b=0
c=0
d=0


def fun(x):
    print(x)

    global a, b, c, d

    if x in list1 and x in list6:
        a+=2
        b+=1
    elif x in list1 and x in list7:
        a+=2
        c+=1
    elif x in list1 and x in list8:
        a+=2
        d+=1
   
    elif x in list2 and x in list5:
        b+=2
        a+=1
    elif x in list2 and x in list7:
        b+=2
        c+=1
    elif x in list2 and x in list8:
        b+=2
        d+=1
   
        
    elif x in list3 and x in list5:
        c+=2
        a+=1
    elif x in list3 and x in list6:
        c+=2
        b+=1
    elif x in list3 and x in list8:
        c+=2
        d+=1

    elif x in list4 and x in list5: 
        d+=2
        a+=1
    elif x in list4 and x in list6: 
        d+=2
        b+=1
    elif x in list4 and x in list7: 
        d+=2
        c+=1
    


for x in questions:
    Label=tk.Label(master=content_frame, text=x, height=5)
    Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    Frame=tk.Frame(master=content_frame)
    Frame.pack(fill=tk.X, side=tk.TOP)

    for e in questions[x]:
        button=tk.Button(master=Frame, text=e, height=7, width=16, command=lambda x=e: fun(x))
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



def answer():
    if a>b and a>c and a>d:
        print("You are a PDP boy/homeschooled girl")
        window=tk.Tk()
        window.title("You are ....")
        window.minsize(500,500)
        Label=tk.Label(master=window, text="PDP boy/homeschooled girl", height=12, width=12)
        Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Label=tk.Label(master=window, text="You enjoy long walks to the chapel and liturgy of the hours. Welcome to Franciscan!", height=5, width=12)
        Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window = Image.open("Chapel-2-1 (1).jpg")
        label = tk.Label(Image)
        label.pack(window)
        window.mainloop()
    elif b>a and b>c and b>d:
        print("You are that one passionate missionary kid/FOP lover")
        window=tk.Tk()
        window.title("You are ....")
        Label=tk.Label(master=window, text="That one passionate missionary kid/FOP lover", height=30, width=30)
        Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.mainloop()
    elif c>a and c>b and c>d:
        print("You are a social floater")
        window=tk.Tk()
        window.title("You are ....")
        Label=tk.Label(master=window, text="Social floater", height=30, width=30)
        Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.mainloop()
    elif d>a and d>b and d>c:
        print("AMDG intent/Little Flowers intent")
        window=tk.Tk()
        window.title("You are ....")
        Label=tk.Label(master=window, text="AMDG intent/Little Flowers intent", height=30, width=30)
        Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.mainloop()
    else:
        print("You are a social floater")
        window=tk.Tk()
        window.title("You are ....")
        Label=tk.Label(master=window, text="Social floater", height=30, width=30)
        Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        window.mainloop()
 

submit=tk.Button(master=content_frame, text="Sumbit Answers", command=answer)
submit.pack()

    

content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()
