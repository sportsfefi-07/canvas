import math
import tkinter as tk





# Draw a diagonal line from top-left to bottom-right

m = 10
x = 70
b = 60
y = m*x+b
print (y)


window = tk.Tk() # create a window
window.title("Slope intercept")
window.geometry("1500x1500") # set the window size
window.resizable(True, True) #
canvas = tk.Canvas(window, width=1000, height=1000)



def listen_button():
    x1 =350 + int(txtNum1.get())
    y1 =350 + int(txtNum2.get())
    x2 =350 + int(txtNum3.get())
    y2 =350 + int(txtNum4.get())
    canvas.create_line(x1, y1, x2, y2)


lblOne = tk.Label(window, text="x1: ")
lblTwo = tk.Label(window, text="y1: ")
lblThree = tk.Label(window, text="x2: ")
lblFour = tk.Label(window, text="y2: ")
lblFive = tk.Label(window, text="slope: ")
lblSix = tk.Label(window, text="y intercept: ")

txtNum1 = tk.Entry(window)
txtNum2 = tk.Entry(window)
txtNum3 = tk.Entry(window)
txtNum4 = tk.Entry(window)
txtNum5 = tk.Entry(window)
txtNum6 = tk.Entry(window)

btnCalc = tk.Button(window, text="Calculate",command=listen_button)
#vertical line
canvas.create_line(250,800,250,400)
#horizintal line
canvas.create_line(0,500,500,500)




#####Building the Grid
txtNum1.grid(row=0, column=0)
txtNum2.grid(row=0, column=1)
txtNum3.grid(row=0, column=2)
txtNum4.grid(row=0, column=3)
txtNum5.grid(row=0, column=4)
txtNum6.grid(row=0, column=5)
lblOne.grid(row=1, column=0)
lblTwo.grid(row=1, column=1)
lblThree.grid(row=1, column=2)
lblFour.grid(row=1, column=3)
lblFive.grid(row=1, column=4)
lblSix.grid(row=1, column=5)
btnCalc.grid(row=2, column=0)
canvas.grid(row=3, column=4)

window.mainloop()

