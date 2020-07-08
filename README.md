# Tekken 7 Script GUI
*By: Malik R. Booker  
Created: June 30, 2020  
Last Updated: July 3, 2020*
  
  
## Overview and Demonstration
The purpose of this program is so that the user can  
**simulate multiple keystrokes with a single button.**  
This program was entirely built on python and primarily  
utilizes **ctypes**, and **pymem** to interact with the game's  
native virtual memory and send virtual keys.  

![Script](demo_/overviewdemo.gif)  
  
This program reads the game's virtual memory in order to  
determine what side the player is on, and determine which  
scripts should be used when using one of the bound script keys. 

### Automatic Side Switch/Control Swap
![Script](demo_/SideSwitchDemo.gif)  

The Interactive GUI allows the player to choose which scripts, if  
any, they want to use while playing.
   
### Character-specific Script Selection from GUI
![Script](demo_/GuiDemo.gif)  
  
The script keys are:
- Left control (function 1)
- Right control (function 2)
- Left shift (function 3)
- Right shift (function 4)
- F5 (pause/unpause)
- ESC (immediately exit program)

## Todo
- [ ] Add more characters
- [ ] Make overlay only display over Tekken game
- [x] Disable input when Tekken is in the background **July 6, 2020**
- [ ] Find address of 'in-game' bool so that scripts only work inside of a match
- [x] Find a reliable way to produce executable versions of the program **July 3, 2020**
- [ ] Refactor utils
- [ ] ...

## Forever Todo
- [ ] bugfixes
- [ ] improve execution speed/reliability of keys

## Ambitious?
- [ ] wrap c++ version of SendInput into a custom module in place of pynput
- [ ] Only accept input if the player's frame advantage is withing buffer frame range ( +-3 )
