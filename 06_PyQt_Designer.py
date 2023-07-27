from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit, QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5 import uic
from PyQt5.QtGui import QFont
import sys


# Loading the ui as a class
class Ui(QMainWindow):
    def __init__(self):
        
        # Call the inherited classes __init__ method
        super(Ui, self).__init__() 
        
        # Load the Qt designer layout
        # self.uic.loadUi('06-mylayout.ui', self) # Load the .ui file
        self.ui = uic.loadUi('06-basic.ui', self) # Load the .ui file
        
        # Get widgets in the ui 
        # self.printbutton = self.findChild(QPushButton, 'printButton') 
        self.printbutton = self.ui.printButton
        self.modebutton = self.findChild(QPushButton, 'modeButton') 
        self.setbutton = self.findChild(QPushButton, 'setButton') 
        self.clearbutton = self.findChild(QPushButton, 'clearButton') 
        self.inputbox = self.findChild(QLineEdit, 'inputBox')
        # self.label = self.findChild(QLabel, 'label')
        self.label = self.ui.label
        
        # Set comboBox list
        self.combobox = self.ui.comboBox
        self.combobox.addItems(["Orange juice", "Apple juice", "Pineaple juice"]) 
        
        # Assign method to buttons
        self.printbutton.clicked.connect(self.printBtn_pressed) 
        self.setbutton.clicked.connect(self.setBtn_pressed) 
        self.clearbutton.clicked.connect(self.clearBtn_pressed) 
        
        # Show the layout
        self.show() # Show the GUI
        
    def printBtn_pressed(self):
        # This is executed when the printbutton is pressed
        self.label.setText(f"you wrote: {self.inputbox.text()} !")
    
    def setBtn_pressed(self):
        # This is executed when the printbutton is pressed
        self.label.setText(f"you chose: {self.combobox.currentText()} !")
            
    def clearBtn_pressed(self):
        # This is executed when the printbutton is pressed
        self.label.setText(f"")
        

if __name__ == "__main__":
    app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class

    # Run the app
    app.exec()
