import tkinter
import tkinter.dialog
import tkinter.dnd as dnd
import tkinter.filedialog
import tkinter.messagebox
import sounddevice as sd
import soundfile as sf


MOUSE_DOWN = "<ButtonPress-1>"
MOUSE_UP = "<ButtonRelease-1>"
MOUSE_MOVEMENT = "<B1-Motion>"
MOUSE_DOUBLE_CLICK = "<Double-Button-1>"


def drag_start(event):
    widget = event.widget
    widget.drag_start = (event.x, event.y)
    dnd.dnd_start(widget, event)

def drag_motion(event):
    widget = event.widget
    drag_start_x, drag_start_y = widget.drag_start
    x = widget.winfo_x() - drag_start_x + event.x
    y = widget.winfo_y() - drag_start_y + event.y
    widget.place(x=x, y=y)



tk = tkinter.Tk()

def make_label(event):
    text = tkinter.messagebox.askquestion(title="Create Label", message="Enter label:")
    label = tkinter.Label(tk, name='test', text=text)
    label.pack()
    label.bind(MOUSE_DOWN, drag_start)
    label.bind(MOUSE_MOVEMENT, drag_motion)
    label.dnd_end = lambda *_: None
    tk.bind(MOUSE_UP)

def play_audio():
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
    if file_path:
        data, fs = sf.read(file_path)
        sd.play(data, fs)

def pause_audio():
    sd.stop()


play_button = tkinter.Button(tk, text="Select & Play", command=play_audio)
play_button.pack(side="bottom")
pause_button = tkinter.Button(tk, text="Pause", command=play_audio)
pause_button.pack(side="bottom", before=play_button)

tk.bind(MOUSE_DOUBLE_CLICK, make_label)
tk.mainloop()
