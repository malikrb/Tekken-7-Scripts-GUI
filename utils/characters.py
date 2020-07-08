from .moves import * # comment for debug
# from moves import * # uncomment for debug

# -------------- CONTSTANTS --------------- #


NOP = lambda: 0 # No Operation


# -------------- CHARACTER ---------------- #


class Character:
    def __init__(self,  lc=(NOP, NOP),
                        rc=(NOP, NOP),
                        ls=(NOP, NOP),
                        rs=(NOP, NOP)):
        self.left_control  = (lc[0], lc[1])
        self.right_control = (rc[0], rc[1])
        self.left_shift    = (ls[0], ls[1])
        self.right_shift   = (rs[0], rs[1])

Roster = {
    "NONE": Character(), 

    "Generic": Character(
            lc=(generic_two_plus_three, generic_two_plus_three),
            rc=(generic_one_plus_four, generic_one_plus_four),
            ls=(generic_three_plus_four, generic_three_plus_four),
            rs=(generic_one_plus_two, generic_one_plus_two),
    ),

    "Bryan": Character(
            lc=(tauntJetUpper_L, tauntJetUpper_R),
            rc=(NOP, NOP),
            ls=(generic_three_plus_four, generic_three_plus_four),
            rs=(generic_one_plus_two, generic_one_plus_two)
    ),

    "Heihachi": Character(
            lc=(otgf_L, otgf_R),
            rc=(ewgf_L, ewgf_R),
            ls=(kbd_L, kbd_R),
            rs=(lightdash_L, lightdash_R)
    ),

    "Lee": Character(
            lc=(acid_rain, acid_rain),
            rc=(NOP, NOP),
            ls=(kbd_L, kbd_R),
            rs=(b2_L, b2_R)
    ),

    "Nina": Character(
            lc=(generic_two_plus_three, generic_two_plus_three),
            rc=(generic_one_plus_four, generic_one_plus_four),
            ls=(kbd_L, kbd_R),
            rs=(butterfly_L, butterfly_R)
    ),
    
    
}


# ------------- DEBUG ------------ #


if __name__ == "__main__":
    hei = Roster["Heihachi"]
    nina = Roster["Nina"]
    none = Character()

