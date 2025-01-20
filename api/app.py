from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from investment_bot import InvestmentBot
import joblib
import os


app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


# Load the trained model and scaler
model_path = os.path.join(os.path.dirname(__file__), 'models', 'random_forest_model.joblib')
scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'scaler.joblib')
feature_importance_path = os.path.join(os.path.dirname(__file__), 'models', 'feature_importance.joblib')

# Initialize the investment bot with the loaded model
try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature_importance = joblib.load(feature_importance_path)
    bot = InvestmentBot(model, scaler, feature_importance)
except FileNotFoundError:
    print("Warning: Model files not found. Please train the model first.")
    bot = None

@app.route('/api/market-analysis', methods=['GET'])
def get_market_analysis():
    if bot is None:
        return jsonify({"error": "Model not initialized"}), 500

    print("in get api")

    # Get latest market data
    latest_data = pd.DataFrame({
        'VIX': [25.5],
        'XAU BGNL': [1900.0],
        'DXY': [90.5],
        'MXUS': [3000.0],
        'MXJP': [1200.0],
        'GTITL30YR': [2.5]
    })

    # Get analysis from the bot
    analysis = bot.analyze_market_conditions(latest_data)
    print("'''''''''''''''''''''",analysis)
    return jsonify(analysis)

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
