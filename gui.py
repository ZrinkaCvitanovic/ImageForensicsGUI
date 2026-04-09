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
            ent_ela_in.delete(0, tk.END)
            ent_ela_q.delete(0, tk.END)
    except ValueError:
        lbl_ela_msg["text"] ="Quality value must be an integer!"

def event_color(event):
    in_image = ent_color_in.get()
    method = opt_color_method.get()
    if method != "lum" and method != "hsv":
        lbl_color_msg["text"] ="Unsupported choice of method. Choose 'lum' or 'hsv!"
        print("method: ", method)
    else: 
        lbl_color_msg["text"] ="Success!"
        subprocess.run(['python3', 'detection/change-color-scheme/main.py', in_image, method])
        ent_color_in.delete(0, tk.END)
        #ent_color_method.delete(0, tk.END)

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
        ent_edge_in.delete(0, tk.END)
        ent_edge_lower.delete(0, tk.END)
        ent_edge_higher.delete(0, tk.END)
    except ValueError:
        lbl_edge_msg["text"] ="Lower and higher threshold values must be numbers!"
        

def event_telea(event):
    in_image = ent_telea_in.get()
    mask_image = ent_telea_mask.get()
    radius = ent_telea_radius.get()
    try:
        radius_int = int(radius)
        lbl_telea_msg["text"] ="Success!"
        subprocess.run(['python3', 'reconstruction/pyhealtelea/main.py', '-r', radius, in_image, mask_image])
        ent_telea_in.delete(0, tk.END)
        ent_telea_mask.delete(0, tk.END)
        ent_telea_radius.delete(0, tk.END)
    except:
        lbl_telea_msg["text"] ="Radius must be a number!"
    


def event_patch(event):
    in_image = ent_patch_in.get()
    mask_image = ent_patch_mask.get()
    color = opt_patch_maskc.get()
    if color != "white" and color != "black" and color != "blue" and color != "green" and color != "red":
        lbl_patch_msg["text"] = "Mask color must be white, black, blue, green or red."
    else:
        lbl_patch_msg["text"] ="Success!"
        subprocess.run(['python3', 'reconstruction/PatchMatchInpainting/main.py', in_image, mask_image, color])
        ent_patch_in.delete(0, tk.END)
        ent_patch_mask.delete(0, tk.END)

def event_resize(event):
    in_image = ent_resize_in.get()
    height_scale = ent_resize_height.get()
    width_scale = ent_resize_width.get()
    method = opt_resize_method.get()

    try:
        height = int(height_scale)
        width = int(width_scale)
        if method != "cubic" and method != "lanzos" and method != "linear":
            lbl_resize_msg["text"] = "Supported choices are cubic, lanzos and linear."
        else:
            lbl_resize_msg["text"] ="Success!"
            subprocess.run(['python3', 'reconstruction/enhancement/resize/resize.py', in_image, height_scale, width_scale, method])
            ent_resize_in.delete(0, tk.END)
            ent_resize_height.delete(0, tk.END)
            ent_resize_width.delete(0, tk.END)
    except:
        lbl_resize_msg["text"] = "Height and width scale must be numbers!"

def event_noise(event):
    in_image = ent_noise_in.get()
    method = opt_noise_method.get()
    if method != "gaussian" and method != "median":
        lbl_noise_msg["text"] = "Supported choices for method are gaussian and median"
    else:
        lbl_noise_msg["text"] ="Success!"
        subprocess.run(['python3', 'reconstruction/enhancement/noise/denoising.py', in_image, method])
        ent_noise_in.delete(0, tk.END)

def event_sharp(event):
    in_image = ent_sharp_in.get()
    method = opt_sharp_method.get()
    if method != "histogram" and method != "kernel" and method != "laplacian":
        lbl_sharp_msg["text"] = "Supported choices for method are histogram, kernel or laplacian"
    else:
        if method == "histogram":
                subprocess.run(['python3', 'reconstruction/enhancement/sharpen/histogram.py', in_image])
        else:
            subprocess.run(['python3', 'reconstruction/enhancement/sharpen/sharpen.py', in_image, method])            
        lbl_sharp_msg["text"] ="Success!"
        ent_sharp_in.delete(0, tk.END)

 
    

tabControl.add(tab1, text ='Welcome page')
#TODO: add text explanations for all used algorithms


tabControl.add(tab2, text ='Detect image manipulation')

