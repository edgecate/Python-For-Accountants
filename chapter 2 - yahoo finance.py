import yfinance as yf
stocks_list = ['MSFT', 'AAPL', 'FB', 'TSLA', 'NVDA']

for each_stock in stocks_list:
    stock = yf.Ticker(each_stock)
    recs = stock.recommendations
    print(recs)

    hist = stock.history(period="1mo")
    print(hist)

    fins = stock.financials
    bs = stock.balance_sheet
    cs = stock.cashflow

    recs.to_csv(f'{each_stock} recs.csv')
    hist.to_csv(f'{each_stock} hist.csv')
    fins.to_csv(f'{each_stock} fins.csv')
    bs.to_csv(f'{each_stock} bs.csv')
    cs.to_csv(f'{each_stock} cs.csv')
