import pyautogui
import time
import tkinter as tk
from threading import Thread

# Función que mueve el ratón
def move_mouse():
    global running
    while running:
        pyautogui.moveRel(60, 60, duration=0.5)
        pyautogui.moveRel(-60, -60, duration=0.5)
        time.sleep(10)

# Función para iniciar el movimiento del ratón
def start_moving():
    global running
    running = True
    t = Thread(target=move_mouse)
    t.start()

# Función para detener el movimiento del ratón
def stop_moving():
    global running
    running = False

# GUI
app = tk.Tk()
app.title("Control del Ratón")

start_button = tk.Button(app, text="Iniciar", command=start_moving)
start_button.pack(pady=25)

stop_button = tk.Button(app, text="Detener", command=stop_moving)
stop_button.pack(pady=25)

app.mainloop()
