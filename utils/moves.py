import ctypes

from time import sleep


# -------------- CONSTANTS --------------- #


U = 0x11
L = 0x1E
D = 0x1F
R = 0x20

ONE   = 0x16
TWO   = 0x17
THREE = 0x24
FOUR  = 0x25

KEYEVENTF_KEYUP    = 0x0002
KEYEVENTF_SCANCODE = 0x0008

PUL = ctypes.POINTER(ctypes.c_ulong)
SendInput = ctypes.windll.user32.SendInput


# -------- C STRUCT TRANSLATIONS --------- #


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# ------------ SIMULATED KEYS -------------- #


def Frame(N):
    const = 1/60
    sleep(N * const)

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, KEYEVENTF_SCANCODE, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


#  --------------- MOVELIST ----------------- #


def ewgf_L():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(R)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(R)
    ReleaseKey(TWO)
    Frame(35)

def ewgf_R():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(L)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(TWO)
    Frame(35)

def ew2f_L():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(R)
    PressKey(ONE)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(R)
    ReleaseKey(ONE)
    Frame(35)

def ew2f_R():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(L)
    PressKey(ONE)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(ONE)
    Frame(35)

def pewgf_L():
    PressKey(R)
    Frame(0.9)
    ReleaseKey(R)
    Frame(0.1)
    PressKey(D)
    Frame(0.9)
    PressKey(R)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(R)
    ReleaseKey(TWO)
    Frame(35)

def pewgf_R():
    PressKey(L)
    Frame(0.9)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    PressKey(L)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(TWO)
    Frame(35)

def dewgf_L():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(R)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(R)
    ReleaseKey(TWO)
    Frame(1)
 
def dewgf_R():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(L)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(TWO)
    Frame(1)   

# Mishimas
def lightdash_L():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(R)
    Frame(1)
    ReleaseKey(D)
    Frame(1)
    ReleaseKey(R)
    Frame(3)

def lightdash_R():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(L)
    Frame(1)
    ReleaseKey(D)
    Frame(1)
    ReleaseKey(L)
    Frame(3)

def wavedash_L():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(R)
    Frame(1)
    ReleaseKey(D)
    Frame(1)
    ReleaseKey(R)
    Frame(7)

def wavedash_R():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    Frame(1)
    PressKey(L)
    Frame(1)
    ReleaseKey(D)
    Frame(1)
    ReleaseKey(L)
    Frame(7)

def kbd_L():
    Frame(1)
    PressKey(L)
    Frame(7)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    PressKey(L)
    Frame(1)
    ReleaseKey(D)
    Frame(2)
    ReleaseKey(L)

def kbd_R():
    Frame(1)
    PressKey(R)
    Frame(7)
    ReleaseKey(R)
    Frame(1)
    PressKey(D)
    PressKey(R)
    Frame(1)
    ReleaseKey(D)
    Frame(2)
    ReleaseKey(R)

# Bryan
def tauntJetUpper_L():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(ONE)
    PressKey(THREE)
    PressKey(FOUR)
    Frame(1)
    ReleaseKey(ONE)
    ReleaseKey(THREE)
    ReleaseKey(FOUR)
    Frame(27)
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(L)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(L)
    ReleaseKey(TWO)

def tauntJetUpper_R():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(ONE)
    PressKey(THREE)
    PressKey(FOUR)
    Frame(1)
    ReleaseKey(ONE)
    ReleaseKey(THREE)
    ReleaseKey(FOUR)
    Frame(27)
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(R)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(R)
    ReleaseKey(TWO)

# Heihachi
def otgf_L():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(D)
    PressKey(R)
    PressKey(ONE)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(R)
    ReleaseKey(ONE)
    Frame(51)

def otgf_R():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(D)
    PressKey(L)
    PressKey(ONE)
    Frame(1)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(ONE)
    Frame(51)

# Nina Williams
def butterfly_L():
    PressKey(D)
    Frame(0.9)
    PressKey(R)
    Frame(0.9)
    ReleaseKey(D)
    Frame(0.9)
    PressKey(U)
    PressKey(ONE)
    Frame(1)
    ReleaseKey(U)
    ReleaseKey(R)
    ReleaseKey(ONE)
    Frame(35)

def butterfly_R():
    PressKey(D)
    Frame(1)
    PressKey(L)
    Frame(1)
    ReleaseKey(D)
    Frame(1)
    PressKey(U)
    PressKey(ONE)
    Frame(1)
    ReleaseKey(U)
    ReleaseKey(L)
    ReleaseKey(ONE)
    Frame(37)

def generic_one_plus_four():
    PressKey(ONE)
    PressKey(FOUR)
    Frame(1)
    ReleaseKey(ONE)
    ReleaseKey(FOUR)

def generic_one_plus_two():
    PressKey(ONE)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(ONE)
    ReleaseKey(TWO)

def generic_two_plus_three():
    PressKey(TWO)
    PressKey(THREE)
    Frame(1)
    ReleaseKey(TWO)
    ReleaseKey(THREE)

def generic_three_plus_four():
    PressKey(THREE)
    PressKey(FOUR)
    Frame(1)
    ReleaseKey(THREE)
    ReleaseKey(FOUR)

# Lee Chaolan
def mist_trap():
    PressKey(THREE)
    Frame(1)
    ReleaseKey(THREE)
    Frame(1)
    PressKey(THREE)
    Frame(1)
    ReleaseKey(THREE)
    Frame(27.69)
    PressKey(FOUR)
    Frame(1)
    ReleaseKey(FOUR)
    Frame(1)

def acid_rain():
    PressKey(ONE)
    Frame(10)
    ReleaseKey(ONE)
    PressKey(THREE)
    Frame(1)
    ReleaseKey(THREE)
    Frame(13)
    PressKey(THREE)
    Frame(1)
    ReleaseKey(THREE)
    Frame(9)
    PressKey(THREE)
    Frame(1)
    ReleaseKey(THREE)

def b2_L():
    PressKey(L)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(L)
    ReleaseKey(TWO)
    Frame(3)
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(7)

def b2_R():
    PressKey(R)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(R)
    ReleaseKey(TWO)
    Frame(3)
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(7)

def iwr2_L():
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(R)
    Frame(1)
    ReleaseKey(R)
    Frame(1)
    PressKey(R)
    Frame(1)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(R)
    ReleaseKey(TWO)

def iwr2_R():
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(L)
    Frame(1)
    ReleaseKey(L)
    Frame(1)
    PressKey(L)
    Frame(1)
    PressKey(TWO)
    Frame(1)
    ReleaseKey(L)
    ReleaseKey(TWO)    
