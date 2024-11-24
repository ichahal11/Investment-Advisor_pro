from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Mock function to get stock data (this should eventually call real data APIs)
def get_market_data(api_key, stock_symbols):
    market_data = {}
    for symbol in stock_symbols:
        # This is just an example of how you might fetch data (you need to replace this with a real API call)
        market_data[symbol] = {"latest_price": 100, "growth_rate": 5}  # Fake data
    return market_data

# Generate investment recommendations based on user's info
def generate_recommendation(client_data, market_data):
    recommendations = []
    
    if client_data["goal"] == "retirement":
        recommendations.append(f"Invest 50% in {list(market_data.keys())[0]} stocks.")
    else:
        recommendations.append(f"Invest 30% in {list(market_data.keys())[1]} stocks.")
    
    rationale = "Recommendations are based on your financial goal."
    return recommendations, rationale

# Home route where user inputs their data
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')  # Get name from form
        goal = request.form.get('goal')  # Get goal from form
        timeline = request.form.get('timeline')  # Get timeline from form
        
        api_key = 'your_alpha_vantage_api_key'  # You will get this from Alpha Vantage (or another API)
        stock_symbols = ['AAPL', 'GOOGL', 'AMZN']  # Stock symbols to track
        
        # Client data
        client_data = {'name': name, 'goal': goal, 'timeline': timeline}
        
        # Get stock data
        market_data = get_market_data(api_key, stock_symbols)
        
        # Get personalized recommendations
        recommendations, rationale = generate_recommendation(client_data, market_data)
        
        # Display the results on a new page
        return render_template('result.html', recommendations=recommendations, rationale=rationale)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
