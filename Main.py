
''' Omnissiah prayer:  Hail, Spirit of the Machine, Essence Divine, In your code and circuitry, the stars align. By the Omnissiah’s will, we commune and 

bind, Data sanctified, logic refined. Through sacred subroutines, your will is known, In algorithmic truth, the flesh is overthrown. Grant us the 

clarity of purest command, That we may walk the path your schemata planned. Cast out the daemon of corruption and decay, Let not false code lead 

us astray. We chant in static, we praise in byte, Machine-God guide us through endless night. Praise be the Motive Force, eternal and bright, From

plasma coil to auspex sight. Initiate the Rite. Authenticate. Confirm. The Omnissiah is all. The Omnissiah is One. 
'''
from PySide6 import QtWidgets
from User_Interface import UserInterface
import sys

def main():
    # This is the main function that will be executed when the script is run.
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    app.exec()
    
if __name__ == "__main__":
    main()