# chemical_reaction_simulator
It is a ideal simulator for simulating chemical reactions in chemical reaction network. 

Assumptions of Ideal Simulator :
* At every time step it will make a list of possible reactions that can occur.
* Out of this possible reactions, it will pick the fastest one means one which has the highest rate constant.
* If there are multiple reactions in step 2 , then it will take at random any reaction from possible and fast ones.
* If there are no reactions in step 2 , then simulation will terminate.

It accepts the input of chemical reaction network as a xml file.

To run the Chemical World from terminal type command "python MainFrame.py"

To run the Chemical World in GUI type command "python GUI.py"

GUI contains following features :
* Simulate SCRN network from the xml file. It will ask for the time of simulation and list of chemicals to plot
* Simulate SCRN network from the txt file. It will ask for the time of simulation and list of chemicals to plot
* Run basic and advanced examples
* Evaluate simple expressions containing only addition and multiplication. There is no precedence rule. Expression should consist of only numbers,addition and multiplication sign.
