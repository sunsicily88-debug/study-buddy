import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("Study Buddy")
window.geometry("420x520")

# Variables
time_left = 25 * 60
running = False
mode = "study"


# Show time on screen
def show_time():
    minutes = time_left // 60
    seconds = time_left % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")


# Update countdown
def update_timer():
    global time_left, running, mode

    if not running:
        return

    if time_left > 0:
        time_left -= 1
        show_time()
        window.after(1000, update_timer)

    else:
        running = False

        # Study finished
        if mode == "study":
            messagebox.showinfo(
                "Study Buddy",
                "Time for a break!"
            )

            mode = "break"
            time_left = 5 * 60

            study_label.config(text="Break Time")
            message_label.config(text="Relax for a few minutes!")
            show_time()

        # Break finished
        else:
            messagebox.showinfo(
                "Study Buddy",
                "Time to study!"
            )

            mode = "study"
            set_study_time()
            message_label.config(text="Stay focused!")


# Start
def start_timer():
    global running

    if not running:
        running = True
        window.after(1000, update_timer)


# Pause
def pause_timer():
    global running
    running = False


# Set study time
def set_study_time():
    global time_left, running, mode

    try:
        minutes = int(time_entry.get())

        if minutes <= 0:
            messagebox.showerror(
                "Error",
                "Please enter a number greater than 0."
            )
            return

        running = False
        mode = "study"
        time_left = minutes * 60

        study_label.config(text="Study Time")
        message_label.config(text="Stay focused!")
        show_time()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a number."
        )


# Reset
def reset_timer():
    set_study_time()


# Title
title = tk.Label(
    window,
    text="Study Buddy",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)


# Input label
input_label = tk.Label(
    window,
    text="Enter study time (minutes):",
    font=("Arial", 13)
)
input_label.pack(pady=5)


# Input box
time_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=10,
    justify="center"
)
time_entry.insert(0, "25")
time_entry.pack(pady=5)


# Set Time button
set_button = tk.Button(
    window,
    text="Set Time",
    command=set_study_time
)
set_button.pack(pady=5)


# Study / Break label
study_label = tk.Label(
    window,
    text="Study Time",
    font=("Arial", 16)
)
study_label.pack(pady=10)


# Timer
timer_label = tk.Label(
    window,
    text="25:00",
    font=("Arial", 40, "bold")
)
timer_label.pack(pady=15)


# Message
message_label = tk.Label(
    window,
    text="Stay focused!",
    font=("Arial", 12)
)
message_label.pack(pady=5)


# Button area
button_frame = tk.Frame(window)
button_frame.pack(pady=10)


# Start button
start_button = tk.Button(
    button_frame,
    text="Start",
    width=8,
    command=start_timer
)
start_button.grid(row=0, column=0, padx=5)


# Pause button
pause_button = tk.Button(
    button_frame,
    text="Pause",
    width=8,
    command=pause_timer
)
pause_button.grid(row=0, column=1, padx=5)


# Reset button
reset_button = tk.Button(
    button_frame,
    text="Reset",
    width=8,
    command=reset_timer
)
reset_button.grid(row=0, column=2, padx=5)


window.mainloop()