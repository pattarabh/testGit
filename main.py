import numpy as np
import pandas as pd
from datetime import datetime
now = datetime.now()
date_str = now.strftime("%d/%m/%Y %H:%M:%S")
print("-"*45)
print("           Pattara Store INVOICE")
print("         As of", date_str)
print("-"*45)
print("Iphone 12 pro 128GB x 1      THB 39900")
print("Ipad pro 128GB x 1           THB 34900")
print("Air Pod x 1                  THB 5400")
print("MacBook Air x 1              THB 32900")
print("MacBook Pro x 1              THB 52900")
print("HomePod x 1                  THB 4900")
print("iMac x 1                     THB 120000")
print("Applecare x 1                THB 12000")
print("-"*45)
Subtotal = 39900+34900+5400+32900+52900+4900+120000+12000
VAT = Subtotal*0.07
Total = Subtotal + VAT
print("                         THB       "+ str(round(Subtotal,2)))
print("                     VAT THB       "+str(round(VAT,2)))
print("                   TOTAL THB       " +str(round(Total,2)))
print("-"*45)
print("Thank you for buying with us")
print("\U0001f600"*25)