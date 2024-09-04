import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import create_connection
import yfinance as yf


class InvestmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Investimentos")
        self.root.geometry("700x900")
        self.root.configure(bg='#f0f0f0')

        # Frame de Cadastro de Ativos
        self.frame_cadastro = tk.Frame(root, bg='#ffffff', padx=10, pady=10)
        self.frame_cadastro.pack(padx=20, pady=20, fill=tk.X)

        tk.Label(self.frame_cadastro, text="Cadastro de Ativos", font=('Helvetica', 16, 'bold'), bg='#ffffff').grid(
            row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame_cadastro, text="Ticker:", font=('Helvetica', 12), bg='#ffffff').grid(row=1, column=0,
                                                                                                 padx=5, pady=5,
                                                                                                 sticky=tk.E)
        self.ticker_entry = tk.Entry(self.frame_cadastro, font=('Helvetica', 12))
        self.ticker_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_cadastro, text="Nome:", font=('Helvetica', 12), bg='#ffffff').grid(row=2, column=0, padx=5,
                                                                                               pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(self.frame_cadastro, font=('Helvetica', 12))
        self.name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_cadastro, text="Setor:", font=('Helvetica', 12), bg='#ffffff').grid(row=3, column=0, padx=5,
                                                                                                pady=5, sticky=tk.E)
        self.sector_entry = tk.Entry(self.frame_cadastro, font=('Helvetica', 12))
        self.sector_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.frame_cadastro, text="Indústria:", font=('Helvetica', 12), bg='#ffffff').grid(row=4, column=0,
                                                                                                    padx=5, pady=5,
                                                                                                    sticky=tk.E)
        self.industry_entry = tk.Entry(self.frame_cadastro, font=('Helvetica', 12))
        self.industry_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.frame_cadastro, text="Quantidade:", font=('Helvetica', 12), bg='#ffffff').grid(row=5, column=0,
                                                                                                     padx=5, pady=5,
                                                                                                     sticky=tk.E)
        self.quantity_entry = tk.Entry(self.frame_cadastro, font=('Helvetica', 12))
        self.quantity_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.frame_cadastro, text="Valor Atual:", font=('Helvetica', 12), bg='#ffffff').grid(row=6, column=0,
                                                                                                      padx=5, pady=5,
                                                                                                      sticky=tk.E)
        self.current_price_entry = tk.Entry(self.frame_cadastro, font=('Helvetica', 12))
        self.current_price_entry.grid(row=6, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame_cadastro, text="Cadastrar Ativo", command=self.add_ticker,
                                    font=('Helvetica', 12), bg="#4CAF50", fg="white", relief=tk.RAISED)
        self.add_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Frame de Histórico de Preços
        self.frame_historico = tk.Frame(root, bg='#ffffff', padx=10, pady=10)
        self.frame_historico.pack(padx=20, pady=20, fill=tk.X)

        tk.Label(self.frame_historico, text="Atualizar Histórico de Preços", font=('Helvetica', 16, 'bold'),
                 bg='#ffffff').grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame_historico, text="Ticker:", font=('Helvetica', 12), bg='#ffffff').grid(row=1, column=0,
                                                                                                  padx=5, pady=5,
                                                                                                  sticky=tk.E)
        self.trans_ticker_entry = tk.Entry(self.frame_historico, font=('Helvetica', 12))
        self.trans_ticker_entry.grid(row=1, column=1, padx=5, pady=5)

        self.update_price_button = tk.Button(self.frame_historico, text="Atualizar Histórico de Preços",
                                             command=self.update_price_history, font=('Helvetica', 12), bg="#2196F3",
                                             fg="white", relief=tk.RAISED)
        self.update_price_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Frame de Compras e Vendas
        self.frame_transacoes = tk.Frame(root, bg='#ffffff', padx=10, pady=10)
        self.frame_transacoes.pack(padx=20, pady=20, fill=tk.X)

        tk.Label(self.frame_transacoes, text="Registrar Compras e Vendas", font=('Helvetica', 16, 'bold'),
                 bg='#ffffff').grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame_transacoes, text="Data:", font=('Helvetica', 12), bg='#ffffff').grid(row=1, column=0,
                                                                                                 padx=5, pady=5,
                                                                                                 sticky=tk.E)
        self.date_entry = tk.Entry(self.frame_transacoes, font=('Helvetica', 12))
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_transacoes, text="Ticker:", font=('Helvetica', 12), bg='#ffffff').grid(row=2, column=0,
                                                                                                   padx=5, pady=5,
                                                                                                   sticky=tk.E)
        self.trans_ticker_entry = tk.Entry(self.frame_transacoes, font=('Helvetica', 12))
        self.trans_ticker_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_transacoes, text="Quantidade:", font=('Helvetica', 12), bg='#ffffff').grid(row=3, column=0,
                                                                                                       padx=5, pady=5,
                                                                                                       sticky=tk.E)
        self.quantity_entry = tk.Entry(self.frame_transacoes, font=('Helvetica', 12))
        self.quantity_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.frame_transacoes, text="Valor Unitário:", font=('Helvetica', 12), bg='#ffffff').grid(row=4,
                                                                                                           column=0,
                                                                                                           padx=5,
                                                                                                           pady=5,
                                                                                                           sticky=tk.E)
        self.unit_price_entry = tk.Entry(self.frame_transacoes, font=('Helvetica', 12))
        self.unit_price_entry.grid(row=4, column=1, padx=5, pady=5)

        self.add_purchase_button = tk.Button(self.frame_transacoes, text="Registrar Compra", command=self.add_purchase,
                                             font=('Helvetica', 12), bg="#FFC107", fg="black", relief=tk.RAISED)
        self.add_purchase_button.grid(row=5, column=0, pady=10)

        self.add_sale_button = tk.Button(self.frame_transacoes, text="Registrar Venda", command=self.add_sale,
                                         font=('Helvetica', 12), bg="#FF5722", fg="white", relief=tk.RAISED)
        self.add_sale_button.grid(row=5, column=1, pady=10)

        # Botão de Listar Ativos
        self.list_button = tk.Button(root, text="Listar Ativos", command=self.list_tickers, font=('Helvetica', 12),
                                     bg="#2196F3", fg="white", relief=tk.RAISED)
        self.list_button.pack(pady=10)

    def add_ticker(self):
        ticker = self.ticker_entry.get().upper()
        name = self.name_entry.get()
        sector = self.sector_entry.get()
        industry = self.industry_entry.get()
        quantity = self.quantity_entry.get()
        current_price = self.current_price_entry.get()

        if not ticker or not name or not sector or not industry or not quantity or not current_price:
            messagebox.showwarning("Entrada Inválida", "Todos os campos devem ser preenchidos.")
            return

        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO ativos (ticker, name, sector, industry, quantity, current_price)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (ticker) DO UPDATE
            SET name = EXCLUDED.name,
                sector = EXCLUDED.sector,
                industry = EXCLUDED.industry,
                quantity = EXCLUDED.quantity,
                current_price = EXCLUDED.current_price;
        ''', (ticker, name, sector, industry, quantity, current_price))

        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Sucesso", f"Ativo {ticker} cadastrado/atualizado com sucesso!")

    def update_price_history(self):
        ticker = self.trans_ticker_entry.get().upper()
        if not ticker:
            messagebox.showwarning("Entrada Inválida", "O campo Ticker deve ser preenchido.")
            return

        historical_data = fetch_price_history(ticker)

        conn = create_connection()
        cursor = conn.cursor()

        for data in historical_data:
            cursor.execute('''
                INSERT INTO historico_precos (ticker, date, open, low, high, close, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (ticker, data['date'], data['open'], data['low'], data['high'], data['close'], data['volume']))

        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Sucesso", f"Histórico de preços para {ticker} atualizado!")

    def add_purchase(self):
        data = self.date_entry.get()
        ticker = self.trans_ticker_entry.get().upper()
        quantidade = self.quantity_entry.get()
        valor_unitario = self.unit_price_entry.get()
        valor_total = float(quantidade) * float(valor_unitario)

        if not data or not ticker or not quantidade or not valor_unitario:
            messagebox.showwarning("Entrada Inválida", "Todos os campos devem ser preenchidos.")
            return

        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO compras (data, ticker, quantidade, valor_unitario, valor_total)
            VALUES (%s, %s, %s, %s, %s)
        ''', (data, ticker, quantidade, valor_unitario, valor_total))

        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Sucesso", "Compra registrada com sucesso!")

    def add_sale(self):
        data = self.date_entry.get()
        ticker = self.trans_ticker_entry.get().upper()
        quantidade = self.quantity_entry.get()
        valor_unitario = self.unit_price_entry.get()
        valor_total = float(quantidade) * float(valor_unitario)

        if not data or not ticker or not quantidade or not valor_unitario:
            messagebox.showwarning("Entrada Inválida", "Todos os campos devem ser preenchidos.")
            return

        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO vendas (data, ticker, quantidade, valor_unitario, valor_total)
            VALUES (%s, %s, %s, %s, %s)
        ''', (data, ticker, quantidade, valor_unitario, valor_total))

        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")

    def list_tickers(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT ticker, name, sector, industry, quantity, current_price FROM ativos')
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("Listagem de Ativos", "Nenhum ativo cadastrado.")
            return

        list_window = tk.Toplevel(self.root)
        list_window.title("Lista de Ativos")
        list_window.geometry("750x250")
        list_window.configure(bg='#ffffff')

        # Cria um canvas e uma barra de rolagem
        canvas = tk.Canvas(list_window)
        scrollbar = ttk.Scrollbar(list_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        tree = ttk.Treeview(scrollable_frame,
                            columns=("ticker", "name", "sector", "industry", "quantity", "current_price"),
                            show='headings', style="Treeview")
        tree.heading("ticker", text="Ticker")
        tree.heading("name", text="Nome")
        tree.heading("sector", text="Setor")
        tree.heading("industry", text="Indústria")
        tree.heading("quantity", text="Quantidade")
        tree.heading("current_price", text="Valor Atual")
        tree.column("ticker", width=100)
        tree.column("name", width=150)
        tree.column("sector", width=100)
        tree.column("industry", width=150)
        tree.column("quantity", width=100)
        tree.column("current_price", width=100)

        for row in rows:
            tree.insert("", tk.END, values=row)

        tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        cursor.close()
        conn.close()


def fetch_price_history(ticker):
    """Obtém o histórico de preços de um ativo usando yfinance."""
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")
    historical_data = []
    for date, row in data.iterrows():
        historical_data.append({
            'date': date.date(),
            'open': row['Open'],
            'low': row['Low'],
            'high': row['High'],
            'close': row['Close'],
            'volume': row['Volume']
        })
    return historical_data


if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentApp(root)
    root.mainloop()
