import tkinter


def calc_mile_kilo():
    miles = number.get()
    miles = float(miles)
    result = miles * 1.609
    answer['text'] = f"{result}"

window = tkinter.Tk()
window.minsize(height=300,width=500)
window.config(pady=100,padx=100)
number = tkinter.Entry()
number.grid(row=0,column=0)
mile_label = tkinter.Label(text="Miles",font=("Arial",24,"bold"))
mile_label.grid(row=0,column=1)

text = tkinter.Label(text="is equal to  ",font=("Arial",24,"bold"))
text.grid(row=1,column=0)

answer = tkinter.Label(text=0)
answer.grid(row=1,column=1)

kilo = tkinter.Label(text="Kilometers",font=("Arial",24,"bold"))
kilo.grid(row=1,column=2)

button = tkinter.Button(text="Calculate", command=calc_mile_kilo)
button.grid(row=2,column=1)

window.mainloop()
