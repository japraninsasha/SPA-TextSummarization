import sys
from PyQt5 import QtWidgets
from transformers import pipeline
from gui import GUI

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Summarizer')
        self.setFixedSize(1200, 800)

        self.gui = GUI()
        self.setCentralWidget(self.gui)
        self.gui.summarize_button.clicked.connect(self.summarizeText)

    def summarizeText(self):
        input_text = self.gui.input_text.toPlainText()

        if not input_text.strip():
            self.gui.output_text.setPlainText("Morate unijti tekst za sumiranje.")
            return

        min_text_length = 20
        if len(input_text) < min_text_length:
            self.gui.output_text.setPlainText("Uneseni tekst je prekratak. Molimo vas da unesete tekst sa najmanje 20 karaktera.")
            return

        summary = summarizer(input_text, max_length=300, min_length=30, do_sample=False)
        self.gui.output_text.setPlainText(summary[0]['summary_text'])

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
