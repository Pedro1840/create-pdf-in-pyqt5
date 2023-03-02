from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtPrintSupport import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
import textwrap
from main_window import *
import sys

class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Ui_MainWindow = Ui_MainWindow()

        self.Ui_MainWindow.setupUi(self)

        self.Ui_MainWindow.textBrowser.setHtml("""SEU HTML""")

        wrapper = textwrap.TextWrapper(width=78)
  
        lines = wrapper.wrap(text=self.Ui_MainWindow.textBrowser.toPlainText())

        self.setWindowTitle('Exemplo de Aplicação com PyQT5')

        self.Ui_MainWindow.pushButton.clicked.connect(lambda: self.gerar_pdf(lines))

    def gerar_pdf(self, lista):
      # Cria um novo arquivo PDF
      pdf = canvas.Canvas("arquivo.pdf", pagesize=A4)

      # Configura as margens do documento
      margin_left = 50
      margin_bottom = 50
      page_width, page_height = A4
      max_y = page_height - margin_bottom
      current_y = max_y

      # Divide a lista em linhas de acordo com o limite de caracteres
      linhas = []
      linha_atual = []
      for item in lista:
          if len(' '.join(linha_atual + [item])) > 0:
              linhas.append(linha_atual)
              linha_atual = []
          linha_atual.append(item)
      linhas.append(linha_atual)

      # Percorre as linhas e escreve o conteúdo no PDF
      for linha in linhas:
          # Verifica se a linha atual excede o limite de espaço disponível
          if current_y - len(linha)*10 < 0:
              # Adiciona uma nova página ao PDF
              pdf.showPage()
              current_y = max_y

          # Escreve a linha no PDF
          for i, texto in enumerate(linha):
              pdf.drawString(margin_left, current_y - i*10, texto)

          # Atualiza a posição vertical atual
          current_y -= len(linha)*10 + 10

      # Salva o PDF gerado
      pdf.save()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApplication()
    ex.show()
    sys.exit(app.exec_())