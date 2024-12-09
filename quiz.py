import tkinter as tk
from tkinter import PhotoImage
#from PIL import Image, ImageTk

questions={
    'What intramural sport do you play?' : ['ultimate frisbee', 'volleyball', 'soccer', 'no intramurals for me'],
    'Choose a Household': ['AMDG', 'Fishers', 'DDM', 'Stella'],
    'Favorite Professor?': ['Scott Hahn', 'Dr. Reinhard', 'Dr. Pathakamuri', 'Dr. Knox'],
    'What is your major?':['theocat', 'nursing', 'business', 'psych'],
    'Favorite Mass time?': ['6:30 AM', '10:00 AM', 'Noon', '8:00 PM'],
    'Favorite Caf meal?': ['pizza', 'stir fry', 'cereal and ice cream', 'chicken and rice'],
    'What is your favorite place to study?': ['CTT', 'Library', 'JC', 'Dorm'],
    'What do you do in your free time?' : ['Reading outside', 'Go on a walk with \n my Franny significant \n other', 'Always studying', 'I am a JC rat'],
    'How often do you go to Latin mass?': ['every other month', 'every single day', 'never', 'when my friends go'],
    'What are you doing this summer?': ['Mission Trip!!', 'Working at Summer Camp', 'Getting an \n internship/working', 'I do not know yet']
}


window=tk.Tk()
window.title("Which Franciscan steorotype are you?")
window.minsize(725,700)

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

canvas=tk.Canvas(f1)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar=tk.Scrollbar(f1, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set, bg="dark green")

content_frame=tk.Frame(canvas)
content_frame.configure(bg="dark green")

canvas.create_window((0,0), window=content_frame, anchor="nw")


label=tk.Label(master=content_frame, text="Which Franciscan steorotype are you?", height=5, font=("Courier", 18, "bold"), bg="dark green")
label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




list1=["no intramurals for me", "Fishers", "Scott Hahn", "theocat", "6:30 AM", "stir fry", "Dorm","Go on a walk with \n my Franny significant \n other", "every single day", "Working at Summer Camp" ]
list2=["DDM", "ultimate frisbee", "Dr. Reinhard", "psych", "10:00 AM", "cereal and ice crea", "Library", "Library", "Reading outside", "every other month", "Mission Trip!!"]
list3=["soccer", "Stella", "Dr. Pathakamuri", "nursing", "Noon", "chicken and rice", "CTT", "Always studying", "when my friends go", "Getting an \n internship/working" ]
list4=["AMDG", "volleyball", "Dr. Knox", "Business", "8:00 PM", "JC", "pizza", "I am a JC rat", "never", "I do not know yet"] 

list5=["DDM", "Dr. Reinhard", "Library", "Reading outside", "Mission Trip!!", "ultimate frisbee", "psych", "Noon", "chicken and rice", "every other month"]
list6=["Fishers", "Scott Hahn", "theocat", "6:30 AM", "Dorm", "Go on a walk with \n my Franny significant \n other", "every single day", "Always studying", "volleyball", "I do not know yet"]
list7=["no intramurals for me", "Working at Summer Camp", "AMDG", "Dr. Knox", "Business", "8:00 PM", "JC", "pizza", "I am a JC rat", "never" ]
list8=["stir fry", "cereal and ice cream", "soccer",  "Stella", "Dr. Pathakamuri", "nursing", "CTT", "Getting an \n internship/working", "10:00 AM", "when my friends go"]

a=0
b=0
c=0
d=0


def fun(x, m):

    m.configure(bg="dark green", fg="white")

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
    Label=tk.Label(master=content_frame, text=x, height=5, font=("Courier", 14, "bold"), bg="dark green")
    Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    Frame=tk.Frame(master=content_frame)
    Frame.pack(fill=tk.X, side=tk.TOP)

    for e in questions[x]:
        button=tk.Button(master=Frame, text=e, height=7, width=20, font=("Courier", 12), bg="tan")
        button.configure(command=lambda x=e, m=button: fun(x,m))
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



