import tkinter as tk
from interface import InvestmentApp
from database import create_tables

def main():
    # Cria as tabelas no banco de dados
    create_tables()

    # Inicia a interface gráfica
    root = tk.Tk()
    app = InvestmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
