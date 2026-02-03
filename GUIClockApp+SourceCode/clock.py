# IMPORTS - TOOLBOX
from customtkinter import *
from tkinter import *
from time import *
import time
import ttkbootstrap as ttk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        self.root.style = ttk.Style(theme="darkly")
        
        # --------------------------------------------------------------------
        # OPTIONAL FEATURES
        # --------------------------------------------------------------------
        # # self.root.style = ttk.Style(theme="darkly")
        # # self.root.geometry("1200x250")
        # # self.root.resizable(False, False)
        # --------------------------------------------------------------------      
        
        # Create a time frame and label and pack it to the frame
        self.timeLabelFrame = Frame(master=root, pady=50, padx=20, bg="black")
        self.timeLabel = CTkLabel(self.timeLabelFrame, font=("Trebuchet MS", 150), text_color="green")
        self.dayLabel = CTkLabel(self.timeLabelFrame, font=("Cambria", 60),)
        self.timeLabel.pack()
        self.dayLabel.pack()
        
        # Create a frame for the button to make it bigger
        self.buttonFrame = Frame(master=root, background="#000000")
        # Create and pack the button in the frame
        self.exitButton = CTkButton(master=self.buttonFrame, text="EXIT", command=self.Exit,)
        self.exitButton.pack(fill="both")
        

        # pack labels to the screen
        self.timeLabelFrame.pack(expand=True, fill="both")
        # Pack the button and the frame
        self.buttonFrame.pack(fill="both")
        
        # call the updateTime function on the root window
        self.updateTime()
    
    def updateTime(self):
        timeString = strftime("%H:%M")
        self.timeLabel.configure(text=timeString)
        
        dayString = strftime("%A %B %d, %Y")
        self.dayLabel.configure(text=f"Date: {dayString}")

        self.root.after(500, self.updateTime)


    # Previous Code (Might be needed later)
    """
    def editTimeString(self):
        timeString = strftime("%H:%M")
        self.timeLabel.configure(text_color="green", bg_color="transparent", text=timeString)

        self.root.after(500, self.updateTime)
    """
    
    
    # create an exit function
    def Exit(self):
        print("Closing clock...")
        time.sleep(1.5)
        self.root.destroy()
        exit()



if __name__ == "__main__":
    window = CTk()
    app = App(window)
    print("App Running...")
    
    # run the app
    window.mainloop()