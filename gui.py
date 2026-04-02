import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.pack(expand = 1, fill ="both")

def event_ela(event):
    in_image = ent_ela_in.get()
    try:
        quality = int(ent_ela_q.get())
        if quality < 0 or quality > 100:
            lbl_ela_msg["text"] ="Quality must be an integer between 0 and 100!"
        else: 
            lbl_ela_msg["text"] ="Success!"
            subprocess.run(['python3', 'detection/ela/main.py', in_image, str(quality)])
    except ValueError:
        lbl_ela_msg["text"] ="Quality value must be an integer!"
    finally:
        ent_ela_in.delete(0, tk.END)
        ent_ela_q.delete(0, tk.END)

def event_color(event):
    in_image = ent_color_in.get()
    method = ent_color_method.get()
    if method != "lum" and method != "hsv":
        lbl_color_msg["text"] ="Unsupported choice of method. Choose 'lum' or 'hsv!"
    else: 
        lbl_color_msg["text"] ="Success!"
        subprocess.run(['python3', 'detection/change-color-scheme/main.py', in_image, method])

    ent_color_in.delete(0, tk.END)
    ent_color_method.delete(0, tk.END)

def event_edge(event):
    in_image = ent_edge_in.get()
    try:
        lower = int(ent_edge_lower.get())
        higher = int(ent_edge_higher.get())
        if (robust_pressed.get() == 1):
            subprocess.run(['python3', 'detection/edges/main.py', "--robust", in_image, str(lower), str(higher)])

        else:
            subprocess.run(['python3', 'detection/edges/main.py', in_image, str(lower), str(higher)])

        lbl_edge_msg["text"] ="Success!"
    except ValueError:
        lbl_ela_msg["text"] ="Quality value must be an integer!"
    finally:
        ent_ela_in.delete(0, tk.END)
        ent_ela_q.delete(0, tk.END)

tabControl.add(tab1, text ='Welcome page')
#TODO: add text explanations for all used algorithms


tabControl.add(tab2, text ='Detect image manipulation')

tk.Label(tab2, text ="Error Level Analysis").grid(column = 0, row = 0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=1, column=0, sticky="w")
tk.Label(tab2, text="Desired quality", width=50).grid(row=2, column=0, sticky="w")
ent_ela_in = tk.Entry(tab2, width=100)
ent_ela_in.grid(row=1, column=1, sticky="w")
ent_ela_q = tk.Entry(tab2, width=5)
ent_ela_q.grid(row=2, column=1, sticky="w")
btn_ela = tk.Button(tab2, text='Start')
btn_ela.bind('<Button>', event_ela)
btn_ela.grid(row=3, column=1, sticky="w")
lbl_ela_msg = tk.Label(tab2, text="")
lbl_ela_msg.grid(row=4, column=1)

tk.Label(tab2, text ="Change Color Scheme").grid(column = 0, row = 6, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=7, column=0, sticky="w")
tk.Label(tab2, text="Desired method (luminence or HSV)", width=50).grid(row=8, column=0, sticky="w")
ent_color_in = tk.Entry(tab2, width=100)
ent_color_in.grid(row=7, column=1, sticky="w")
ent_color_method = tk.Entry(tab2, width=5)
ent_color_method.grid(row=8, column=1, sticky="w")
btn_color = tk.Button(tab2, text='Start')
btn_color.bind('<Button>', event_color)
btn_color.grid(row=9, column=1, sticky="w")
lbl_color_msg = tk.Label(tab2, text="")
lbl_color_msg.grid(row=10, column=1)

tk.Label(tab2, text ="Edge detection").grid(column = 0, row = 12, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=13, column=0, sticky="w")
tk.Label(tab2, text="Lower threshold", width=50).grid(row=14, column=0, sticky="w")
tk.Label(tab2, text="Higher threshold", width=50).grid(row=15, column=0, sticky="w")
robust_pressed = tk.IntVar()
tk.Checkbutton(tab2, text="Robust", variable=robust_pressed, onvalue=1,
                        offvalue=0).grid(column=0, row=16, sticky="w")
ent_edge_in = tk.Entry(tab2, width=100)
ent_edge_in.grid(row=13, column=1, sticky="w")
ent_edge_lower = tk.Entry(tab2, width=5)
ent_edge_lower.grid(row=14, column=1, sticky="w")
ent_edge_higher = tk.Entry(tab2, width=5)
ent_edge_higher.grid(row=15, column=1, sticky="w")

btn_edge = tk.Button(tab2, text='Start')
btn_edge.bind('<Button>', event_edge)
btn_edge.grid(row=17, column=1, sticky="w")
lbl_edge_msg = tk.Label(tab2, text="")
lbl_edge_msg.grid(row=18, column=1)



tabControl.add(tab3, text ='Restore images')

# Widgets are added here

root.mainloop()