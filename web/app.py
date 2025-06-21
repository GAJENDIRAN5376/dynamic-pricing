from flask import Flask, render_template, request
from project.pricing import dynamic_price

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        base_price = float(request.form['base_price'])  # Get base price
        demand = request.form['demand']                 # Get demand level
        stock = int(request.form['stock'])              # Get stock
        result = dynamic_price(base_price, demand, stock)  # Calculate result
    return render_template('index.html', result=result)  # Show form and result

if __name__ == '__main__':
    app.run(debug=True)
