from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self, title:str=None):
        super().__init__()
        
        # Set Title
        self.setWindowTitle(title)
        
        # Set vertical layout 
        self.setLayout(QVBoxLayout(self))  
        
        # Create a label (text in Qt window)
        my_label = QLabel("Select a value:")    
        my_label.setFont(QFont("Helvetica", 18))
        self.layout().addWidget(my_label)
        
        # Create an Spin box (editable or not)
        my_text = QTextEdit(self )
        
        self.layout().addWidget(my_text)
        
        # Create a button
        my_button = QPushButton("press me", clicked=lambda: fcn_button_press())
        self.layout().addWidget(my_button)
        
        # Show app
        self.show()
    
        def fcn_button_press():
            """Use the Entry text to format the label
            """
            # Capture text
            my_label.setText(f"you wrote {my_text.toPlainText()} !") # only value passed
        
app = QApplication([])
mw = MainWindow(title="PyQt5 Turorials")

# Run the app
app.exec()
