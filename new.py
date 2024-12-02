import tkinter as tk
window=tk.Tk()
window.title("What Franciscan sterotype are you?")


f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

canvas=tk.Canvas(f1)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar=tk.Scrollbar(f1, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

content_frame=tk.Frame(canvas)

canvas.create_window((0,0), window=content_frame, anchor="nw")

label1=tk.Label(master=window,text="What intramural sport would you play?", width=50, height=10)
label1.pack()

answer_one=0
answer_two=0
answer_three=0
answer_four=0
answer_five=0
answer_six=0

def answer_one():
    pass

def answer_two():
    pass

def answer_three():
    pass

def answer_four():
    pass

def answer_five():
    pass

def answer_six():
    pass

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="ultimate frisbee", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="volleyball")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="soccer", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="I don't play sports")
b4.grid(row=1, column=1, sticky="nsew")




label1=tk.Label(master=window,text="Choose a household", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="AMDG", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Fishers")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="DDM", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="Stella")
b4.grid(row=1, column=1, sticky="nsew")





label1=tk.Label(master=window,text="Choose a household", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="Stella", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Rosa Mystica")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="DOZ", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="DDM")
b4.grid(row=1, column=1, sticky="nsew")




label1=tk.Label(master=window,text="Who is your favorite professor", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="Scott Hahn", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Dr. Reinhard")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="Dr. Kuebler", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="Dr. Knox")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="What's your major?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="TheoCat", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Engineering")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="Computer Sci", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="Philosophy")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="What's your major?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="TheoCat", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Nursing")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="Education", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="Psych")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="What's your favorite mass time?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="6:30 am", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="10:00 am ")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="Noon")
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="8 pm")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="Pick a place to study", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="CTT", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Library")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="Dorm", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="JC")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="Favorite Cafe meal", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="Pizza", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Stir Fry")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="Chicken and Rice", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="Cereal and Ice Cream")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="What do you do in your freetime?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="Read spiritual boooks outside", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Go on long walks with your Frannie significant other")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="Always studying", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="I'm a JC rat")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="How often do you go to Latin Mass?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0,1], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="Every other month", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Every single day")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f1, text="When my friends go", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f1, text="Never")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=window,text="Are you working at a summer camp or getting an internship this summer?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0], minsize=20, weight=1)
f1.columnconfigure([0, 1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="Summer camp", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Internship/working")
b2.grid(row=0, column=1, sticky="nsew")




label1=tk.Label(master=window,text="Matt Fradd or Jordan Peterson?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=window)
f1.pack(fill=tk.BOTH, expand=True)

f1.rowconfigure([0], minsize=20, weight=1)
f1.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f1, text="Matt Fradd", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f1, text="Jordan Peterson")
b2.grid(row=0, column=1, sticky="nsew")



content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()