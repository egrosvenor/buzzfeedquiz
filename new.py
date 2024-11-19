

import tkinter as tk


window=tk.Tk()
window.title("What Franciscan sterotype are you?")


label1=tk.Label(master=window,text="What intramural sport would you play?", width=50, height=10)
label1.pack()


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


b3=tk.Button(master=f1, text="Guardians", height=10)
b3.grid(row=1, column=0, sticky="nsew")


b4=tk.Button(master=f1, text="Disciples")
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


b3=tk.Button(master=f1, text="Guardians", height=10)
b3.grid(row=1, column=0, sticky="nsew")


b4=tk.Button(master=f1, text="Disciples")
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


window.mainloop()