lbl_ela_title = tk.Label(tab2, text ="Error Level Analysis")
lbl_ela_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_ela_title.grid( row = 0, column = 0, sticky="w")
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

lbl_color_title = tk.Label(tab2, text ="Change Color Scheme")
lbl_color_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_color_title.grid(row = 10, column = 0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=11, column=0, sticky="w")
tk.Label(tab2, text="Desired method", width=50).grid(row=12, column=0, sticky="w")

ent_color_in = tk.Entry(tab2, width=100)
ent_color_in.grid(row=11, column=1, sticky="w")
#ent_color_method = tk.Entry(tab2, width=5)
#ent_color_method.grid(row=12, column=1, sticky="w")
opt_color_method = tk.StringVar(value="hsv")
opt_color_dropdown = tk.OptionMenu(tab2, opt_color_method, "hsv", "lum")
opt_color_dropdown.grid(row=12, column=1, sticky="w")
btn_color = tk.Button(tab2, text='Start')
btn_color.bind('<Button>', event_color)
btn_color.grid(row=13, column=1, sticky="w")
lbl_color_msg = tk.Label(tab2, text="")
lbl_color_msg.grid(row=14, column=1)

lbl_edge_title = tk.Label(tab2, text ="Edge detection")
lbl_edge_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_edge_title.grid(column = 0, row = 20, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=21, column=0, sticky="w")
tk.Label(tab2, text="Lower threshold", width=50).grid(row=22, column=0, sticky="w")
tk.Label(tab2, text="Higher threshold", width=50).grid(row=23, column=0, sticky="w")
robust_pressed = tk.IntVar()
tk.Checkbutton(tab2, text="Robust", variable=robust_pressed, onvalue=1,
                        offvalue=0).grid(column=1, row=24, sticky="w")
ent_edge_in = tk.Entry(tab2, width=100)
ent_edge_in.grid(row=21, column=1, sticky="w")
ent_edge_lower = tk.Entry(tab2, width=5)
ent_edge_lower.grid(row=22, column=1, sticky="w")
ent_edge_higher = tk.Entry(tab2, width=5)
ent_edge_higher.grid(row=23, column=1, sticky="w")
btn_edge = tk.Button(tab2, text='Start')
btn_edge.bind('<Button>', event_edge)
btn_edge.grid(row=25, column=1, sticky="w")
lbl_edge_msg = tk.Label(tab2, text="")
lbl_edge_msg.grid(row=26, column=1)



tabControl.add(tab3, text ='Restore images')

lbl_telea_title = tk.Label(tab3, text ="Telea inpainting")
lbl_telea_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_telea_title.grid(row=0, column=0, sticky="w")
tk.Label(tab3, text="Input image", width=50).grid(row=1, column=0, sticky="w")
tk.Label(tab3, text="Mask image", width=50).grid(row=2, column=0, sticky="w")
tk.Label(tab3, text="Neighbourhood radius", width=50).grid(row=3, column=0, sticky="w")
ent_telea_in = tk.Entry(tab3, width=100)
ent_telea_in.grid(row=1, column=1, sticky="w")
ent_telea_mask = tk.Entry(tab3, width=100)
ent_telea_mask.grid(row=2, column=1, sticky="w")
ent_telea_radius = tk.Entry(tab3, width=5)
ent_telea_radius.grid(row=3, column=1, sticky="w")
ent_telea_radius.insert(0, 5)
btn_telea = tk.Button(tab3, text='Start')
btn_telea.bind('<Button>', event_telea)
btn_telea.grid(row=4, column=1, sticky="w")
lbl_telea_msg = tk.Label(tab3, text="")
lbl_telea_msg.grid(row=5, column=1)

