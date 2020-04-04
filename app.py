from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key="YOUR_FIXER.IO_API_KEY"
url="http://data.fixer.io/api/latest?access_key=" + api_key

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        firstCurrency=request.form.get("firstCurrency")
        secondCurrency=request.form.get("secondCurrency")
        amount=request.form.get("amount")
        response=requests.get(url)
        datas=response.json()
        firstValue=datas["rates"][firstCurrency]
        secondValue=datas["rates"][secondCurrency]

        result=(secondValue/firstValue) * float(amount)
        results=dict()
        results["firstCurrency"]=firstCurrency
        results["secondCurrency"]=secondCurrency
        results["result"]=result
        results["amount"]=amount


        return render_template('index.html',results=results)
    else:
        return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 