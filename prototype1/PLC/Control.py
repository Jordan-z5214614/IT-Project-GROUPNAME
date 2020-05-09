import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep

Turbine1 = 1
Turbine2 = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(Turbine1, GPIO.OUT)
GPIO.setup(Turbine2, GPIO.OUT)

m = tk.Tk()
m.title("Power Plant Control System")
m.geometry("200x100")

Turbine1_state = True
Turbine2_state = True

def Turbine1button():
    global Turbine1_state
    if Turbine1_state == True:
        GPIO.output(Turbine1, Turbine1_state)
        Turbine1_state = False
        on = tk.Label(m, text = "Running")
        on.grid(row = 0, column = 1)
    else:
        GPIO.output(Turbine1, Turbine1_state)
        Turbine1_state = True
        ON = tk.Label(m, text = "Powered Off")
        ON.grid(row = 0, column = 1)


def Turbine2button():
    global Turbine2_state
    if Turbine2_state == True:
        GPIO.output(Turbine2, Turbine2_state)
        Turbine2_state = False
        on1 = tk.Label(m, text = "Running")
        on1.grid(row = 1, column = 1)
    else:
        GPIO.output(Turbine2, Turbine2_state)
        Turbine2_state = True
        ON = tk.Label(m, text = "Powered Off")
        ON.grid(row = 1, column = 1)


ONbutton = tk.Button(m, text = "Turbine 1", bg="green", command=Turbine1button)
ONbutton.grid(row = 0, column = 0)

ON2button = tk.Button(m, text = "Turbine 2", bg="green", command=Turbine2button)
ON2button.grid(row = 1, column = 0)

Exitbutton = tk.Button(m, text = "Exit", bg = "red", command = m.destroy)
Exitbutton.grid(row = 2, column = 0)

m.mainloop()

