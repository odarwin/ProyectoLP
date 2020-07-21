import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy, QPlainTextEdit
import Lexico
def leer(ruta):
    with open(ruta, 'r') as file:
        s = file.read()
    return s

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("Proyecto de Lenguajes de Programación")
    win.setMinimumHeight(600)
    win.setMinimumWidth(600)
    # Creación del label ruta, cuadro de text y botón enviar(junto a sus respectivas funciones).
    labelRuta = QLabel()
    labelRuta.setText("Escriba su código en LUA")
    #Creación cuadro de texto donde se ingresa el código, o donde lo recibe de la ruta.
    codigo = QPlainTextEdit()
    policy1 = codigo.sizePolicy()
    policy1.setHorizontalPolicy(QSizePolicy.Expanding)
    codigo.setSizePolicy(policy1)
    #Creación del label análisis, y botones para sintáctico y semántico.
    labelAnalisis = QLabel()
    labelAnalisis.setText("Análisis:")
    botonSintactico = QPushButton()
    botonSintactico.setText("Sintáctico")
    policy3 = botonSintactico.sizePolicy()
    policy3.setHorizontalPolicy(QSizePolicy.Expanding)
    botonSintactico.setSizePolicy(policy3)
    botonLexer = QPushButton()
    botonLexer.setText("Lexer")
    policy4 = botonSintactico.sizePolicy()
    policy4.setHorizontalPolicy(QSizePolicy.Expanding)
    botonLexer.setSizePolicy(policy4)
    #Creación cuadro de texto donde se ingresa el código, o donde lo recibe de la ruta.
    resultado = QPlainTextEdit()
    policy5 = resultado.sizePolicy()
    policy5.setHorizontalPolicy(QSizePolicy.Expanding)
    resultado.setSizePolicy(policy5)
    def analisisS():
        text = codigo.toPlainText()
        resultado.clear()
        tokens = ["id", "=", "NUMBER"]
        for linea in tokens:
            resultado.appendPlainText(linea)
            print(linea)
    botonSintactico.clicked.connect(analisisS)
    def analisisL():
        text = codigo.toPlainText()
        resultado.clear()
        listaTokensR=Lexico.analizarLexico(text)
        for elem in listaTokensR:
            resultado.appendPlainText(str(elem))
    botonLexer.clicked.connect(analisisL)
    #Se agregan todos los widgets a sus respectivos layouts
    layoutRuta = QVBoxLayout()
    layoutRuta.addWidget(labelRuta)
    layoutRuta.addWidget(codigo)
    layoutAnalisis = QHBoxLayout()
    layoutAnalisis.addWidget(labelAnalisis)
    layoutAnalisis.addWidget(botonSintactico)
    layoutAnalisis.addWidget(botonLexer)
    layoutResultado = QVBoxLayout()
    layoutResultado.addWidget(resultado)
    #Se agregan todos los layouts al layout principal
    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layoutRuta)
    mainLayout.addLayout(layoutAnalisis)
    mainLayout.addLayout(layoutResultado)
    #Ejecución de la interfaz
    win.setLayout(mainLayout)
    win.show()
    sys.exit(app.exec_())

window()