lbl_patch_title = tk.Label(tab3, text ="PatchMatch inpainting")
lbl_patch_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_patch_title.grid(row=10, column=0, sticky="w")
tk.Label(tab3, text="Input image", width=50).grid(row=11, column=0, sticky="w")
tk.Label(tab3, text="Mask image", width=50).grid(row=12, column=0, sticky="w")
tk.Label(tab3, text="Mask color", width=50).grid(row=13, column=0, sticky="w")
#tk.Label(tab3, text="Pyramid/single", width=50).grid(row=14, column=0, sticky="w")   TODO
ent_patch_in = tk.Entry(tab3, width=100)
ent_patch_in.grid(row=11, column=1, sticky="w")
ent_patch_mask = tk.Entry(tab3, width=100)
ent_patch_mask.grid(row=12, column=1, sticky="w")
opt_patch_maskc = tk.StringVar(value="white")
opt_patch_dropdown = tk.OptionMenu(tab3, opt_patch_maskc, "white", "black", "red", "green", "blue")
opt_patch_dropdown.grid(row=13, column=1, sticky="w")
#ent_patch_method = tk.Entry(tab3, width=100)                                        TODO
#ent_patch_method.grid(row=14, column=1, sticky="w")
btn_patch = tk.Button(tab3, text='Start')
btn_patch.bind('<Button>', event_patch)
btn_patch.grid(row=15, column=1, sticky="w")
lbl_patch_msg = tk.Label(tab3, text="")
lbl_patch_msg.grid(row=16, column=1)

lbl_resize_title = tk.Label(tab3, text ="Image resizing")
lbl_resize_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_resize_title.grid(row=20, column=0, sticky="w")
tk.Label(tab3, text="Input image", width=50).grid(row=21, column=0, sticky="w")
tk.Label(tab3, text="Height scale", width=50).grid(row=22, column=0, sticky="w")
tk.Label(tab3, text="Width scale", width=50).grid(row=23, column=0, sticky="w")
tk.Label(tab3, text="Method", width=50).grid(row=24, column=0, sticky="w")
ent_resize_in = tk.Entry(tab3, width=100)
ent_resize_in.grid(row=21, column=1, sticky="w")
ent_resize_height = tk.Entry(tab3, width=5)
ent_resize_height.grid(row=22, column=1, sticky="w")
ent_resize_width = tk.Entry(tab3, width=5)
ent_resize_width.grid(row=23, column=1, sticky="w")
opt_resize_method = tk.StringVar(value="cubic")
opt_resize_dropdown = tk.OptionMenu(tab3, opt_resize_method, "cubic", "lanzos", "linear")
opt_resize_dropdown.grid(row=24, column=1, sticky="w")
btn_resize = tk.Button(tab3, text='Start')
btn_resize.bind('<Button>', event_resize)
btn_resize.grid(row=25, column=1, sticky="w")
lbl_resize_msg = tk.Label(tab3, text="")
lbl_resize_msg.grid(row=26, column=1)

lbl_noise_title = tk.Label(tab3, text ="Removing noise from images")
lbl_noise_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_noise_title.grid(row=30, column=0, sticky="w")
tk.Label(tab3, text="Input image", width=50).grid(row=31, column=0, sticky="w")
tk.Label(tab3, text="Method", width=50).grid(row=32, column=0, sticky="w")
ent_noise_in = tk.Entry(tab3, width=100)
ent_noise_in.grid(row=31, column=1, sticky="w")
opt_noise_method = tk.StringVar(value="gaussian")
opt_noise_dropdown = tk.OptionMenu(tab3, opt_noise_method, "gaussian", "median")
opt_noise_dropdown.grid(row=32, column=1, sticky="w")
btn_noise = tk.Button(tab3, text='Start')
btn_noise.bind('<Button>', event_noise)
btn_noise.grid(row=33, column=1, sticky="w")
lbl_noise_msg = tk.Label(tab3, text="")
lbl_noise_msg.grid(row=34, column=1)

lbl_sharp_title = tk.Label(tab3, text ="Sharpening images")
lbl_sharp_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_sharp_title.grid(row=40, column=0, sticky="w")
tk.Label(tab3, text="Input image", width=50).grid(row=41, column=0, sticky="w")
tk.Label(tab3, text="Method", width=50).grid(row=42, column=0, sticky="w")
ent_sharp_in = tk.Entry(tab3, width=100)
ent_sharp_in.grid(row=41, column=1, sticky="w")
opt_sharp_method = tk.StringVar(value="histogram")
opt_sharp_dropdown = tk.OptionMenu(tab3, opt_sharp_method, "histogram", "kernel", "laplacian")
opt_sharp_dropdown.grid(row=42, column=1, sticky="w")
btn_sharp = tk.Button(tab3, text='Start')
btn_sharp.bind('<Button>', event_sharp)
btn_sharp.grid(row=43, column=1, sticky="w")
lbl_sharp_msg = tk.Label(tab3, text="")
lbl_sharp_msg.grid(row=44, column=1)




root.mainloop()