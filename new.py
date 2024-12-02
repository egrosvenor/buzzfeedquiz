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



label1=tk.Label(master=content_frame,text="What intramural sport would you play?", width=50, height=10)
label1.pack()

f1=tk.Frame(master=content_frame)
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




label2=tk.Label(master=content_frame,text="Choose a household", width=50, height=10)
label2.pack()

f2=tk.Frame(master=content_frame)
f2.pack(fill=tk.BOTH, expand=True)

f2.rowconfigure([0,1], minsize=20, weight=1)
f2.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f2, text="AMDG", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f2, text="Fishers")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f2, text="DDM", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f2, text="Stella")
b4.grid(row=1, column=1, sticky="nsew")




label1=tk.Label(master=content_frame,text="Who is your favorite professor?", width=50, height=10)
label1.pack()

f3=tk.Frame(master=content_frame)
f3.pack(fill=tk.BOTH, expand=True)

f3.rowconfigure([0,1], minsize=20, weight=1)
f3.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f3, text="Scott Hahn", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f3, text="Dr. Reinhard")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f3, text="Dr. Kuebler", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f3, text="Dr. Knox")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=content_frame,text="What's your major?", width=50, height=10)
label1.pack()

f4=tk.Frame(master=content_frame)
f4.pack(fill=tk.BOTH, expand=True)

f4.rowconfigure([0,1], minsize=20, weight=1)
f4.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f4, text="TheoCat", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f4, text="Nursing")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f4, text="Business", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f4, text="Psych")
b4.grid(row=1, column=1, sticky="nsew")


label1=tk.Label(master=content_frame,text="What's your favorite mass time?", width=50, height=10)
label1.pack()

f6=tk.Frame(master=content_frame)
f6.pack(fill=tk.BOTH, expand=True)

f6.rowconfigure([0,1], minsize=20, weight=1)
f6.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f6, text="6:30 am", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f6, text="10:00 am ")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f6, text="Noon")
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f6, text="8 pm")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=content_frame,text="Pick a place to study", width=50, height=10)
label1.pack()

f7=tk.Frame(master=content_frame)
f7.pack(fill=tk.BOTH, expand=True)

f7.rowconfigure([0,1], minsize=20, weight=1)
f7.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f7, text="CTT", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f7, text="Library")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f7, text="Dorm", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f7, text="JC")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=content_frame,text="Favorite Cafe meal", width=50, height=10)
label1.pack()

f8=tk.Frame(master=content_frame)
f8.pack(fill=tk.BOTH, expand=True)

f8.rowconfigure([0,1], minsize=20, weight=1)
f8.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f8, text="Pizza", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f8, text="Stir Fry")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f8, text="Chicken and Rice", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f8, text="Cereal and Ice Cream")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=content_frame,text="What do you do in your freetime?", width=50, height=10)
label1.pack()

f9=tk.Frame(master=content_frame)
f9.pack(fill=tk.BOTH, expand=True)

f9.rowconfigure([0,1], minsize=20, weight=1)
f9.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f9, text="Read spiritual boooks outside", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f9, text="Go on long walks with your Frannie significant other")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f9, text="Always studying", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f9, text="I'm a JC rat")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=content_frame,text="How often do you go to Latin Mass?", width=50, height=10)
label1.pack()

f10=tk.Frame(master=content_frame)
f10.pack(fill=tk.BOTH, expand=True)

f10.rowconfigure([0,1], minsize=20, weight=1)
f10.columnconfigure([0,1], minsize=20, weight=1)

b1=tk.Button(master=f10, text="Every other month", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f10, text="Every single day")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f10, text="When my friends go", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f10, text="Never")
b4.grid(row=1, column=1, sticky="nsew")



label1=tk.Label(master=content_frame,text="Are you working at a summer camp or getting an internship this summer?", width=50, height=10)
label1.pack()

f11=tk.Frame(master=content_frame)
f11.pack(fill=tk.BOTH, expand=True)

f11.rowconfigure([0,1], minsize=20, weight=1)
f11.columnconfigure([0, 1], minsize=20, weight=1)

b1=tk.Button(master=f11, text="Summer camp", height=10)
b1.grid(row=0, column=0, sticky="nsew")

b2=tk.Button(master=f11, text="Internship/working")
b2.grid(row=0, column=1, sticky="nsew")

b3=tk.Button(master=f11, text="Mission Trip!!", height=10)
b3.grid(row=1, column=0, sticky="nsew")

b4=tk.Button(master=f11, text="I do not know yet")
b4.grid(row=1, column=1, sticky="nsew")



content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()