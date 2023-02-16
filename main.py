import tkinter


def calc_mile_kilo():
    miles = number.get()
    miles = float(miles)
    result = miles * 1.609
    label['text'] = f"Kilometers = {result}"

window = tkinter.Tk()
label = tkinter.Label(text="I will convert miles to kilometers. Provide a number below to calculate it to Kilometer")
button = tkinter.Button(text="Calculate", command=calc_mile_kilo)
number = tkinter.Entry()
label.pack()
button.pack()
number.pack()

window.mainloop()
