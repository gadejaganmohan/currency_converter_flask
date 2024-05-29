import os
from dotenv import load_dotenv
from requests import get
from pprint import PrettyPrinter
load_dotenv()

BASE_URL = "https://api.freecurrencyapi.com" 
API_KEY = os.getenv("API_KEY")
endpoint = f"/v1/latest?apikey={API_KEY}"
print("Welcome to CURRENCY CONVERTER")
print("-----------------------------")
print("List - lists the different currencies \nConvert - Convert from one currency to another \nRate - get the exchange rate of two currencies")


def get_currency():

    printer = PrettyPrinter()
    url = BASE_URL + endpoint
    data = get(url).json()
    printer.pprint(data)

def exchange_rate(cur1,cur2):
    
     
    url = BASE_URL + endpoint + "&currencies=" + cur2 + "&base_currency=" + cur1

    data = get(url).json()
    rate = data['data']
    print(rate)
    value = rate[cur2]
    print("-------------------------------------")
    print(f"{cur1} -> {cur2} = {value}  ")
    print(F"One {cur1} is equal to {value} {cur2}")
    print("-------------------------------------")
    return value
def convert_currency(cur1,cur2,value):
   #endpoint = f"/v1/latest?apikey={API_KEY}&currencies={cur2}&base_currency={cur1}"
   conversion = exchange_rate(cur1,cur2)
   product = conversion * float(value)
   print(f"{value} {cur1} is equal to {product} {cur2}")
   print("----------------------------------------------")
   return product
def main(): 
 while True:
    choice = input("Enter a command (q to quit): ").lower()
    if choice == "list" or "convert" or "rate":
        if choice == "list":           
            get_currency()
        if choice == "rate":
            base = input("Enter Base currency: ").upper()
            convert = input("Enter a currency to convert to: ").upper()
            exchange_rate(base,convert)

        if choice == "convert":
            cur1 = input("Enter a base currency: " ).upper()
            while True:
                value = input(f"Enter an amount in {cur1}: ")
                if value.isdigit():
                    cur2 =  input("Enter a currency to convert to: ").upper()
                    convert_currency(cur1,cur2,value)
                    break
                

        elif choice == "q":
            print("Thank you see you :)")
            break
        else:
            print("Accepted values List, convert, rate: ")




