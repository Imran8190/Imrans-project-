from flask import Flask, render_template, jsonify

app = Flask(__name__)

CHAINS = [
  {
    'id': 1,
    'Model Name':'KARUGAMANI CHAIN',
    'Model Size':'24 inches,34 inches',
    'Cost':'Rs.400,600'
  },
  {
    'id': 2,
    'Model Name':'SARADU CHAIN',
    'Model Size':'24 inches,34 inches',
    'Cost':'Rs.500,700'
  },
  {
    'id': 3,
    'Model Name':'THAAMBU KAIRU CHAIN',
    'Model Size':'24 inches,34 inches',
    'Cost':'Rs.600,800'
  },
  {
    'id': 4,
    'Model Name':'TENDULKAR CHAIN',
    'Model Size':'24 inches,34 inches',
    'Cost':'Rs.300,500'
  }
]

@app.route("/")

def bismillah():
    return render_template('home.html', 
 chains=CHAINS,company_name='NEW ROYAL GOLD COVERING')
@app.route("/api/chains")

def bismilla():
    return jsonify(CHAINS)

if (__name__)=="__main__":
  app.run(host='0.0.0.0',debug=True)
