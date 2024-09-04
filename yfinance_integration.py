import yfinance as yf

def get_current_price(ticker):
    """Obtém o preço atual do ativo usando yfinance."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period='1d')['Close'].iloc[-1]
        return price
    except Exception as e:
        print(f"Erro ao obter preço: {e}")
        return None

def fetch_price_history(ticker):
    """Obtém o histórico de preços do ativo usando yfinance."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='1y')
        data = []
        for index, row in hist.iterrows():
            data.append({
                'date': index.date(),
                'open': row['Open'],
                'low': row['Low'],
                'high': row['High'],
                'close': row['Close'],
                'volume': row['Volume']
            })
        return data
    except Exception as e:
        print(f"Erro ao obter histórico: {e}")
        return None
