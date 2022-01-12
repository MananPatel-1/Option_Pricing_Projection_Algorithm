from ib_insync import *
from IPython.display import display, clear_output
import pandas as pd


ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)

option = Option("SPY", "20220112", 370, "C", "SMART")

# Asynchronous call
data = ib.reqMktData(option, "", False, False)
print(data)

# Call-Back function
def onPendingTicker(ticker):
    print("pending ticker event received")
    print(ticker)


ib.pendingTickersEvent += onPendingTicker

ib.run()
