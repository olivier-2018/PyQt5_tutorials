from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit, QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self, title:str=None):
        super().__init__()
        
        # Set Title
        self.setWindowTitle(title)
        
        # Set vertical layout 
        # self.setLayout(QVBoxLayout(self))  
        my_layout = QFormLayout()
        self.setLayout(my_layout)
        
        # Create a label (text in Qt window)
        my_label = QLabel("Form template:")    
        my_label.setFont(QFont("Helvetica", 18))
        my_layout.addRow(my_label)   
        
        # Add line
        my_line = QLineEdit(self)
        my_layout.addRow(my_line)
        
        # Create a button
        my_button = QPushButton("press me", clicked=lambda: fcn_button_press())
        my_layout.addRow(my_button)
        
        # Show app
        self.show()
    
        def fcn_button_press():
            """Use the Entry text to format the label
            """
            # Capture text
            my_label.setText(f"you wrote {my_line.text() } !") # only value passed
        
app = QApplication([])
mw = MainWindow(title="PyQt5 Turorials")

# Run the app
app.exec()
