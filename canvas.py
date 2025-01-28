import math
import tkinter as tk
#find the distance between 2 points
def listen_button():
    if txtNum1.get()and txtNum2.get() and txtNum3.get() and txtNum4.get() :
        x1 =350 + int(txtNum1.get())
        y1 =350 + int(txtNum2.get())
        x2 =350 + int(txtNum3.get())
        y2 =350 + int(txtNum4.get())
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance = round(distance,2)
        lblAnswer.config(text=f"The distance between the two points is {distance}")
    else:
        lblAnswer.config(text=" Error you need to type 4 variables. ")
window = tk.Tk() # create a window
window.title("Slope intercept")
window.resizable(True, True)
#Making GUI elements
lblOne = tk.Label(window, text="x1: ")
lblTwo = tk.Label(window, text="y1: ")
lblThree = tk.Label(window, text="x2: ")
lblFour = tk.Label(window, text="y2: ")
lblAnswer =tk.Label(window, text="")
txtNum1 = tk.Entry(window)
txtNum2 = tk.Entry(window)
txtNum3 = tk.Entry(window)
txtNum4 = tk.Entry(window)
btnCalc = tk.Button(window, text="Calculate",command=listen_button)

#####Building the Grid
txtNum1.grid(row=0, column=0)
txtNum2.grid(row=0, column=1)
txtNum3.grid(row=0, column=2)
txtNum4.grid(row=0, column=3)
lblOne.grid(row=1, column=0)
lblTwo.grid(row=1, column=1)
lblThree.grid(row=1, column=2)
lblFour.grid(row=1, column=3)
btnCalc.grid(row=2, column=2)
lblAnswer.grid(row=3,column=0,columnspan = 5)

window.mainloop()

