import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

root = tk.Tk()
root.title("GUI IN 4 QUADRANTS")
root.geometry("1920x1080")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

frame1 = tk.Frame(root, bg="black", bd=2, relief="groove")
frame2 = tk.Frame(root, bg="lightcoral", bd=2, relief="groove")
frame3 = tk.Frame(root, bg="black", bd=2, relief="groove")
frame4 = tk.Frame(root, bg="lightyellow", bd=2, relief="groove")

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")
frame3.grid(row=1, column=0, sticky="nsew")
frame4.grid(row=1, column=1, sticky="nsew")

tk.Label(frame1, text="Video").pack(expand=True)
# tk.Label(frame2, text="Section 2", bg="lightcoral").pack(expand=True)
tk.Label(frame3, text="Video").pack(expand=True)
# tk.Label(frame4, text="Section 4", bg="lightyellow").pack(expand=True)

frame4.grid_rowconfigure(0, weight=1)
frame4.grid_columnconfigure(0, weight=1)
log_text = ScrolledText(frame4, wrap="word", font=("Consolas", 12))
log_text.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    log_text.insert("end", f"[{ts}] {msg}\n")
    log_text.see("end")

for r in range(3):
    frame2.grid_rowconfigure(r, weight=1)
for c in range(3):
    frame2.grid_columnconfigure(c, weight=1)

up    = tk.Button(frame2, text="Up",    command=lambda: log("Up"))
left  = tk.Button(frame2, text="Left",  command=lambda: log("Left"))
right = tk.Button(frame2, text="Right", command=lambda: log("Right"))
down  = tk.Button(frame2, text="Down",  command=lambda: log("Down"))

up.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
left.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
right.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
down.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

center = tk.Frame(frame2, bg="lightcoral")
center.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
center.grid_columnconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

btn_play = tk.Button(center, text="Play", command=lambda: log("Play"))
btn_stop = tk.Button(center, text="Stop", command=lambda: log("Stop"))
btn_play.grid(row=0, column=0, sticky="nsew", padx=(0,5))
btn_stop.grid(row=0, column=1, sticky="nsew", padx=(5,0))

root.mainloop()