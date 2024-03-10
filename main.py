import tkinter as tk
import pyautogui
import time

exame = ""

def execute_automation():
    global value
    value = entry.get()
   
    print("Automation executed with value:", value)
    root.withdraw()  # Esconde a janela principal
    show_options_window()

def show_options_window():
    options_window = tk.Toplevel()
    options_window.title("Choose an Option")

    label = tk.Label(options_window, text="Choose an option:")
    label.pack()

    button1 = tk.Button(options_window, text="Panorâmica", command=lambda: option_selected("Panorâmica"))
    button1.pack()

    button2 = tk.Button(options_window, text="Telleradiografia", command=lambda: option_selected("Telleradiografia"))
    button2.pack()

    # Centraliza a janela de opções
    x = (options_window.winfo_screenwidth() - options_window.winfo_reqwidth()) / 2
    y = (options_window.winfo_screenheight() - options_window.winfo_reqheight()) / 2
    options_window.geometry("+%d+%d" % (x, y))

def option_selected(option):
    global exame
    exame = option
    print("Option selected:", exame)

    if exame == "Panorâmica":
        print("pano")
    elif exame == "Telleradiografia":
        print("tele")
    root.destroy()

root = tk.Tk()
root.title("Automation Input")

label = tk.Label(root, text="Enter a value:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Execute Automation", command=execute_automation)
button.pack()

# Centraliza a janela principal
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))

root.mainloop()

# Restante do código
pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("template")
pyautogui.press("enter")


time.sleep(3)

print(pyautogui.position())
pyautogui.click(x = 86, y = 203)
pyautogui.write(value)
#pyautogui.click()
#pyautogui.click()
#pyautogui.click()







