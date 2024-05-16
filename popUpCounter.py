import tkinter as tk
import signal

def on_top():
    top = tk.Toplevel(root)
    top.geometry("230x80+20+70")  # Set position 100px away from the left side and 100px down from the top
    top.attributes("-topmost", True)
    top.title("Popup Menu")

    counter = tk.IntVar()
    counter.set(0)

    def increase_counter():
        counter.set(counter.get() + 1)
        if counter.get() < 100:
            label.config(text="Total Form(s) submitted: " + str(counter.get()))
            top.after(100, increase_counter)

    def handle_interrupt(signum, frame):
        top.destroy()  # Close the popup window when interrupted
        root.quit()    # Exit the main loop

    def on_close():
        top.destroy()  # Close the popup window when the close button is clicked
        root.quit()    # Exit the main loop

    label = tk.Label(top, text="Total Form(s) submitted: " + str(counter.get()), font=("Helvetica", 13))
    label.pack(pady=20)

    increase_counter()

    signal.signal(signal.SIGINT, handle_interrupt)  # Register the signal handler for Ctrl+C

    top.protocol("WM_DELETE_WINDOW", on_close)  # Handle window close event

root = tk.Tk()
root.withdraw()  # Hide the main window
on_top()
try:
    root.mainloop()
except KeyboardInterrupt:
    root.quit()  # Exit gracefully when Ctrl+C is pressed
