from PyQt5.QtWidgets import  *
from pytube import YouTube
from moviepy.editor import *

class MainApp(QMainWindow):
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent=parent)

        #Se establece el tamanio de la ventana
        self.setFixedSize(300,300)
        self.setWindowTitle("mp3 downloader")

        #Boton
        self.button = QPushButton("Descargar MP3", self)
        self.button.setGeometry(50, 120, 200, 30)
        self.button.clicked.connect(self.descargar)

        #Entrada de texto
        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(50, 80, 200, 30)

        #Labels
        self.label_url = QLabel("URL", self)
        self.label_url.setGeometry(135, 40, 200, 30)
        self.label_estado = QLabel("", self)
        self.label_estado.setGeometry(20, 150, 200, 30)

        self.label_firma = QLabel("- insoportable -", self)
        self.label_firma.setGeometry(110, 230, 200, 30)

    # Metodo asociado al boton
    def descargar(self):
        # Se obtiene el url de la entrada de texto
        url = self.text_input.text()

        # Se crea un objeto YouTube a partir de la URL dada por el usuario
        # El metodo streams del objeto Youtube devuelve un objeto con las streams disponibles para el video
        # El metodo "get_audio_only" del objeto "streams" obtiene el audio solamente
        mp4 = YouTube(url).streams.get_audio_only()

        # Se descarga el audio MP4 del video
        mp4.download()

        # Se carga el audio mp4
        audiomp4 = AudioFileClip(mp4.default_filename)

        # Se extrae el nombre del archivo
        posicion = mp4.default_filename.find(".mp4")
        nombre = mp4.default_filename[0:posicion] + ".mp3"

        # Se realiza la conversion a MP3
        audiomp4.write_audiofile(nombre)

        # Se indica el nombre del archivo mp3 descargado
        self.label_estado.setText(nombre)

        # Se elimina el archivo de audio mp4 después de la conversion a mp3
        os.remove(mp4.default_filename)

if __name__ == '__main__':
    # Inicia la aplicacion
    app = QApplication([])
    # Crea la ventana
    window = MainApp()
    # Muestra la ventana
    window.show()
    # Ejecuta la aplicacion
    app.exec_()