# Syscan-Badge
#datasheets and some code for the badge handed out at Syscan 2015
I've grabbed the relevant datasheets for the STM32 processor used.

##dumping the current flash
Unfortunately the code is readout protected so dumping it over serial is not possible without some Travis Goodspeed style shenanigans
I haven't got a SWD debugger at the moment - so haven't been able to see if that can be connected.

##glitching
My next step will be to try a bit of glitching by trying to reduce the voltage lower then the voltage required by programming the flash during the 
"Mass Erase" step of the "Readout Unprotect" command. 

##programming
However you can erase the flash and program the code you want at the moment i believe. 
Just run the Readout Unprotect to enable programming again - unfortunately this'll wipe the present firmware :(.




