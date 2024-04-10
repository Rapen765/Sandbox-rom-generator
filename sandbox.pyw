from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt, pyqtSlot
import clipboard
import sys

class SandBoxGenerator(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)
                self.text_input = QLineEdit()
                self.text_input.setFont(QFont("Arial",10))
                generate_button = QPushButton("Generate")
                copy_button = QPushButton("Copy rom")

                generate_button.clicked.connect(self.generate)
                copy_button.clicked.connect(self.copy)

                vbl = QVBoxLayout()
                vbl.addWidget(self.text_input)
                vbl.addWidget(generate_button)
                vbl.addWidget(copy_button)

                self.setLayout(vbl)
                self.setWindowTitle("SandBox Rom Generator")
        @pyqtSlot()
        def generate(self):
            expr = self.text_input.text()
            self.output = []
            for b in range(256):
                for a in range(256):
                    val = eval(expr) % 255
                    val = hex(val)
                    val.removeprefix("0x")
                    self.output.append(val)
        
        def copy(self):
                clipboard.copy("".join(self.output))
            

if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = SandBoxGenerator()
        win.show()
        sys.exit(app.exec_())
