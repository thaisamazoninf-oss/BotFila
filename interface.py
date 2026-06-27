import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import sys

from main4 import iniciar_automacao

class Console:
    def __init__(self, widget):
        self.widget = widget
    
    def write(self, texto):
        self.widget.insert("end", texto)
        self.widget.see("end")
    
    def flush(self):
        pass

janela = tk.Tk()
janela.title("Automação")

logs = ScrolledText(janela, width=70, height=30)
logs.pack()

#Todos os prints aparecem aqui
sys.stdout = Console(logs)

def executar():
    threading.Thread(
        target=iniciar_automacao,
        daemon=True
    ).start()
    
botao = tk.Button(
    janela,
    text="iniciar",
    command=executar
)

botao.pack()

janela.mainloop()