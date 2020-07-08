import tkinter as tk
import sys
import os

from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep

from utils.characters import *
from utils.memory import *
from utils.moves import *


# --------------- CONSTANTS -------------- #

# Character Selected On Launch
DEFAULT_CHARACTER = "Bryan"

# Offsets
OFFSET_SIDE = 0x34C508C # WORKING AS OF 2020-07-02
OFFSET_INGAME = 0x34303F8 # WORKING AS OF 2020-07-06

# Settings
CHARACTERLIST = list(Roster.keys())
TRANSPARENTCOLOR = "green"
NULL = None


# --------------- MAIN GUI --------------- #


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Initial Setup
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "T7 Scripts")
        tk.Tk.configure(self, bg=TRANSPARENTCOLOR)

        # Geometry
        self.w = tk.Tk.winfo_screenwidth(self)
        self.h = tk.Tk.winfo_screenheight(self)
        tk.Tk.geometry(self, f"{self.w}x{self.h}")

        # Variables
        self.status = tk.StringVar(self,"ON")
        self.SIDE = tk.StringVar(self, "Left")
        self.varCharacters = tk.StringVar(self, f"{DEFAULT_CHARACTER}")

        # How to exit
        labelHelp = tk.Label(self, text="Press 'END' key to exit", fg="white", bg=TRANSPARENTCOLOR)
        labelHelp.configure(font=("Calibri", 14))
        labelHelp.place(x=10, y=5)

        # How to pause
        labelHelp = tk.Label(self, text="Press 'F5' to toggle", fg="white", bg=TRANSPARENTCOLOR)
        labelHelp.configure(font=("Calibri", 14))
        labelHelp.place(x=self.w//2 - 90, y=self.h*0.02)

        # Script Status
        labelStatus = tk.Label(self, text="Status: ", fg="white", bg=TRANSPARENTCOLOR)
        labelStatus.config(font=("Calibri", 18))
        labelStatus.place(x=self.w*0.38, y=self.h*0.125)
        varStatus = tk.Label(self, textvariable=self.status, fg='white', bg=TRANSPARENTCOLOR)
        varStatus.config(font=("Calibri", 18))
        varStatus.place(x=self.w*0.38 + 100, y=self.h*0.125)
        
        # Side Status
        labelSide = tk.Label(self, text="Side: ", fg="white", bg=TRANSPARENTCOLOR)
        labelSide.config(font=("Calibri", 18))
        labelSide.place(x=self.w*0.56, y=self.h*0.125)
        varSide = tk.Label(self, textvariable=self.SIDE, fg='white', bg=TRANSPARENTCOLOR)
        varSide.config(font=("Calibri", 18))
        varSide.place(x=self.w*0.56 + 70, y=self.h*0.125)

        # Character Menu
        menuCharacters = tk.OptionMenu(self, self.varCharacters, *CHARACTERLIST)
        menuCharacters.config(fg="white", bg=TRANSPARENTCOLOR)
        menuCharacters.config(font=("Calibri", 12))
        menuCharacters.place(x=self.w - 215, y=5)




# -------------- REGULAR FUNCTIONS -------------- #


def on_press(key) -> bool:
    """
    @rtype: bool
    @param: virtual_key
    @fn: Performs actions based on virtual
         pressed.
    """
    global app, Roster, CHAR, SIDE, ACTIVE, FOREGROUND
 
    if ACTIVE == 1 and FOREGROUND:
        if key == Key.shift_r:
            Roster[CHAR].right_shift[SIDE]()
    
        elif key == Key.ctrl_r:
            Roster[CHAR].right_control[SIDE]()

        elif key == Key.shift:
            Roster[CHAR].left_shift[SIDE]()

        elif key == Key.ctrl_l:
            Roster[CHAR].left_control[SIDE]()

    if key == Key.f5 and INGAME:
        if ACTIVE == 1:
            ACTIVE = -1
        else:
            ACTIVE = 1

    if key == Key.end or ACTIVE == 0:
        os._exit(1)
        return False

def Update() -> NULL:
    """
    @rtype: NULL
    @param: NULL
    @fn: Reads Tekken Memory to determine SIDE
         and updates SIDE/ACTIVE variables.
    """
    global processId, CHAR, SIDE, ACTIVE, FOREGROUND, INGAME
    while True:
        CHAR = app.varCharacters.get()
        
        # Side Logic
        if SIDE == 0 and INGAME:
            app.SIDE.set("LEFT")

        elif SIDE == 1 and INGAME:
            app.SIDE.set("RIGHT")

        else:
            app.SIDE.set("NONE")

        # Active Logic
        if ACTIVE == 1 and FOREGROUND:
            app.status.set("ON")

        elif ACTIVE == -1 or not FOREGROUND:
            ACTIVE = -1
            app.status.set("PAUSED")

        if ACTIVE == 0:
            os._exit(1)
            break

        SIDE = WhichSide(processHandle, BASEADDRESS, OFFSET_SIDE, DATA, bytesread=BYTESREAD)
        INGAME = IsIngame(processHandle, BASEADDRESS, OFFSET_INGAME, DATA)
        FOREGROUND = IsForeground(processId)

        sleep(0.25)
            
def nput() -> NULL:
    """
    @rtype: NULL
    @param: NULL
    @fn: Listens for key strokes.
    """
    with Listener(on_press=on_press) as listener:
        listener.join()
    

# ------------------- MAIN GUI ------------------ #


if __name__ == "__main__":

    ACTIVE = 1
    FOREGROUND = 0
    INGAME = 0
    CHAR = NULL
    SIDE = NULL

    processId = GetPid("TekkenGame-Win64-Shipping.exe")
    processHandle, BASEADDRESS, DATA, BYTESREAD = GetTekkenInfo()

    app = Main()
    nput = Thread(target=nput)
    update = Thread(target=Update)

    app.overrideredirect(1) # TOGGLE WINDOW FRAME
    app.call("wm", "attributes", ".", "-topmost", "1")
    app.wm_attributes("-transparentcolor", TRANSPARENTCOLOR)

    nput.start()
    update.start()
    app.mainloop()
