import yfinance as yf

TICKERS=["7011.T","5803.T","8035.T"]

def main():
    for t in TICKERS:
        df=yf.download(t,period="2y",progress=False,auto_adjust=False)
        print(t,len(df))
if __name__=="__main__":
    main()
