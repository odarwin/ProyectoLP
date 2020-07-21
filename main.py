from tkinter import *
from tkinter import messagebox
from Lexico import analizador
from Lexico import tokens
from Sintactico import *
from ply.lex import LexToken
# def lexear(t):
#      analizador.input(t);
#      tokenRec = analizador.token()
#      tokensRec= []
#      while True:
#         if tokenRec != None:
#             tokensRec.insert(tokenRec)
#
#         else:
#             break
#         return tokensRec


def parsear(t):
    return parser.parse(t)

def fun():
    temp=""
    for tk in tokens:
        temp +="\t* "
        temp+=tk
        temp+="\n"

    messagebox.showinfo("Tokens Disponibles", temp)

class Aplicacion():
    def __init__(self):
        self.text_input = " "
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry("1000x700")
        self.root.title('Interfaz LengPro')




        self.txt1 = StringVar(value="\n\t\t\t\t¡INGRESA TU CODIGO DE DART!\t\t\t\t\n\n")

        self.txt2 = StringVar(value="Resultado del LEXER y PARSER:")

        self.lbl1 = Label(self.root, textvariable=self.txt1)
        self.lbl1.pack(side=TOP, padx=10, pady=3)
        self.bt= Button(self.root, text="Ver Tokens", command=fun)
        self.bt.pack(side=TOP, padx=10, pady=5)

        self.TextArea = Text(self.root, width=30, height=13)
        self.TextArea.pack(side=TOP, fill=BOTH)

        self.lbl2 = Label(self.root, textvariable=self.txt2)
        self.lbl2.pack(side=TOP, pady=10)

        self.TextResultado = Text(self.root, width=30, height=13, wrap=WORD)
        self.TextResultado.pack(side=TOP, fill=BOTH)

        self.Revisar = Button(self.root, fg='white', bg='green', width='20', height='2', text='Revisar Sintaxis', command=self.evaluate)
        self.Revisar.pack(side=LEFT, padx=10, pady=3)

        self.RevisarLexer = Button(self.root, fg='white', bg='blue', width='20', height='2', text='Revisar Lexer', command=self.evaluarLex)
        self.RevisarLexer.pack(side=LEFT, padx=30, pady=3)



        self.Salir = Button(self.root, fg='white', bg='red', width='20', height='2', text='Salir', command=self.root.destroy)
        self.Salir.pack(side=RIGHT, padx=10, pady=3)

        self.Revisar.focus_set()
        self.root.mainloop()

    def evaluarLex(self):
        self.TextResultado.delete(0.0, END)
        self.text_input = self.TextArea.get("1.0", "end-1c")  # Obtengo el texto quitando el salto de linea/ solo la primera linea
        lineas = self.text_input.split("\n")
        for elem in lineas:
            listaR=Lexico.analizarCadena(elem)
            for elem1 in listaR:
                self.TextResultado.insert(INSERT, str(elem1) +"\n")
# AQUI SE EVALUA LA PARTE SINTACTICA
    def evaluate(self):
        self.TextResultado.delete(0.0, END)
        self.text_input = self.TextArea.get("1.0", "end-1c")  # Obtengo el texto quitando el salto de linea/ solo la primera linea
        lineas = self.text_input.split("\n")
        #print(lineas)
        count = 1
        for linea in lineas:
            error.append("SINTAXIS CORRECTA!")
            parsear(linea)
            #print(error)
            self.TextResultado.insert(INSERT,"Línea "+str(count)+": "+ error[0]+"\n")
            count = count+1
            error.pop()


            #self.text_input=self.TextArea.get(0.0, END)
            #parts= self.text_input.split("\n")
            #for part in parts:
             #   print("indi %s  %s",len(parts),part)
              #  parsear(part)
             #   self.TextResultado.delete(0.0, END)
               # self.TextResultado.insert(INSERT, "Compiladoo!" )

def main():
    mi_app = Aplicacion()

    return 0

if __name__ == '__main__':
    main()
