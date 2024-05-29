from flask import Flask, render_template, request
from currency_converter import exchange_rate, convert_currency # Import your conversion functions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Render the HTML page with a form
    
@app.route("/convert", methods=["POST"])
def convert():
    base_currency = request.form["base_currency"].upper()
    convert_to = request.form["convert_to"].upper()
    amount = float(request.form["amount"])

    converted_value = convert_currency(base_currency, convert_to, amount)

    return render_template("result.html",converted_value=converted_value,converting=base_currency,converted=convert_to,result=amount)  # Render result page
 
