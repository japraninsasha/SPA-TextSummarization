from PyQt5 import QtWidgets, QtGui, QtCore

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.setStyleSheet("background-color: #212121; color: #ffffff;")

        font_path = r"C:\\Users\sasaj\Desktop\\TextSummarization\\TextSummarizer\\OpenSans-Regular.ttf"
        font_id = QtGui.QFontDatabase.addApplicationFont(font_path)
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QtGui.QFont(font_family)

        custom_font.setPointSize(12) 

        self.input_text = QtWidgets.QTextEdit(self)
        self.input_text.setStyleSheet("background-color: #424242; color: #ffffff; border-radius: 10px; padding: 10px;")
        self.input_text.setPlaceholderText("Unesite tekst ovdje...")
        self.input_text.setFont(custom_font)
        layout.addWidget(self.input_text)

        self.summarize_button = QtWidgets.QPushButton('Sumiraj', self)
        self.summarize_button.setStyleSheet("background-color: #f06292; color: #ffffff; border-radius: 10px; padding: 10px;")
        self.summarize_button.setFont(custom_font)
        layout.addWidget(self.summarize_button, alignment=QtCore.Qt.AlignHCenter)

        self.output_text = QtWidgets.QTextEdit(self)
        self.output_text.setStyleSheet("background-color: #424242; color: #ffffff; border-radius: 10px; padding: 10px;")
        self.output_text.setReadOnly(True)
        self.output_text.setFont(custom_font)
        layout.addWidget(self.output_text)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor(33, 33, 33))
        self.setPalette(p)
