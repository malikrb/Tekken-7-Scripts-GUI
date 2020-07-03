# Tekken 7 Script GUI
By: Malik R. Booker  
Created: June 30, 2020  
Last Updated: July 2, 2020

## Overview and Demonstration
![Script](demo_/OverviewDemo.gif)  
  
This program reads the game's virtual memory in order to  
determine what side the player is on, and determine which  
scripts should be used when using one of the bound script keys.  

### Automatic side switch control swap
![Script](demo_/SideSwitchDemo.gif)  
   
### Character-specific script selection from GUI
![Script](demo_/GuiDemo.gif)  
  
The script keys are:
- Left control (function 1)
- Right control (function 2)
- Left shift (function 3)
- Right shift (function 4)
- F5 (pause/unpause)

![Script](demo_/.gif)  

## Todo
- [ ] Add more characters
- [ ] Make overlay only display over Tekken game while Tekken HWND is active
- [ ] Find address of 'in-game' bool so that scripts only work inside of a match
- [x] Find a reliable way to produce executable versions of the program
- [ ] ...

## Forever Todo
- [ ] bugfixes
- [ ] improve execution speed/reliability of keys

## Ambitious?
- [ ] wrap c++ version of SendInput into a custom module in place of pynput