def answer():
    global window
    window.destroy()
    if a>b and a>c and a>d:
        print("You are a PDP boy/homeschooled girl")
        window1=tk.Tk()
        window1.title("You are ....")
        window1.minsize(700,500)
        window1.configure(bg="dark green")

        Label=tk.Label(master=window1, text="PDP boy/homeschooled girl", font=("Courier", 14, "bold"), bg="dark green")
        Label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        Label4=tk.Label(master=window1, text="You enjoy long walks to the chapel and liturgy of the hours. Welcome to Franciscan!", height=5, width=12, font=("Courier", 14, "bold"), bg="dark green")
        Label4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        img = PhotoImage(file="Chapel-2-1.png")
        img=img.subsample(2)
        label6 = tk.Label(window1, image=img, bg="dark green")
        label6.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        window1.mainloop()

    elif b>a and b>c and b>d:
        print("You are that one passionate missionary kid/FOP lover")

        window3=tk.Tk()
        window3.title("You are ....")
        window3.minsize(700,500)
        window3.configure(bg="dark green")

        Label11=tk.Label(master=window3, text="That one passionate missionary kid/FOP lover", font=("Courier", 14, "bold"), bg="dark green")
        Label11.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        Label2=tk.Label(master=window3, text="What's your favorite worship song? \n How long have you played guitar? Welcome to Franciscan!", height=5, width=12, font=("Courier", 14, "bold"), bg="dark green")
        Label2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        img2 = PhotoImage(file="file.png")
        img2= img2.subsample(4)
        label2 = tk.Label(window3, image=img2, bg="dark green")
        label2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        window3.mainloop()

    elif c>a and c>b and c>d:
        print("You are a social floater")
        window4=tk.Tk()
        window4.title("You are ....")
        window4.minsize(700,500)
        window4.configure(bg="dark green")

        Label21=tk.Label(master=window4, text="Social Floater", font=("Courier", 14, "bold"), bg="dark green")
        Label21.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        Label3=tk.Label(master=window4, text="You don't really have a set group, but you seem to know \n everyone on campus. Welcome to Franciscan!", height=5, width=12, font=("Courier", 14, "bold"), bg="dark green")
        Label3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        img3 = PhotoImage(file="socialfloater.png")
        img3=img3.subsample(4)
        label3 = tk.Label(window4, image=img3, bg="dark green")
        label3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        window4.mainloop()

    elif d>a and d>b and d>c:
        print("AMDG intent/Little Flowers intent")

        window5=tk.Tk()
        window5.title("You are ....")
        window5.minsize(700,500)
        window5.configure(bg="dark green")

        Label31=tk.Label(master=window5, text="AMDG intent/Little Flowers intent", font=("Courier", 14, "bold"), bg="dark green")
        Label31.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        Label4=tk.Label(master=window5, text="You love your household and hanging out \n with them! Welcome to Franciscan!", height=5, width=15, font=("Courier", 14, "bold"), bg="dark green")
        Label4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        img4 = PhotoImage(file="amdg.png")
        img4=img4.subsample(1)
        label4 = tk.Label(window5, image=img4,bg="dark green")
        label4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        window5.mainloop()

    else:
        print("You are a social floater")
        window4=tk.Tk()
        window4.title("You are ....")
        window4.minsize(700,500)
        window4.configure(bg="dark green")

        Label21=tk.Label(master=window4, text="Social Floater", font=("Courier", 14, "bold"), bg="dark green")
        Label21.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        Label3=tk.Label(master=window4, text="You don't really have a group but you seem to know \n everyone on campus. Welcome to Franciscan!", height=5, width=12, font=("Courier", 14, "bold"), bg="dark green")
        Label3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        img3 = PhotoImage(file="socialfloater.png")
        img3=img3.subsample(4)
        label3 = tk.Label(window4, image=img3, bg="dark green")
        label3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        window4.mainloop()
 

submit=tk.Button(master=content_frame, text="Sumbit Answers", command=answer, height=2, width=15, bg="tan", font=("Courier", 14, "bold"))
submit.pack()

    

content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()
