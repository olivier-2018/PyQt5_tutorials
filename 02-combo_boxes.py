from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self, title:str=None):
        super().__init__()
        
        # Set Title
        self.setWindowTitle(title)
        
        # Set vertical layout 
        self.setLayout(QVBoxLayout(self))  
        
        # Create a label (text in Qt window)
        my_label = QLabel("Pick your favorite drink:")    
        my_label.setFont(QFont("Helvetica", 18))
        self.layout().addWidget(my_label)
        
        # Create an COMBO box (editable or not)
        my_combo = QComboBox(self,
                             editable = True,
                             insertPolicy = QComboBox.InsertAtBottom) 
        
        my_combo.addItem("Coke", "Something")                                   # Format: Text, Data
        my_combo.addItem("Fanta", 2)
        my_combo.addItem("Water", QWidget)
        my_combo.addItem("wine")
        my_combo.addItems(["Orange juice", "Apple juice", "Pineaple juice"])   # insert several items   
        my_combo.insertItem(1, "Pepsi")                                       # insert at given position 
        
        self.layout().addWidget(my_combo)
        
        # Create a button
        my_button = QPushButton("press me", clicked=lambda: fcn_button_press())
        self.layout().addWidget(my_button)
        
        # Show app
        self.show()
    
        def fcn_button_press():
            """Use the Entry text to format the label
            """
            # Capture text
            # my_label.setText(f"you picked {my_combo.currentText()} !")
            my_label.setText(f"you picked {my_combo.currentData()} !") # returns the 2nd object in the list
            # my_label.setText(f"you picked {my_combo.currentIndex()} !") # return the index of the item
            # clear entry box
        
app = QApplication([])
mw = MainWindow(title="PyQt5 Turorials")

# Run the app
app.exec()
