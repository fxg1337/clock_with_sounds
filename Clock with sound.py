
import tkinter as tk
import time
import winsound

def update_clock():
    current_time = time.time()
    milliseconds = int((current_time - int(current_time)) * 1000)
    current_time = time.localtime(current_time)
    hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

    clock_display = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    label.config(text=clock_display)
    
    if int(seconds) == 0 and int(milliseconds) < 300:
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        
        
 
    # Schedule the function to run after 1 millisecond
    root.after(1, update_clock)
   

# Create the main window
root = tk.Tk()
root.title("Millisecond Clock")
root.resizable(width=False, height=False)

# Create a label for displaying the clock
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='yellow')
label.pack(anchor='center')

# Start the clock update
update_clock()
    

# Run the Tkinter event loop
root.mainloop()
