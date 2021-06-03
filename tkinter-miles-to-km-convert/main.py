from tkinter import *

window=Tk()
window.title("Miles to Kilometer Convertor")
window.minsize(320,150)
window.config(padx=50, pady=30)

def calculate():
    miles=float(entry.get())
    km=miles*1.609
    label_result.config(text=f"{km}",font =("Aerial" , 10 , "bold"))



#entry
entry=Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0,column=1)


#Label1 -
label_miles=Label(text="miles ",font =("Aerial" , 10 , "bold"))
label_miles.config(padx=5, pady=5)
label_miles.grid(row=0,column=2)

#button
button=Button(text="Calculate",command=calculate)
button.grid(row=3,column=1)

#Label2 -
label_equal=Label(text=f"is equal to ",font =("Aerial" , 10 , "bold"))
label_equal.grid(row=2,column=0)


#Label3 -
label_result=Label(text="0",font =("Aerial" , 10 , "bold"))
label_result.grid(row=2,column=1)


#Label4 -
label_km=Label(text="k m ",font =("Aerial" , 10 , "bold"))
label_km.grid(row=2,column=2)


window.mainloop()